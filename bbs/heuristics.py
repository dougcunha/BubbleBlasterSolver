#encoding: utf-8

def sumOfUndropedBubbles(board):
    """
    Calculate value that represents how much longer a board is to be solved.
    Board solved returns 0.
        4 -> 1
        3 -> 2
        2 -> 3
        1 -> 4
        0 -> 0
    >>> s = sumOfUndropedBubbles({(0,1): 4, (0,2): 3, (1,2): 1})
    >>> s
    7
    """
    vl = lambda x: (5-x) %5
    return sum([vl(x) for x in board.values()])