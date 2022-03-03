from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class min(TestCase):
    def test_feladat01(self):
        adat = "3,2; -2,4; -3,5; -6,7; 4,3; -3,9; -2,1; 0,6; 1,5"
        aktualis = feladatok.min(adat)
        elvart = -6.7
        self.assertEqual(elvart, aktualis, adat+" számok legkisebb elemét nem jól határozta meg")
    def test_feladat02(self):
        adat = "5.5"
        aktualis = feladatok.min(adat)
        elvart = 5.5
        self.assertEqual(elvart, aktualis, adat+" számok legkisebb elemét nem jól határozta meg")
    def test_feladat03(self):
        adat = "3,2; -2,4; -3,5; -6,7; 4,3; -3,9; -2,1; 0,6; 1,5; -8.3"
        aktualis = feladatok.min(adat)
        elvart = -8.3
        self.assertEqual(elvart, aktualis, adat+" számok legkisebb elemét nem jól határozta meg")
    def test_feladat04(self):
        adat = ""
        aktualis = feladatok.min(adat)
        elvart = None
        self.assertEqual(elvart, aktualis, " üres string legkisebb elemét nem jól határozta meg")