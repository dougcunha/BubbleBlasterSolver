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
    def __init__(self, config):
        if isinstance(config, list):
            self.newBoard(config)
        else:
            self.newFromStr(config)
    
    #newFromStr
    def newFromStr(self, str):
        row = 0
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
        return self.newBoard(self.config)

    #newBoard
    def newBoard(self, config):
        '''
            >>> b = Board([[1,2,3,4],[2,3,4,5],[5,4,2,3]])
            >>> b.rows()
            3
            >>> b.cols()
            4
        '''
        self.config = config
        for row in range(0, len(config)):
            for col in range(0, len(config[0])):
                self.board[(row, col)] = BubbleCell(self, [row, col], config[row][col])
    #executeBubbles
    def executeBubbles(self):
        if len(self.bubbles) == 0:
            return True
        for i in range(len(self.bubbles) -1, -1, -1):
            self.bubbles[i].dowalk()
        return self.executeBubbles()
    #get
    def get(self, position):
        if self.isValid(position): return self.board[(position[0], position[1])]
        
    #addbubble
    def addbubbles(self, bubbles):
        for bubble in bubbles:
            self.bubbles.append(bubble)
        
    #removebubble
    def removebubble(self, bubble):
        if bubble in self.bubbles:
            self.bubbles.remove(bubble)
        
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    
