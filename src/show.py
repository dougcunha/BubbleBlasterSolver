from board import *

def showTouch(aboard, touch):
    config = ''
    for row in range(0, len(aboard.config)):
        for col in range(0, len(aboard.config[0])):
            if touch == [row, col]:
                config += 'X '
            else:
                config += str(aboard.get([row, col]).level) + ' '
        config += '\n'
    print config            

def showSolution(aboard, touchs):
    aboard.reset()
    print str(aboard)
    for touch in touchs:
        showTouch(aboard, touch)
        aboard.touch(touch, False)
        print(str(aboard))
        
        
        
        