from board import *
from bubble import *
from bubblecell import *
import unittest

class TestTouch(unittest.TestCase):        
    def testTouch4(self):
        self.maxDiff = None
        tab = Board('''
        3 3 3 3 
        4 4 4 4 
        3 3 3 3 
        ''')
        tab.touch([1,1])        
        self.assertEqual(str(tab), str(Board('''
        4 4 4 4 
        0 0 0 0 
        4 4 4 4         
        ''')))
        
    def testTouch5(self):
        self.maxDiff = None
        tab = Board('''
         3 3 3
         3 4 3 
         4 4 4 
         3 4 3
         3 3 3 
        ''')
        tab.touch([2,1])        
        self.assertEqual(str(tab), str(Board('''
         0 0 0 
         0 0 0 
         0 0 0 
         0 0 0
         0 0 0      
        ''')))
        
        
    def testTouch6(self):
        self.maxDiff = None
        tab = Board('''
         3 1 3
         3 4 3 
         4 4 4 
         3 4 3
         3 1 3 
        ''')
        tab.touch([2,1])        
        self.assertEqual(str(tab), str(Board('''
         0 0 0 
         0 0 0 
         0 0 0 
         0 0 0
         0 0 0      
        ''')))
        
        
    def testTouch7(self):
        self.maxDiff = None
        tab = Board('''
         1 1 1
         3 4 3 
         4 4 4 
         3 4 3
         3 1 3 
        ''')
        tab.touch([2,1])        
        self.assertEqual(str(tab), str(Board('''
         4 4 4 
         0 0 0 
         0 0 0 
         0 0 0
         0 0 0      
        ''')))
        
    def testTouch8(self):
        #2 30
        self.maxDiff = None
        tab = Board('''
        0 2 2 1 3
        1 1 4 1 4
        4 4 4 2 2
        4 0 4 2 1
        4 2 3 3 2
        2 3 4 0 2
        ''')
        tab.touch([2,2])        
        self.assertEqual(str(tab), str(Board('''
        0 4 0 3 4
        0 0 0 0 0
        0 0 0 0 4
        0 0 0 0 2
        0 0 0 0 4
        0 0 0 0 0
        ''')))
        
        
    def testTouch9(self):
        #4 66
        self.maxDiff = None
        tab = Board('''
        2 3 1 0 2
        1 0 3 2 3
        3 4 4 3 3
        2 4 4 1 3
        1 4 4 1 1
        4 4 4 2 3 
        ''')
        tab.touch([5,0])        
        self.assertEqual(str(tab), str(Board('''
        3 4 2 0 3
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 0
        0 0 0 0 4
        0 0 0 4 3
        ''')))
        
if __name__ == '__main__':
    unittest.main()
        
