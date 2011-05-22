# -*- coding: utf-8 -*-
from board import *
import random

def absoluteScore(aboard):
    total = 0
    for key in aboard.board:
        if aboard.get(key).level > 0:
            total += 5 - aboard.get(key).level
    return total