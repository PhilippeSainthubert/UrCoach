import random
import re
from datetime import datetime

from tests.helpers import DBCase
from ucoach import nudge
from ucoach.core.planner import plan_day

THURSDAY = datetime(2026, 11, 19)


def at(hhmm):
    h, m = map(int, hhmm.split(":"))
    return THURSDAY.replace(hour=h, minute=m)


class NudgeTest(DBCase):
    def run_at(self, hhmm, rng_value=0.0):
        sent = []
        d = nudge.decide(self.db, at(hhmm), rng=random.Random())
        if "tipo" in d:
            r = nudge.run(self.db, at(hhmm), sender=lambda text, p: sent.append(text) or "prueba")
            return r, sent
        return d, sent

    def test_templates_have_no_numbers_about_health_or_user_text(self):
        for kind, text in nudge.TEMPLATES.items():
            self.assertNotRegex(text, r"\b\d+([.,]\d+)?\s*h\b", kind)
            self.assertNotIn("{", text)

    def test_budget_and_gap(self):
        self.db.set_profile({"avisos_max_dia": 2, "avisos_probabilidad": 1.0})
        sent_times = []
        for hhmm in ["07:30", "08:00", "09:00", "09:30", "15:00", "15:30", "17:00", "21:00", "22:00"]:
            r = nudge.run(self.db, at(hhmm), sender=lambda t, p: "prueba")
            if r.get("enviar"):
                sent_times.append(hhmm)
        self.assertLessEqual(len(sent_times), 2)
        mins = [int(h[:2]) * 60 + int(h[3:]) for h in sent_times]
        self.assertTrue(all(b - a >= 60 for a, b in zip(mins, mins[1:])))

    def test_never_more_than_four_even_if_profile_says_more(self):
        self.db.conn.execute("INSERT OR REPLACE INTO profile VALUES ('avisos_max_dia', '9')")
        self.db.conn.commit()
        for i in range(6):
            self.db.conn.execute("INSERT INTO nudges (ts, date, kind, sent) VALUES (?,?,?,1)",
                                 (at("07:00").replace(minute=i).isoformat(), "2026-11-19", f"k{i}"))
        self.db.conn.commit()
        self.assertEqual(nudge.decide(self.db, at("15:00"))["motivo"], "presupuesto del día agotado")

    def test_silence_before_wake_after_bedtime_and_on_days_off(self):
        self.assertEqual(nudge.decide(self.db, at("06:00"))["motivo"], "horas de silencio")
        self.assertEqual(nudge.decide(self.db, at("22:45"))["motivo"], "horas de silencio")
        saturday = datetime(2026, 11, 21, 15, 0)
        self.assertEqual(nudge.decide(self.db, saturday)["motivo"], "día libre")

    def test_no_nudges_during_focus_block_or_meeting(self):
        plan = plan_day(self.db, THURSDAY.date(), [{"inicio": "15:00", "fin": "16:00", "titulo": "x"}])
        focus = next(b for b in plan["bloques"] if b["tipo"] == "foco")
        self.assertIn("foco", nudge.decide(self.db, at(focus["inicio"]))["motivo"])
        self.assertEqual(nudge.decide(self.db, at("15:30"))["motivo"], "en una reunión")

    def test_hoy_no_and_snooze(self):
        nudge.today_no(self.db, THURSDAY.date())
        self.assertEqual(nudge.decide(self.db, at("15:00"))["motivo"], "hoy no")
        self.db.set_profile({"hoy_no": None})
        nudge.snooze(self.db, 2, at("14:30"))
        self.assertEqual(nudge.decide(self.db, at("15:00"))["motivo"], "snooze")

    def test_randomized_decisions_are_logged_even_if_not_sent(self):
        self.db.set_profile({"avisos_probabilidad": 0.0})
        r = nudge.run(self.db, at("15:00"), sender=lambda t, p: self.fail("no debería enviarse"))
        self.assertEqual(r["tipo"], "bajon_tarde")
        self.assertFalse(r["enviar"])
        row = self.db.one("SELECT sent FROM nudges WHERE kind='bajon_tarde'")
        self.assertEqual(row["sent"], 0)
        # No se repite el mismo tipo el mismo día.
        self.assertNotEqual(nudge.decide(self.db, at("16:00")).get("tipo"), "bajon_tarde")

    def test_sostener_mode_only_keeps_light_and_wind_down(self):
        self.db.set_profile({"modo": "sostener"})
        self.assertNotIn("tipo", nudge.decide(self.db, at("15:00")))
        self.assertEqual(nudge.decide(self.db, at("22:00"))["tipo"], "desconexion")
