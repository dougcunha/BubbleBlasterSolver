from board import *
from bubblecell import *
from bubble import *
from show import *
import solution
from bubblesolver import *
from step import *
from evaluators import *
from os.path import realpath
import sys
sys.path.append(realpath('../bbs'))
import games

class Ret():
    def __init__(self, func, touchs, score):
        self.touchs = touchs
        self.score = score
        self.func_name = func.func_name
        
    def __repr__(self):
        return "%s - %s => %d" % (self.func_name, str(self.touchs), self.score)

def testSolution():
    maxTouchs = 6
    b = Board(games.game_6_100_m6, maxTouchs)
    maxIters = 2000
    done = False
    solutions = []    
    while maxIters > 0:
        touchs = []
        b.reset()
        temp = []
        f = random.choice(evaluatorsList)
        for i in range(0, maxTouchs):
            touch = solution.getTouch(b.clone(), f)
            if not touch: continue
            touchs.append(touch)
            score = b.touch(touch, False)
            if score == 0: 
                break
                done = True                
        maxIters -= 1
        solutions.append(Ret(f, touchs, score)) 
        if done: break   
           
    best = min(solutions, key=lambda x: x.score)
    worst = max(solutions, key=lambda x: x.score)
    print "Best -> " + str(best)
    print "Worst -> " + str(worst)  
    showSolution(b, best.touchs)

if __name__ == '__main__':
    testSolution()