# -*- coding: latin1 -*-
'''
    Classe que representa um tabuleiro de um tabuleiro de 
    Blubble Blast
'''
import celula

class Tabuleiro:
    celulas = []
    def __init__(self):
        self.celulas = [[Celula(0),Celula(0),Celula(0),Celula(0),Celula(0)]
                        [Celula(0),Celula(0),Celula(0),Celula(0),Celula(0)]
                        [Celula(0),Celula(0),Celula(0),Celula(0),Celula(0)]
                        [Celula(0),Celula(0),Celula(0),Celula(0),Celula(0)]
                        [Celula(0),Celula(0),Celula(0),Celula(0),Celula(0)]
                        [Celula(0),Celula(0),Celula(0),Celula(0),Celula(0)]]
	
