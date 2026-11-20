import io
import json

from tests.helpers import DBCase
from ucoach.mcp.server import Server, serve


class ServerTest(DBCase):
    def setUp(self):
        super().setUp()
        self.s = Server(self.db)

    def call(self, method, params=None, id_=1):
        msg = {"jsonrpc": "2.0", "id": id_, "method": method}
        if params is not None:
            msg["params"] = params
        return self.s.handle(msg)

    def test_initialize_echoes_supported_version(self):
        r = self.call("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "t"}})
        self.assertEqual(r["result"]["protocolVersion"], "2025-06-18")
        self.assertIn("tools", r["result"]["capabilities"])
        self.assertIn("instructions", r["result"])

    def test_initialize_unknown_version_falls_back_to_latest(self):
        r = self.call("initialize", {"protocolVersion": "2099-01-01"})
        self.assertEqual(r["result"]["protocolVersion"], "2025-11-25")

    def test_server_discover_gets_method_not_found_immediately(self):
        r = self.call("server/discover", {})
        self.assertEqual(r["error"]["code"], -32601)

    def test_notifications_get_no_response(self):
        self.assertIsNone(self.s.handle({"jsonrpc": "2.0", "method": "notifications/initialized"}))

    def test_tools_have_annotations_and_strict_schemas(self):
        tools = self.call("tools/list")["result"]["tools"]
        self.assertGreaterEqual(len(tools), 17)
        for t in tools:
            self.assertIn("readOnlyHint", t["annotations"])
            self.assertFalse(t["annotations"]["destructiveHint"])
            self.assertFalse(t["inputSchema"].get("additionalProperties", True), t["name"])

    def test_invalid_arguments_return_tool_error(self):
        r = self.call("tools/call", {"name": "registrar_sueno", "arguments": {"horas": "muchas"}})
        self.assertTrue(r["result"]["isError"])
        r = self.call("tools/call", {"name": "registrar_sueno", "arguments": {"horas": 7, "extra": 1}})
        self.assertTrue(r["result"]["isError"])

    def test_tool_call_returns_structured_content(self):
        r = self.call("tools/call", {"name": "registrar_sueno", "arguments": {"horas": 7.5, "fecha": "2026-11-19"}})
        self.assertFalse(r["result"].get("isError", False))
        self.assertEqual(r["result"]["structuredContent"]["estado"], "bien")

    def test_prompts_and_resources(self):
        names = {p["name"] for p in self.call("prompts/list")["result"]["prompts"]}
        self.assertTrue({"brief_manana", "cierre_dia", "revision_semanal", "retomar", "preparar_momento_clave",
                         "onboarding"} <= names)
        msg = self.call("prompts/get", {"name": "brief_manana"})["result"]["messages"][0]
        self.assertIn("planificar_dia", msg["content"]["text"])
        uris = {r["uri"] for r in self.call("resources/list")["result"]["resources"]}
        self.assertIn("ucoach://privacidad", uris)
        self.assertEqual(self.call("resources/read", {"uri": "ucoach://nada"})["error"]["code"], -32602)

    def test_stdio_loop(self):
        lines = "\n".join(json.dumps(m) for m in [
            {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-11-25"}},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 2, "method": "ping"},
            "basura"]) + "\nno es json\n"
        out = io.StringIO()
        serve(io.StringIO(lines), out)
        responses = [json.loads(x) for x in out.getvalue().splitlines()]
        self.assertEqual([r.get("id") for r in responses[:2]], [1, 2])
        self.assertEqual(responses[-1]["error"]["code"], -32700)
