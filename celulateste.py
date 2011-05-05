'''
    Teste para a classe Celula da unit celula.py
'''
import celula
import unittest

class TesteDeCelula(unittest.TestCase):
    def setUp(self):
        self.celula = Celula(0)
    def testDeveIniciarComNivel0(self):
        self.assertEqual(self.celula.nivel, 0)
    def testDeveIncrementarONivelPara1(self):
        self.celula.tocar()
        self.assertEqual(self.celula.nivel, 1)
        

if __name__ == '__main__':
    unittest.main()
        