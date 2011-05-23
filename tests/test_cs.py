#coding: utf-8

from os.path import realpath
import sys
sys.path.append(realpath('../bbs'))

import board

import unittest
import cs

from games import *


class TestCompleteSearch(unittest.TestCase):


    def setUp(self):
        self.b = board.newboard(game_1_90_m4)

    def testCS(self):
        root = cs.Node(self.b.copy(), max_depth=4)
        root.eval()
        root.display()
        root.display_solutions() 


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()