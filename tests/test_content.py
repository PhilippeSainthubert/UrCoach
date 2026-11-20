import json
import unittest

from ucoach.core.util import CONTENT, load_json
from ucoach.lint import lint_builtin, lint_paths, lint_text

LEVELS = {"A", "B", "C", "D"}


class ContentTest(unittest.TestCase):
    def test_practices_schema(self):
        items = load_json("practicas.json")
        self.assertGreaterEqual(len(items), 52)
        ids = [p["id"] for p in items]
        self.assertEqual(len(ids), len(set(ids)))
        for p in items:
            self.assertIn(p["nivel"], LEVELS, p["id"])
            for k in ("practica", "para_que", "evidencia", "fuente", "pauta", "revisado_el", "areas"):
                self.assertIn(k, p, p["id"])

    def test_known_levels_from_research(self):
        by_id = {p["id"]: p for p in load_json("practicas.json")}
        text = json.dumps(by_id, ensure_ascii=False).lower()
        self.assertIn("grounding", text)
        grounding = [p for p in by_id.values() if "grounding" in p["practica"].lower()]
        self.assertEqual(grounding[0]["nivel"], "D")
        craneal = [p for p in by_id.values() if "craneal" in p["practica"].lower()]
        self.assertEqual(craneal[0]["nivel"], "D")

    def test_referral_table(self):
        items = {d["tipo"]: d for d in load_json("derivacion.json")}
        self.assertGreaterEqual(len(items), 12)
        self.assertIn("024", json.dumps(items["ideacion-suicida"], ensure_ascii=False))
        self.assertTrue(items["ideacion-suicida"]["detiene_coaching"])
        self.assertNotIn("insomnio", items["dificultad-habitual-para-dormir"]["texto"].lower())

    def test_library(self):
        books = load_json("biblioteca.json")
        self.assertGreaterEqual(len(books), 104)
        self.assertEqual(len({b["id"] for b in books}), len(books))

    def test_no_long_dashes_in_content(self):
        for f in CONTENT.rglob("*"):
            if f.is_file():
                text = f.read_text(encoding="utf-8")
                self.assertNotIn("—", text, f.name)
                self.assertNotIn("–", text, f.name)

    def test_lint_catches_and_respects_negation(self):
        self.assertTrue(lint_text("Ucoach diagnostica tu insomnio"))
        self.assertFalse(lint_text("No está destinada a diagnosticar ninguna enfermedad"))

    def test_builtin_texts_and_content_pass_lint(self):
        found = lint_builtin() + lint_paths([str(CONTENT)])
        self.assertEqual(found, [], "\n".join(f"{f['donde']}: {f['texto']}" for f in found))
