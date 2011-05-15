# -*- coding: latin1 -*-
from board import *
from step import *

class Bubble():
    def __init__(self, board, position, step):
        self.position = position        
        self.board = board
        self.step = step
        
    def dowalk(self):
        '''
            >>> t = Board([[1,1,2],[2,3,4]])
            >>> b = Bubble(t, [0,0], Step.down)
            >>> b.dowalk()
            >>> t.executeBubbles()
            True
            >>> b.position
            [1, 0]
            >>> t.get(b.position).level
            3
            >>> t = Board([[1,2,1,3,4],[0,3,4,2,3],[4,3,4,2,3],[3,4,3,2,1],[2,3,4,3,4],[2,3,4,3,4]])
            >>> t.get([0,0]).touch(4)
            >>> len(t.bubbles)
            4
            >>> t.bubbles[0].position
            [0, 0]
            >>> t.bubbles[0].step
            [-1, 0]
            >>> t.executeBubbles()
            True
            >>> len(t.bubbles)
            0
            >>> t.get([0,0]).level
            0
            >>> t.get([1,0]).level
            0
            >>> t.get([2,0]).level
            0
            >>> t.get([0,1]).level
            3
            >>> t.get([2,0]).touch()
            >>> t.executeBubbles()
            True
            >>> t.get([2,0]).level
            0
            >>> t.get([2,1]).level
            4
            >>> t.get([3,0]).level
            4
        '''
        if not self.validate(): return
        self.position[0] += self.step[0]
        self.position[1] += self.step[1]
        if not self.validate(): return
        if not self.board.get(self.position).isblasted():
            self.board.get(self.position).touch()
            self.removeyourself()
    
    def validate(self):
        if not self.isValid():
            self.removeyourself()
            return False
        return True
        
    def col(self):
        '''
            >>> b = Bubble(Board([[1,1,2],[2,3,4]]), [1,1], Step.down)
            >>> b.col()
            1
        '''
        return self.position[1]
        
    def row(self):
        '''
            >>> b = Bubble(Board([[1,2,3,4],[2,3,4,5],[5,4,2,3]]), [0,1], Step.left)
            >>> b.row()
            0
        '''
        return self.position[0]
    
    def removeyourself(self):
        self.board.removebubble(self)
        
    def isValid(self):
        return self.board.isValid(self.position)
        
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
