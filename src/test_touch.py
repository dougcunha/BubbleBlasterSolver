from board import *
from bubble import *
from bubblecell import *
import unittest

class TestTouch(unittest.TestCase):
    def setUp(self):        
        self.tab = \
        Board('''
        1 2 1 3 4
        0 3 4 2 3
        4 3 4 2 3
        3 4 3 2 1
        2 3 4 3 4
        2 3 4 3 4
        ''')
        self.config1 = \
        '''
        2 2 1 3 4
        0 3 4 2 3
        4 3 4 2 3
        3 4 3 2 1
        2 3 4 3 4
        2 3 4 3 4
        '''
        self.config2 = \
        '''
        0 3 1 3 4
        0 3 4 2 3
        0 4 4 2 3
        4 4 3 2 1
        2 3 4 3 4
        2 3 4 3 4
        '''
        self.config3 = \
        '''
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        '''
        
        self.config4 = \
        '''
        1 2 4 1 3
        0 1 3 4 3
        0 4 0 4 2
        1 0 4 4 4
        2 3 2 3 4
        2 1 1 0 2
        '''
        
        self.config5 = \
        '''
        2 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        4 0 0 0 0
        3 0 0 0 0
        4 0 0 0 0
        '''
        
        self.config6 = \
        '''
        2 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        3 0 0 0 0
        3 0 0 0 0
        3 4 4 0 0
        '''

    def testTouch(self):
        self.assertEqual(self.tab.rows(), 6)
        self.assertEqual(self.tab.cols(), 5)
        self.tab.get([0,0]).touch()
        self.tab.executeBubbles()
        self.assertTrue(self.tab.isequal(self.config1))
        self.tab.get([0,0]).touch()
        self.tab.executeBubbles()
        self.assertEqual(self.tab.get([0,0]).level, 3)
        self.tab.get([0,0]).touch()
        self.tab.executeBubbles()
        self.assertEqual(self.tab.get([0,0]).level, 4)
        self.tab.get([0,0]).touch()
        self.tab.executeBubbles()
        self.assertEqual(str(self.tab), str(Board(self.config2)))
        self.tab.get([2,2]).touch()
        self.tab.executeBubbles()
        self.assertEqual(str(self.tab), str(Board(self.config3)))
        
    def testTouc2(self):
        tab = Board(self.config4)
        tab.get([3, 2]).touch()
        tab.executeBubbles()
        self.assertEqual(str(tab), str(Board(self.config5)))
        
    def testTouch3(self):
        tab = Board(self.config4)
        tab.get([2, 1]).touch()
        tab.executeBubbles()
        self.assertEqual(str(tab), str(Board(self.config6)))
        
if __name__ == '__main__':
    unittest.main()
        
