#coding: utf-8

from pprint import pprint

class BubleEng(object):
    "stores game logic and board info"
    def __init__(self):
        self.tab = {}
        self.explode_state = 4

    def __repr__(self):
        return str(pprint(self.tab))

    def touch(self, x, y):
        coord = (x, y,)

    def newgame(self, game):
        ln = 0
        for l in game.splitlines():
            if l.strip() == '': continue
            for cn, c in enumerate(l.split()):
                c = int(c)
                if c:
                    self.tab[ln, cn] = c
            ln += 1
            
    def get(self, x, y):
        return self.tab.get((x, y), 0)
