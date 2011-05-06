# -*- coding: latin1 -*-
'''
    Classe que representa um tabuleiro de um tabuleiro de 
    Blubble Blast
'''
import numpy

class Tabuleiro:
    celulas = {}
    def __init__(self):
       pass
    
    def tocar(self, linha, coluna):
        self.celulas[linha, coluna] += 1
        self.percorrer()

    def iniciar(self, matriz):
        self.celulas = matriz

    def percorrer(self):
        pass

if __name__ == '__main__':
    tab = Tabuleiro()
    tab.iniciar({(1,1):1, (2,3): 3})
    print tab.celulas
    print tab.celulas[1,1]
    tab.tocar(1, 1)
    print tab.celulas[1,1]
	
