from board import *
from bubblecell import *
from bubble import *
from solution import *
from bubblesolver import *
from step import *

class TestBubbleSolver():
    def __init__(self):
        #pct 2 - 2 toques 3
        self.board = Board('''
        1 2 4 1 3
        0 1 3 4 3
        0 4 0 4 2
        1 0 4 4 4
        2 3 2 3 4
        3 1 1 0 2
        ''', 3)
        
    def testSoluction(self):
        proc = Procriator(self.board, 10, 3)
        proc.createGeneration()
        max = 5000
        winner = proc.check()
        while not winner and max > 0:
            proc.naturalSelection()
            winner = proc.check()
            if winner: break
            max -=1
            
        if max > 0:
            print "There is a solution: %s" % (winner)
        else:
            for x in proc.generation:
                print x
        
        



if __name__ == '__main__':
    t = TestBubbleSolver()
    t.testSoluction()