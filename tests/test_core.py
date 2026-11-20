import os
import stat
from datetime import date, datetime, timedelta

from tests.helpers import DBCase
from ucoach.core import coach, extras
from ucoach.mcp.server import Server

DAY = date(2026, 11, 19)


class CoreTest(DBCase):
    def test_permissions(self):
        mode = stat.S_IMODE(os.stat(self.db.dir).st_mode)
        self.assertEqual(mode, 0o700)
        self.assertEqual(stat.S_IMODE(os.stat(self.db.dir / "ucoach.db").st_mode), 0o600)

    def test_undo_restores_previous_value(self):
        self.db.upsert("sleep", {"date": "2026-11-19", "hours": 7.0, "source": "manual"}, "registrar_sueno")
        self.db.upsert("sleep", {"date": "2026-11-19", "hours": 4.0, "source": "manual"}, "registrar_sueno")
        self.db.undo()
        self.assertEqual(self.db.one("SELECT hours FROM sleep")["hours"], 7.0)
        self.db.undo()
        self.assertIsNone(self.db.one("SELECT hours FROM sleep"))

    def test_only_one_focal_habit(self):
        coach.define_habit(self.db, "Luz solar matinal", focal=True)
        coach.define_habit(self.db, "Lectura 20 min", focal=True)
        focal = [r["name"] for r in self.db.q("SELECT name FROM habits WHERE focal=1")]
        self.assertEqual(focal, ["Lectura 20 min"])

    def test_weekly_review_keeps_focal_habit(self):
        coach.define_habit(self.db, "Luz solar matinal", focal=True, weekly_target=5)
        coach.log_habit(self.db, "Luz solar matinal", DAY)
        r = coach.weekly_review(self.db, DAY)
        self.assertIn("Mismo hábito focal", r["sugerencias"][0])
        self.assertLessEqual(len(r["sugerencias"]), 3)
        self.assertFalse(r["energia_segun_sueno"]["disponible"])

    def test_sleep_energy_comparison_needs_enough_data(self):
        for i in range(20):
            d = DAY - timedelta(days=i)
            self.sleep(d.isoformat(), 7.5 if i % 2 else 5.5)
            self.db.conn.execute("INSERT INTO checkins (ts, energy) VALUES (?, ?)",
                                 (datetime.combine(d, datetime.min.time()).replace(hour=20).isoformat(),
                                  4 if i % 2 else 2))
        self.db.conn.commit()
        r = coach.sleep_energy_comparison(self.db, DAY)
        self.assertTrue(r["disponible"])
        self.assertEqual(r["diferencia_energia"], 2.0)
        self.assertIn("no una prueba de causa", r["lectura"])

    def test_inactivity_suggests_retomar(self):
        self.sleep((DAY - timedelta(days=5)).isoformat(), 7)
        self.assertTrue(coach.day_context(self.db, DAY)["sugerir_ritual_retomar"])

    def test_mood_signal_suggests_referral_type_only(self):
        for i in range(7):
            ts = datetime.combine(DAY - timedelta(days=i), datetime.min.time()).replace(hour=21).isoformat()
            self.db.conn.execute("INSERT INTO checkins (ts, mood) VALUES (?, 2)", (ts,))
        self.db.conn.commit()
        self.assertIn("animo-bajo-persistente", coach.day_context(self.db, DAY)["senales_para_derivar"])

    def test_ergonomics_questions_then_score(self):
        q = extras.ergonomics(self.db, None)
        self.assertGreaterEqual(len(q["preguntas"]), 10)
        r = extras.ergonomics(self.db, {"pies_apoyados": False, "sin_reflejos": True})
        self.assertEqual(r["puntuacion"], 50)
        with self.assertRaises(ValueError):
            extras.ergonomics(self.db, {"inventada": True})

    def test_experiment_flow(self):
        os.environ["UCOACH_NOW"] = "2026-11-19T08:00"
        r = extras.experiment(self.db, "crear", "Último café", "14:00", "16:00", 14)
        self.assertIn(r["hoy"], ("A", "B"))
        self.assertIn(extras.experiment(self.db, "hoy")["hoy"], ("A", "B"))
        self.assertIn("Aún no hay datos", extras.experiment(self.db, "resumen")["lectura"])

    def test_agenda_audit(self):
        ev = [{"fecha": "2026-11-19", "inicio": "09:00", "fin": "11:30"}, {"fecha": "2026-11-19", "inicio": "20:00", "fin": "21:00"}]
        r = extras.audit_agenda(self.db, ev, days=1)
        self.assertEqual(r["cadenas_de_2h_o_mas"], 1)
        self.assertEqual(r["reuniones_fuera_de_horario"], 1)

    def test_server_profile_validation(self):
        s = Server(self.db)
        bad = s.call_tool("perfil", {"cronotipo": "lechuza"})
        self.assertTrue(bad["isError"])
        ok = s.call_tool("perfil", {"cronotipo": "buho", "hora_dormir": "00:30"})
        self.assertEqual(ok["structuredContent"]["cronotipo"], "buho")
