import os
import tempfile
import unittest
from pathlib import Path

from ucoach.db import DB


class DBCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["UCOACH_HOME"] = self.tmp.name
        os.environ.pop("UCOACH_NOW", None)
        self.db = DB(Path(self.tmp.name))

    def tearDown(self):
        self.db.close()
        os.environ.pop("UCOACH_NOW", None)
        self.tmp.cleanup()

    def sleep(self, iso, hours, bed=None, wake=None):
        self.db.conn.execute("INSERT OR REPLACE INTO sleep (date, hours, bedtime, waketime, source) VALUES (?,?,?,?,?)",
                             (iso, hours, bed, wake, "manual"))
        self.db.conn.commit()
