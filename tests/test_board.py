#coding: utf-8

from os.path import realpath
import sys
sys.path.append(realpath('../bbs'))

import unittest
import board

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        self.b = board.newboard(
            """
            3 3 2 0 1
            2 1 2 3 3
            2 0 4 0 1
            4 1 3 4 2
            0 2 4 4 2
            2 2 4 2 2            
            """)
    
    def testNewBoard(self):
        self.assertEqual(len(self.b), 26)

    def testScoreBoard(self):
        score = board.scoreboard(self.b)
        self.assertEqual(score, 65)
        
    def testTouch(self):
        board.touch(self.b, (3,4))
        #print board.board2str(self.b)
        board.touch(self.b, (4,4))
        board.touch(self.b, (0,2))
        board.touch(self.b, (0,2))
        
        score = board.scoreboard(self.b)
        self.assertEqual(score, 0)
        
    

if __name__ == '__main__':
    unittest.main()