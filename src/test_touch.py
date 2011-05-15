from board import *
from bubble import *
from bubblecell import *
import unittest

class TestTouch(unittest.TestCase):
    def setUp(self):        
        self.tab = Board('''
        1 2 1 3 4
        0 3 4 2 3
        4 3 4 2 3
        3 4 3 2 1
        2 3 4 3 4
        2 3 4 3 4
        ''')

    def testTouch(self):
        self.assertEqual(self.tab.rows(), 6)
        self.assertEqual(self.tab.cols(), 5)
        self.tab.get([0,0]).touch()
        self.tab.executeBubbles()
        self.assertEqual(self.tab.get([0,0]).level, 2)
        self.tab.get([0,0]).touch()
        self.tab.executeBubbles()
        self.assertEqual(self.tab.get([0,0]).level, 3)
        self.tab.get([0,0]).touch()
        self.tab.executeBubbles()
        self.assertEqual(self.tab.get([0,0]).level, 4)
        self.tab.get([0,0]).touch()
        self.tab.executeBubbles()
        self.assertEqual(self.tab.get([0,0]).level, 0)
        self.assertEqual(self.tab.get([0,1]).level, 3)
        self.assertEqual(self.tab.get([1,0]).level, 0)
        self.assertEqual(self.tab.get([2,0]).level, 0)
        self.assertEqual(self.tab.get([3,0]).level, 4)

if __name__ == '__main__':
    unittest.main()
        
