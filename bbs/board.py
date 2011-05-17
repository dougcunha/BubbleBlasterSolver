#coding: utf-8

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
    
    places = [iter([(row, col)])]
    placesiter = get_dropsiter(places)
    
    for place in placesiter:
        
        value = board.get(place, 0)
        if value == 0: 
            continue
        
        #notifies that this drop found something
        placesiter.send(1)
        
        if value < 4: 
            board[place] += 1
            #print place, 'increased to %d' % (board.get(place))
            continue
        
        del board[place]
        #print place, 'exploded'
        
        places.extend(get_drops(board, place))
        
def board_dimensions(board):
    if len(board) == 0: 
        return (0,0)
    max_row = max([r for r, _ in board.keys()])
    max_col = max([c for _, c in board.keys()])
    return max_row, max_col

def get_drops(board, position):
    """Returns a list of generated drops vectors."""
    row, col = position
    max_row, max_col = board_dimensions(board)
    
    drops = []
    
    drops.append(((newrow, col) for newrow in xrange(row-1, -1, -1))) #up
    drops.append(((row, newcol) for newcol in xrange(col+1, max_col+1))) #right
    drops.append(((newrow, col) for newrow in xrange(row+1, max_row+1))) #bottom
    drops.append(((row, newcol) for newcol in xrange(col-1, -1, -1))) #left
    
    return drops

def get_dropsiter(drops):
    """Iterates over a list of generated drops vectors.
    Call iter.send(1) to notify that the last drop vector bumped
    >>> b1 = ((x, 1) for x in xrange(0, 3))
    >>> b2 = ((6, x) for x in xrange(10, 14))
    >>> biter = get_dropsiter([b1, b2])
    >>> list(biter)
    [(0, 1), (6, 10), (1, 1), (6, 11), (2, 1), (6, 12), (6, 13)]
    """
    while drops:
        i = 0
        while i < len(drops):
            drop = drops[i]
            try:
                place = drop.next()
                found = (yield place)
                if found == 1:
                    drops.remove(drop)
                    (yield place)
                    continue
                
                i += 1                                   
            except StopIteration:
                drops.remove(drop)
                

def find_neighbours(board, position):
    """
    >>> b = {(0,0): 3, (0,1): 3, (1,1): 3, (1,2): 4, (2,0): 4, (2,2): 2, (3,1): 2}
    >>> find_neighbours(b, (1,1))
    [(0, 1), (1, 2), (3, 1)]
    >>> b = {(0,0): 4, (0,1): 4, (1,1): 1, (1,2): 4, (2,0): 4, (2,2): 1}
    >>> find_neighbours(b, (0,0))
    [(0, 1), (2, 0)]
    """
    
    drops = get_drops(board, position)
    places = []
    dropsi = get_dropsiter(drops)
    for place in dropsi:   
        if board.has_key(place):
            places.append(place)
            dropsi.send(1)
    
    return places

        
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
