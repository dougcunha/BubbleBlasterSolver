from board import *
from bubblecell import *
from bubble import *
from solution import *
from bubblesolver import *
from step import *

class TestBubbleSolver():
    def __init__(self):
        #pct 2 - 2 toques 3
        #self.board = Board('''
        #1 2 4 1 3
        #0 1 3 4 3
        #0 4 0 4 2
        #1 0 4 4 4
        #2 3 2 3 4
        #3 1 1 0 2
        #''', 3)
        self.board = Board('''
        0 2 2 0 1
        1 4 0 0 1
        1 4 3 2 2
        0 1 2 2 2
        2 4 4 4 0
        2 2 3 2 0
        ''', 7)
        
    def testSoluction(self):
        proc = Procriator(self.board, 100, 2)
        proc.createGeneration()
        max = 100
        winner = proc.check()
        while not winner and max > 0:
            proc.naturalSelection()
            #for x in proc.generation:
            #    print x, " -> ", x.score() 
            winner = proc.check()
            if winner: break
            max -=1
            
        if max > 0:
            print "There is a solution: %s" % (winner)
        else:
            for x in proc.generation:
                print x , " -> ", x.score()
        
        



if __name__ == '__main__':
    t = TestBubbleSolver()
    t.testSoluction()