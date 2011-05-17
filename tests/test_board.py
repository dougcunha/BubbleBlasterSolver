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
        
    def _testTouch(self):
        board.touch(self.b, (3,4))
        #print board.board2str(self.b)
        board.touch(self.b, (4,4))
        board.touch(self.b, (0,2))
        board.touch(self.b, (0,2))
        
        score = board.scoreboard(self.b)
        self.assertEqual(score, 0)
        
class TestBoardStateAfterTouchs(unittest.TestCase):
    
    def setUp(self):
        self.b = board.newboard(
            """
            4 2 2 2 1
            0 4 1 3 4
            0 4 0 3 4
            2 0 0 1 4
            3 4 0 4 2
            1 1 0 4 1
            """)
        
    def testTouchOn00(self):
        board.touch(self.b, (0,0))
        b2 = board.newboard(
            """
            0 3 2 2 1
            0 4 1 3 4
            0 4 0 3 4
            3 0 0 1 4
            3 4 0 4 2
            1 1 0 4 1
            """)
        self.assertEquals(self.b, b2)
        
    def testTouchOn01(self):
        board.touch(self.b, (0,1))
        b2 = board.newboard(
            """
            4 3 2 2 1
            0 4 1 3 4
            0 4 0 3 4
            2 0 0 1 4
            3 4 0 4 2
            1 1 0 4 1
            """)
        self.assertEquals(self.b, b2)
        
        board.touch(self.b, (0,1))
        b2 = board.newboard(
            """
            4 4 2 2 1
            0 4 1 3 4
            0 4 0 3 4
            2 0 0 1 4
            3 4 0 4 2
            1 1 0 4 1
            """)
        self.assertEquals(self.b, b2)
        
        board.touch(self.b, (0,1))
        b2 = board.newboard(
            """
            0 0 4 2 1
            0 0 2 3 4
            0 0 0 4 4
            4 0 0 3 4
            0 0 0 0 4
            2 3 0 0 2
            """)
        self.assertEquals(self.b, b2)
        
        board.touch(self.b, (2,3))
        b2 = board.newboard(
            """
            0 0 4 4 4
            0 0 3 0 0
            0 0 0 0 0
            0 0 0 0 0
            0 0 0 0 0
            3 3 0 0 4
            """)
        self.assertEquals(self.b, b2)

if __name__ == '__main__':
    unittest.main()