# -*- coding: utf-8 -*-
from board import *
from scores import *
import random

maxValue = 100
minValue = 0

def randomEvaluator(aboard, touch):
    return random.randrange(0, 100)

def semiRandomEvaluator(aboard, touch):
    if touch[0] % 2: return randomEvaluator(aboard, touch)
    else:
        return absoluteEvaluator(aboard, touch)

def absoluteEvaluator(aboard, touch):
    return (aboard.get(touch).level * 25)

def absoluteScoreEvaluator(aboard, touch):
    aboard.touch(touch, False)
    pt = absoluteScore(aboard)
    aboard.reset()
    return 120 / pt if pt else 120

def alternativeAbsRandomEvaluate(aboard, touch):
    dado = random.randint(0, 30)
    if dado in range(0, 10) : return randomEvaluator(aboard, touch)
    elif dado in range(10, 20): return absoluteEvaluator(aboard, touch)
    else:
        return absoluteScoreEvaluator(aboard, touch)
    
def inverseEvaluator(aboard, touch):
    return ((5 - aboard.get(touch).level) * 25)

def exoticEvaluator(aboard, touch):
    return touch[0] * touch[1] * 10

def wtfEvaluator(aboard, touch):
    return sum([(5 - aboard.get(x).level) for x in aboard.board])

def insaneEvaluator(aboard, touch):
    return sum([aboard.get(x).level for x in aboard.board if aboard.get(x).level == aboard.get(touch).level])


evaluatorsList = [randomEvaluator, semiRandomEvaluator, absoluteEvaluator,
                  absoluteScoreEvaluator, alternativeAbsRandomEvaluate,
                  exoticEvaluator, wtfEvaluator, insaneEvaluator]


def avgEvaluators(aboard, touch):
    sum = 0
    for f in evaluatorsList:
        sum += f(aboard, touch)
    return sum / len(evaluatorsList)