from step import *

class Bubble:
    def __init__(self, position, board):
        self.position = position        
        self.board = board
		
	def dowalk(self, step):
		if board.isPositionValid(self.position):
			self.position += step