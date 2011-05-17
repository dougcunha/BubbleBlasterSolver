# -*- coding: latin1 -*-
'''
    Classe que representa um tabuleiro de 
    Blubble Blast
'''
from bubblecell import *
from bubble import *
from step import *

class Board:
    config = []
    board = {}
    bubbles = []
    #__init__
    def __init__(self, config, maxTouchs = 5):
        if isinstance(config, list):
            self.newBoard(config)
        else:
            self.newFromStr(config)
        self.max = maxTouchs
    
    #reset
    def reset(self):
        self.newBoard(self.config)
        
    #newFromStr
    def newFromStr(self, str, maxTouchs = 5):
        row = 0
        self.max = maxTouchs
        self.config = []
        self.board = {}
        self.bubbles = []
        for line in str.splitlines():
            if line.strip() == '': continue
            l = []
            for col, value in enumerate(line.split()):
                value = int(value)
                l.append(value)
            row += 1
            self.config.append(l)
        return self.newBoard(self.config, maxTouchs)

    #newBoard
    def newBoard(self, config, maxTouchs = 5):
        '''
            >>> b = Board([[1,2,3,4],[2,3,4,5],[5,4,2,3]])
            >>> b.rows()
            3
            >>> b.cols()
            4
            >>> str(b)
            '2-4-1-4-3-5-5-3-2-2-4-3'
        '''
        self.config = config
        self.max = maxTouchs
        self.board = {}
        self.bubbles = []
        for row in range(0, len(self.config)):
            for col in range(0, len(self.config[0])):
                self.board[(row, col)] = BubbleCell(self, [row, col], self.config[row][col])
    
    #executeBubbles
    def executeBubbles(self):
        if len(self.bubbles) == 0:
            return True
        lista = range(len(self.bubbles) -1, -1, -1)
        for i in lista:
            if self.bubbles[i].active:
                self.bubbles[i].dowalk()
        for i in lista:
            if not self.bubbles[i].active: 
                self.bubbles.remove(self.bubbles[i])
        return self.executeBubbles()
    
    #get
    def get(self, position):
        if self.isValid(position): return self.board[(position[0], position[1])]
    
    def score(self):
        '''
           >>> a = Board([[1,2,3],[4,4,4],[0,2,2],[0,1,2]])
           >>> a.score()
           25
           >>> a = Board([[0,0,0],[4,4,4],[1,1,1],[2,2,2]])
           >>> a.score()
           24
        '''
        total = 0
        for key in self.board:
            if self.get(key).level > 0:
                total += 5 - self.get(key).level
        return total        
    
    #addbubble
    def addbubbles(self, bubbles):
        for bubble in bubbles:
            self.bubbles.append(bubble)
    
    #isegual(self, config)
    def isequal(self, config):
        '''
           >>> a = Board([[1,2,3],[4,5,6],[7,8,9],[0,1,2]])
           >>> a.isequal([[1,2,3],[4,5,6],[7,8,9],[0,1,2]])
           True
           >>> a.isequal([[1,0,3],[4,5,6],[7,8,9],[0,1,2]])
           False
           >>> str(a)
           '2-6-2-1-0-1-8-5-7-9-4-3'
        '''
        b = Board(config)
        return self.rows() == b.rows() and self.cols() == b.cols() and str(b) == str(self)
    #isValid
    def isValid(self, position):
        '''
            >>> b = Board([[1,2,3,4],[2,3,4,5],[5,4,2,3]])
            >>> b.isValid([0,1])
            True
            >>> b.isValid([3, 0])
            False
            >>> b.isValid([0,3])
            True
            >>> b.isValid([0,4])
            False
            >>> b.isValid([2,2])
            True
            >>> b.isValid([-1,0])
            False
            >>> b.isValid([0,-1])
            False
        '''
        return self.board.has_key((position[0], position[1]))
        
    #linhas
    def rows(self):
        return len(self.config)
        
    #colunas
    def cols(self):
        if self.rows() == 0: return 0
        return len(self.config[0])
    
    def __repr__(self):
        return "-".join([str(self.board[c].level) for c in self.board])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    
