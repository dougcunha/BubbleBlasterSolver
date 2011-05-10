#coding: utf-8

def scoreboard(board):
    """
    >>> s = scoreboard({(0,1): 4, (0,2): 3, (1,2): 5})
    >>> s
    12
    """
    return sum(board.values())

def newboard(self, game):
    ln = 0
    board = {}
    for l in game.splitlines():
        if l.strip() == '': continue
        for cn, c in enumerate(l.split()):
            c = int(c)
            if c:
                board[cn, ln] = c
    return board

def touch(board, pos, y=None):
    """
    >>> b = {(0,0): 4, (0,1): 4, (1,1): 1, (1,2): 4, (2,0): 4, (2,2): 1}
    >>> touch(b, (0,0))
    >>> b
    {(1, 2): 4, (2, 2): 2, (1, 1): 2}
    >>> touch(b, (1,2))
    >>> b
    {(2, 2): 3, (1, 1): 3}
    """
    if y != None: 
        x = pos
    else: 
        x, y = pos
    
    places = [(0, (x, y))]
    
    while places:
        i, place = places.pop()
        
        value = board.get(place, 0)
        if value == 0: 
            continue
        if value < 4: 
            board[place] += 1
            continue
        
        del board[place]
        
        places.extend(find_neighbours(board, place))
        places.sort()

def find_neighbours(board, position):
    """
    >>> b = {(0,0): 3, (0,1): 3, (1,1): 3, (1,2): 4, (2,0): 4, (2,2): 2, (3,1): 2}
    >>> find_neighbours(b, (1,1))
    [(0, (0, 1)), (0, (1, 2)), (1, (3, 1))]
    >>> b = {(0,0): 4, (0,1): 4, (1,1): 1, (1,2): 4, (2,0): 4, (2,2): 1}
    >>> find_neighbours(b, (0,0))
    [(0, (0, 1)), (1, (2, 0))]
    """
    
    col, row = position
    
    max_row = max([r for c, r in board.keys()])
    max_col = max([c for c, r in board.keys()])
    
    places = []
    #up
    for i, newrow in enumerate(range(row-1, -1, -1)):
        place = (col, newrow)
        if board.has_key(place):
            places.append((i,place))
            break

    #right
    for i, newcol in enumerate(range(col+1, max_col+1)):
        place = (newcol, row)
        if board.has_key(place):
            places.append((i,place))
            break

    #bottom
    for i, newrow in enumerate(range(row+1, max_row+1)):
        place = (col, newrow)
        if board.has_key(place):
            places.append((i,place))
            break
    
    #left
    for i, newcol in enumerate(range(col-1, -1, -1)):
        place = (newcol, row)
        if board.has_key(place):
            places.append((i,place))
            break
         
    places.sort()
    return places
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    