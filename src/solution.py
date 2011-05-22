# -*- coding: utf-8 -*-
from board import *
import random
from evaluators import *

class ScoredTouch():
    def __init__(self, touch, score):
        self.touch = touch
        self.score = score
    def __repr__(self):
        return "%s->%d" % (str(self.touch), self.score)

def getPossibleTouchs(aboard):
    cells = filter(lambda x: x.level > 0, [aboard.board.get(t) for t in [a for a in aboard.board]])    
    touchs = [touch.position for touch in cells]
    return touchs

def getScores(aboard, touchs, f):
    scores = [f(aboard, touch) for touch in touchs]
    return scores     

def getTouch(aboard, f):
    touchs = getPossibleTouchs(aboard)
    scored = [ScoredTouch(t, f(aboard, t)) for t in touchs]            
    biggest = max(scored, key=lambda x: x.score)
    biggests = filter(lambda x: x.score == biggest.score, scored) 
    return biggests[0].touch if len(biggests) == 1 else \
        biggests[random.choice(range(0, len(biggests)))].touch

