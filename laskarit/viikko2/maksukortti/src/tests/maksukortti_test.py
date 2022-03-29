import unittest
from maksukortti import Maksukortti

def test_konstruktori_asettaa_saldon_oikein(self):
    kortti = Maksukortti(10)
    self.assertEqual(str(kortti), "Kortilla on rahaa 9 euroa")

