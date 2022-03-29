import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_rahamaara_oikea(self):
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
    
    def test_myytyjen__edullisten_lounaiden_maara_oikea(self):
        self.assertEqual(str(self.kassapaate.edulliset), '0')
        
    def test_myytyjen__maukkaitten_lounaiden_maara_oikea(self):
        self.assertEqual(str(self.kassapaate.maukkaat), '0')
        
    def test_kassan_rahamaara_oikea_edullisen_oston_jalkeen_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(260)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100240')
        
    def test_kassan_rahamaara_oikea_maukkaan_oston_jalkeen_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100400')
        
    def test_maksu_riittava_myydyt_edulliset_kasvaa_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(str(self.kassapaate.edulliset), '1')
        
    def test_maksu_riittava_myydyt_maukkaat_kasvaa_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(str(self.kassapaate.maukkaat), '1')
        
    def test_maksu_ei_riittava_edulliseen_maarat_oikeat_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.edulliset), '0')
        
    def test_maksu_ei_riittava_maukkaaseen_maarat_oikeat_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        self.assertEqual(str(self.kassapaate.maukkaat), '0')
        
    def test_kortilla_tarpeeksi_edulliseen_veloitetaan_summa(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti.saldo), '760')

    def test_kortilla_tarpeeksi_maukkaaseen_veloitetaan_summa(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti.saldo), '600')
        
    def test_palauttaa_true_jos_rahat_riittivat_edulliseen(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(1000))
        testValue = True
        self.assertTrue(testValue, '760')
        
    def test_palauttaa_true_jos_rahat_riittivat_maukkaaseen(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(1000))
        testValue = True
        self.assertTrue(testValue, '600')
        
    def test_maksu_riittava_myydyt_edulliset_kasvaa_kortti(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(1000))
        self.assertEqual(str(self.kassapaate.edulliset), '1')
        
    def test_maksu_riittava_myydyt_maukkaat_kasvaa_kortti(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(1000))
        self.assertEqual(str(self.kassapaate.maukkaat), '1')
        
    def test_kortilla_ei_tarpeeksi_edulliseen_kortin_summa_muuttumaton(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti.saldo), '200')
        
    def test_kortilla_ei_tarpeeksi_maukkaaseen_kortin_summa_muuttumaton(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti.saldo), '200')
        
    def test_maksu_ei_riittava_edulliseen_maarat_oikeat_kortti(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(200))
        self.assertEqual(str(self.kassapaate.edulliset), '0')
        
    def test_maksu_ei_riittava_maukkaaseen_maarat_oikeat_kortti(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(200))
        self.assertEqual(str(self.kassapaate.maukkaat), '0')
        
    def test_palauttaa_false_jos_rahat_ei_riita_edulliseen_kortti(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(200))
        testValue = False
        self.assertFalse(testValue, '200')
        
    def test_palauttaa_false_jos_rahat_ei_riita_maukkaaseen_kortti(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(200))
        testValue = False
        self.assertFalse(testValue, '200')
        
    def test_kassa_ei_muutu_korttiostolla_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(Maksukortti(1000))
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        
    def test_kassa_ei_muutu_korttiostolla_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(1000))
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')
        
    def test_kortille_lataus_saldo_muuttuu(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 500)
        self.assertEqual(str(self.maksukortti.saldo), '1500')
        
    def test_kortille_lataus_kassan_rahamaara_muuttuu(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100200')
        
    def test_kortille_negatiivinen_lataus_saldo_ei_muutu(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(str(self.maksukortti.saldo), '1000')
        
    def test_kortille_negatiivinen_lataus_kassan_rahamaara_ei_muuttu(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -400)
        self.assertEqual(str(self.kassapaate.kassassa_rahaa), '100000')

        

        

        