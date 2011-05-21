#coding: utf-8
"""
Complete search solution for the Buble Blast Puzzle
"""

import board
from heuristics import sumOfUndropedBubbles

class Node(object):
    def __init__(self, b, spot=None, parent=None, max_depth=5):
        self.parent = parent
        self.root = (self.parent == None)
        self.b = b
        self.spot = spot
        self.children = []
        self.score = sumOfUndropedBubbles(b)
        self.solved = (self.score == 0)
        self.depth = 0
        self.max_depth = max_depth
        if self.parent:
            self.depth = self.parent.depth + 1
            self.max_depth = self.parent.max_depth
        self.aborted = (self.depth >= self.max_depth)
        self.solutions = []
            
    def __str__(self):
        return '[%s: %d%s%s]' % (
                                 str(self.spot), 
                                 self.score, 
                                 's' if self.solved else '', 
                                 'a' if self.aborted else '', )
        
    def eval(self):
        if self.solved:
            self._solution_found()
            return
        
        if self.aborted:
            return
        
        for spot in self.b.keys():
            bcp = self.b.copy()
            board.touch(bcp, spot)
            child = Node(bcp, spot, self)
            self.children.append(child)
        
        map(lambda x: x.eval(), self.children)
            
            
    def _solution_found(self, nodes=None):
        if nodes == None:
            nodes = []
            
        if self.root:
            points = sum([node.score for node in nodes])
            self.solutions.append(((len(nodes), points),(nodes),))
            self.solutions.sort()
        else:
            nodes.insert(0, self)
            self.parent._solution_found(nodes)
            
    def display(self):
        identPattern = "|  "
        ident = identPattern * self.depth
        my = ident + self.__str__()
        print my
        for child in self.children:
            child.display()
            
    def display_solutions(self):
        for (size, points), solution in self.solutions:
            print 'Solution in %d steps, scores %d:' % (size, points), ''.join([str(node) for node in solution])

    
        