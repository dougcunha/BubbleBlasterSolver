#coding: utf-8

import unittest
import buble_eng

class TestBlubleEng(unittest.TestCase):

    def setUp(self):
        self.eng = buble_eng.BubleEng()
        self.eng.newgame("""
            
            4 4 0
            0 1 4
            4 0 1
            
            """)

    def test_board(self):
        self.assertTrue(self.eng.get(0,0) == 4)
        self.assertTrue(self.eng.get(0,1) == 4)
        self.assertTrue(self.eng.get(0,2) == 0)
        self.assertTrue(self.eng.get(1,0) == 0)
        self.assertTrue(self.eng.get(1,1) == 1)
        self.assertTrue(self.eng.get(1,2) == 4)
        self.assertTrue(self.eng.get(2,0) == 4)
        self.assertTrue(self.eng.get(2,1) == 0)
        self.assertTrue(self.eng.get(2,2) == 1)


if __name__ == '__main__':
    unittest.main()
