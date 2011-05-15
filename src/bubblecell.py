from board import *
from step import *
from bubble import *

class BubbleCell:
    def __init__(self, board, position, level):
        self.position = position
        self.board = board
        self.level = level
        
    
    def isblasted(self):
        return self.level == 0
        
    def touch(self):
        '''
            >>> board = Board([[1,2,1,4], [2,3,4,3], [3,2,4,1], [1,0,2,3]])
            >>> board.get([0,0]).level
            1
            >>> board.get([1,0]).level
            2
            >>> board.get([2,2]).level
            4
            >>> board.get([2,0]).touch()
            >>> board.get([2,0]).level
            4
        '''
        if self.level == 0: return
        self.level += 1
        if self.level == 5:
            self.level = 0
            self.doBlast()
    
    def doBlast(self):
        bubbles = []
        bubbles.append(Bubble(self.board, self.position, Step.up))
        bubbles.append(Bubble(self.board, self.position, Step.down))
        bubbles.append(Bubble(self.board, self.position, Step.left))
        bubbles.append(Bubble(self.board, self.position, Step.rigth))
        self.board.addbubbles(bubbles)
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()