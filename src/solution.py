# -*- coding: utf-8 -*-
from board import *
import random

'''
    Classe que representa uma possível solução para
    um jogo de bubble blast
'''
class Solution:
    #__init__    
    def __init__(self, touchs, board):
        self.touchs = touchs
        self.board = board  
        if self.touchs == []:
            self.generateRandomTouchs()
            
    def getPossibleTouchs(self):
        def f(x): return self.board.get(x).level > 0        
        possibletouchs = filter(f, self.board.board)        
        possibletouchsPonderated = []
        
        for i in possibletouchs:
            rg = 1
            if self.board.board.get(i).level == 3:
                rg = 10
            elif self.board.board.get(i).level == 4:
                rg = 50               
            for y in range(0, rg):
                possibletouchsPonderated.append(i)
        return possibletouchsPonderated   
        
    def generateRandomTouchs(self):
        self.touchs = []
        
        possibles = self.getPossibleTouchs()                        
             
        for i in range(0, self.board.max):
            count = 0
            while count < 50:
                touch = random.choice(possibles)
                if not self.board.get(touch).isblasted(): break
            self.touchs.append(touch)
    #tamanho    
    def __len__(self):
        return len(self.touchs)
    
    #score
    def score(self):
        for touch in self.touchs:
            if self.board.isValid(touch):
                self.board.get(touch).touch()
            self.board.executeBubbles()
        pt = self.board.score()
        self.board.reset()            
        return pt
        
    #obterToques
    def getTouchs(self, start, size):
        '''
            >>> ind = Solution([[0,0], [1,2], [1,3], [0,1]], Board([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
            >>> ind.getTouchs(2, 2)
            [[1, 3], [0, 1]]
        '''
        result = []        
        x = 0
        for i in range(start, start + size):
            if i > self.__len__() - 1: break
            result.append(self.touchs[i])
            x += 1
        return result
        
    #cruzar
    def doCross(self, another):
        '''
             >>> ind1 = Solution([[0,0], [1,2], [1,3], [0,1]], Board([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
             >>> ind2 = Solution([[3,1], [0,3], [3,2], [4,5]], Board([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
             >>> filho1 = ind1.doCross(ind2)
             >>> filho1.touchs
             [[0, 0], [1, 2], [3, 2], [4, 5]]
             >>> filho2 = ind2.doCross(ind1)
             >>> filho2.touchs
             [[3, 1], [0, 3], [1, 3], [0, 1]]
			 >>> ind1 = Solution([[0,0], [1,2], [1,3], [0,1], [2,4]], Board([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
             >>> ind2 = Solution([[3,1], [0,3], [3,2], [4,5], [1,0]], Board([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
			 >>> filho = ind1.doCross(ind2)
			 >>> filho.touchs
			 [[0, 0], [1, 2], [3, 2], [4, 5], [1, 0]]
			 >>> ind1 = Solution([[0,0], [1,2], [1,3]], Board([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
             >>> ind2 = Solution([[3,1], [0,3], [3,2]], Board([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
             >>> filho = ind1.doCross(ind2)
             >>> filho.touchs
             [[0, 0], [0, 3], [3, 2]]
        '''
        part = self.__len__() / 2        
        return Solution(self.getTouchs(0, part) + \
                         another.getTouchs(part, another.__len__()),
                         self.board)
    #mutar
    def doMutation(self, genes = 1):
        '''
            >>> ind = Solution([[0,0], [1,2], [1,3], [0,1]], Board([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))
            >>> mutante = ind.doMutation(2)
            >>> mutante.touchs[0] != [0, 0]
            True
        '''   
        possibles = self.getPossibleTouchs()
        gene = []
        for i in range(0, genes):
            gene.append(random.choice(possibles))
                
        return Solution(gene + self.getTouchs(genes, self.__len__()),
                         self.board)
        
    def __repr__(self):
        return str(self.touchs)
        
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
