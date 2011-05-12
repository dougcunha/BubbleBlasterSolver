import tabuleiro

class BubbleIterator:
    up = [-1, 0]
    down = 1
    left = 2
    rigth = 3
    #__init__
    def __init__(self, direction, bubble):
        self.direction = direction
        self.bubble = bubble        
        self.position = 0   

    #__iter__
    def __iter__(self):
        return self

    #next
    def next(self):
        self.position += 1
        if self.direction == up:
            self.bubble.row -= 1
        elif self.direction == down:
            self.bubble.row += 1
        elif self.direction == left:
            self.bubble.col -= 1
        else: self.bubble.col += 1
        if not self.bubble.board.celulaEhValida:
            raise StopIteration
        return self.bubble
            
            
        
        
        
