# -*- coding: latin1 -*-
'''
    Classe que representa um tabuleiro de 
    Blubble Blast
'''
import numpy
from bubble import *

class Tabuleiro:
    tabuleiro = []
    #__init__
    def __init__(self):
       pass

    #bubble
    def bubble(self, linha, coluna):
        '''
            >>> tab = Tabuleiro()
            >>> tab.iniciar([[1,2,1,3,4],[0,3,4,2,3],[4,3,4,2,3],[3,4,3,2,1],[2,3,4,3,4],[2,3,4,3,4]])
            >>> tab.bubble(1,1).row
            1
            >>> tab.bubble(1,1).col
            1
        '''
        return Bubble(linha, coluna, self)
    
    #resolvido
    def resolvido(self):
        '''
           >>> tab = Tabuleiro()
           >>> tab.iniciar([[1,2,1,3,4],[0,3,4,2,3],[4,3,4,2,3],[3,4,3,2,1],[2,3,4,3,4],[2,3,4,3,4]])
           >>> tab.resolvido()
           False
           >>> tab.iniciar([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
           >>> tab.resolvido()
           True
        '''
        for linha in range(0, self.linhas() - 1):
            for coluna in range(0, self.colunas() - 1):
                if self.celula(linha, coluna) != 0:
                    return False
        return True
        
    #celulaEhVazia
    def celulaEhVazia(self, linha, coluna):
        return self.celula(linha, coluna) == 0;
    
    #novo
    def novo(self, configuracao):
        for linha in configuracao.splitlines():
            if linha.strip() == '': continue
            for coluna, valor in enumerate(linha.split()):
                valor = int(valor)
                if valor:
                    self.tabuleiro[linha][coluna] = c
            linha += 1

    
    #tocar
    def tocar(self, linha, coluna):
        '''
            >>> tab = Tabuleiro()
            >>> tab.iniciar([[1,2,1,3,4],[0,3,4,2,3],[4,3,4,2,3],[3,4,3,2,1],[2,3,4,3,4],[2,3,4,3,4]])
            >>> tab.tocar(0, 0)
            >>> tab.celula(0, 0)
            2
            >>> tab.tocar(0, 0)
            >>> tab.celula(0, 0)
            3
            >>> tab.tocar(1, 2)
            >>> tab.celula(1, 2)
            0
        '''
        if not self.celulaEhValida(linha, coluna): return
        self.tabuleiro[linha][coluna] += 1
        self.percorrer()

    #celulaEhValida
    def celulaEhValida(self, linha, coluna):
        '''
            >>> tab = Tabuleiro()
            >>> tab.iniciar([[1,2,1,3,4],[0,3,4,2,3],[4,3,4,2,3],[3,4,3,2,1],[2,3,4,3,4],[2,3,4,3,4]])
            >>> tab.celulaEhValida(0, 0)
            True
            >>> tab.celulaEhValida(1, 0)
            True
            >>> tab.celulaEhValida(-1, 0)
            False
        '''
        return (coluna >= 0) and (coluna < self.colunas()) and \
        (linha >= 0) and (linha < self.linhas())

    #celula
    def celula(self, linha, coluna):
        return self.tabuleiro[linha][coluna]
        
    #obterCelulaNaoVazia
    def obterCelulaNaoVazia(self, linha, coluna, direcao):
        '''
            >>> tab = Tabuleiro()
            >>> tab.iniciar([[1,2,1,3,4],[0,3,4,2,3],[4,3,4,2,3],[3,4,3,2,1],[2,3,4,3,4],[2,3,4,3,4]])
            >>> tab.obterCelulaNaoVazia(0, 0, tab.acima)
            (0, 0)
            >>> tab.obterCelulaNaoVazia(1, 0, tab.acima)
            (0, 0)
            >>> tab.celula(2, 0)
            4
            >>> tab.obterCelulaNaoVazia(2, 0, tab.acima)
            (2, 0)
            >>> tab.obterCelulaNaoVazia(1, 1, tab.acima)
            (1, 1)
        '''
        if not self.celulaEhValida(linha, coluna):
            return -1, -1            
        if self.celula(linha,coluna) in range(1, 5):
            return linha, coluna
        if direcao == self.acima:
            return self.obterCelulaNaoVazia(linha - 1, coluna, direcao)
        elif direcao == self.abaixo:
            return self.obterCelulaNaoVazia(linha + 1, coluna, direcao)
        elif direcao == self.esquerda:
            return self.obterCelulaNaoVazia(linha, coluna - 1, direcao)
        else:
            return self.obterCelulaNaoVazia(linha, coluna + 1, direcao)
        

    #iniciar
    def iniciar(self, matriz):
        self.tabuleiro = matriz

    #percorrer
    def percorrer(self):
        """
            >>> tab = Tabuleiro()
            >>> tab.iniciar([[5,2,1,3,4],[0,3,4,2,3],[4,3,4,2,3],[3,4,3,2,1],[2,3,4,3,4],[2,3,4,3,4]])
            >>> tab.percorrer()
            >>> tab.celula(0, 0)
            0
            >>> tab.celula(0, 1)
            3
            >>> tab.celula(1, 0)
            0
            >>> tab.celula(2, 0)
            0
            >>> tab.celula(3, 0)
            4
        """
        for linha in range(0, self.linhas() - 1):
            for coluna in range(0, self.colunas() - 1):
                if self.celula(linha, coluna) == 5:
                    self.tabuleiro[linha][coluna] = 0
                    
                    x, y = self.obterCelulaNaoVazia(linha - 1, coluna, self.acima)
                    self.tocar(x, y)
                    
                    x, y = self.obterCelulaNaoVazia(linha + 1, coluna, self.abaixo)
                    self.tocar(x, y)
                    
                    x, y = self.obterCelulaNaoVazia(linha, coluna - 1, self.esquerda)
                    self.tocar(x, y)
                    
                    x, y = self.obterCelulaNaoVazia(linha, coluna + 1, self.direita)
                    self.tocar(x, y)

    #linhas
    def linhas(self):
        return len(self.tabuleiro)
        
    #colunas
    def colunas(self):
        if self.linhas == 0: return 0
        return len(self.tabuleiro[0])
    
    #imprimir
    def imprimir(self, linha, coluna):
        print self.tabuleiro[linha][coluna]

    #__repr__
    def __repr__(self):
        return "Tabuleiro de %d linhas e %d colunas\n %s" % (self.linhas(), self.colunas(), \
                                                          [linha for linha in self.tabuleiro])
                                                        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
	
