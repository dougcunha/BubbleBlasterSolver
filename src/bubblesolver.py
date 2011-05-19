# -*- coding: utf-8 -*-
from board import *
from solution import *
import random
'''
  
'''
class Procriator:
    def __init__(self, board, size=10, mutationgenes = 1):
        self.board = board
        self.size = size
        self.mutationgenes = mutationgenes
        
    def check(self):
        solution = filter(lambda i: i.score() == 0, self.generation)
        return solution
    
    def getCompetitors(self):
        competition = []
        c1 = random.choice(self.tournaments)
        competition.append(c1)
        c2 = random.choice(self.tournaments)
        competition.append(c2)
        c3 = random.choice(self.tournaments)
        competition.append(c3)
        return competition
    
    def naturalSelection(self):
        self.tournaments = self.generation
        selecteds = []
        childs = []
        for i in range(0, self.size / 2):
            winner = self.getBest(self.getCompetitors())
            selecteds.append(winner)
            self.tournaments.remove(winner)
            
        selecteds.sort(key=lambda c: c.score(), reverse=True)
            
        for i in range(0, len(selecteds) - 2, 2):
            childs.append(selecteds[i].doCross(selecteds[i+1]))
            
        childs.append(selecteds[-1].doMutation(self.mutationgenes))
        childs.append(selecteds[-2].doMutation(self.mutationgenes))
        
        self.generation = selecteds + childs
            
    def createGeneration(self):
        self.generation = []        
        for i in range(0, self.size):
            self.generation.append(Solution(self.board))            
        
    def getBest(self, competitors):
        competitors.sort(key=lambda c: c.score(), reverse=True)
        return competitors[0]
        
        
    
            
