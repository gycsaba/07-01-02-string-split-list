from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestAtlag(TestCase):
    def test_feladat01(self):
        adat = "5, 3, 2, 5, 2"
        aktualis = feladatok.atlag(adat)
        elvart = 3.4
        self.assertEqual(elvart, aktualis, adat+" számok átlagát nem jól határozta meg")
    def test_feladat02(self):
        adat = "5"
        aktualis = feladatok.atlag(adat)
        elvart = 5
        self.assertEqual(elvart, aktualis, adat+" számok átlagát nem jól határozta meg")
    def test_feladat03(self):
        adat = ""
        aktualis = feladatok.atlag(adat)
        elvart = None
        self.assertEqual(elvart, aktualis, "Üres stringben nincs szám, nincs átlag")