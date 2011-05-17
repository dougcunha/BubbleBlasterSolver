#coding: utf-8

def scoreboard(board):
    """
    >>> s = scoreboard({(0,1): 4, (0,2): 3, (1,2): 5})
    >>> s
    12
    """
    return sum(board.values())

def newboard(game):
    row = 0
    board = {}
    for line in game.splitlines():
        if line.strip() == '': continue
        for col, value in enumerate(line.split()):
            value = int(value)
            if value:
                board[row, col] = value
        row += 1
    return board

def board2str(board):
    """
    >>> b = {(0,0): 4, (0,1): 4, (1,1): 1, (1,2): 4, (2,0): 4, (2,2): 1}
    >>> print board2str(b)
    4 4 0
    0 1 4
    4 0 1
    """
    max_row, max_col = board_dimensions(board)
    r = []
    for row in xrange(max_row+1):
        for col in xrange(max_col+1):
            r.append(str(board.get((row, col), 0)))
        r.append('\n')
    return ' '.join(r).replace(' \n ', '\n').replace(' \n', '')
    

def touch(board, pos, col=None):
    """
    >>> b = {(0,0): 4, (0,1): 4, (1,1): 1, (1,2): 4, (2,0): 4, (2,2): 1}
    >>> touch(b, (0,0))
    >>> b
    {(1, 2): 4, (2, 2): 2, (1, 1): 2}
    >>> touch(b, (1,2))
    >>> b
    {(2, 2): 3, (1, 1): 3}
    """
    if col != None: 
        row = pos
    else: 
        row, col = pos
    
    places = [(0, (row, col))]
    
    while places:
        i, place = places.pop()
        
        value = board.get(place, 0)
        if value == 0: 
            continue
        if value < 4: 
            board[place] += 1
            #print place, 'increased to %d' % (board.get(place))
            continue
        
        del board[place]
        #print place, 'exploded'
        
        places.extend(find_neighbours(board, place))
        places.sort()
        
def board_dimensions(board):
    max_row = max([r for r, c in board.keys()])
    max_col = max([c for r, c in board.keys()])
    return max_row, max_col

def find_neighbours(board, position):
    """
    >>> b = {(0,0): 3, (0,1): 3, (1,1): 3, (1,2): 4, (2,0): 4, (2,2): 2, (3,1): 2}
    >>> find_neighbours(b, (1,1))
    [(0, (0, 1)), (0, (1, 2)), (1, (3, 1))]
    >>> b = {(0,0): 4, (0,1): 4, (1,1): 1, (1,2): 4, (2,0): 4, (2,2): 1}
    >>> find_neighbours(b, (0,0))
    [(0, (0, 1)), (1, (2, 0))]
    """
    
    row, col = position
    max_row, max_col = board_dimensions(board)
    
    places = []
    #up
    for i, newrow in enumerate(range(row-1, -1, -1)):
        place = (newrow, col)
        if board.has_key(place):
            places.append((i,place))
            break

    #right
    for i, newcol in enumerate(range(col+1, max_col+1)):
        place = (row, newcol)
        if board.has_key(place):
            places.append((i,place))
            break

    #bottom
    for i, newrow in enumerate(range(row+1, max_row+1)):
        place = (newrow, col)
        if board.has_key(place):
            places.append((i,place))
            break
    
    #left
    for i, newcol in enumerate(range(col-1, -1, -1)):
        place = (row, newcol)
        if board.has_key(place):
            places.append((i,place))
            break
         
    places.sort()
    return places
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    