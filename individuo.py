# -*- coding: utf-8 -*-
import tabuleiro
import random

'''
    Classe que representa uma possível solução para
    um jogo de bubble blast
'''
class Individuo:
    #__init__    
    def __init__(self, toques, linhas, colunas):
        self.toques = toques
        self.linhas = linhas
        self.colunas = colunas
        
    #tamanho
    def tamanho(self):
        return len(self.toques)
        
    #obterToques
    def obterToques(self, inicio, tamanho):
        '''
            >>> ind = Individuo([[0,0], [1,2], [1,3], [0,1]], 6, 5)
            >>> ind.obterToques(2, 2)
            [[1, 3], [0, 1]]
        '''
        resultado = []        
        x = 0
        for i in range(inicio, inicio + tamanho):
            if i > self.tamanho() - 1: break
            resultado.append(self.toques[i])
            x += 1
        return resultado
        
    #cruzar
    def cruzar(self, outro):
        '''
             >>> ind1 = Individuo([[0,0], [1,2], [1,3], [0,1]], 6, 5)
             >>> ind2 = Individuo([[3,1], [0,3], [3,2], [4,5]], 6, 5)
             >>> filho1 = ind1.cruzar(ind2)
             >>> filho1.toques
             [[0, 0], [1, 2], [3, 2], [4, 5]]
             >>> filho2 = ind2.cruzar(ind1)
             >>> filho2.toques
             [[3, 1], [0, 3], [1, 3], [0, 1]]
			 >>> ind1 = Individuo([[0,0], [1,2], [1,3], [0,1], [2,4]], 6, 5)
             >>> ind2 = Individuo([[3,1], [0,3], [3,2], [4,5], [1,0]], 6, 5)
			 >>> filho = ind1.cruzar(ind2)
			 >>> filho.toques
			 [[0, 0], [1, 2], [3, 2], [4, 5], [1, 0]]
        '''
        parte = self.tamanho() / 2        
        return Individuo(self.obterToques(0, parte) + \
                         outro.obterToques(parte, outro.tamanho()),
                         self.linhas, self.colunas)
    #mutar
    def mutar(self):
        '''
            >>> ind = Individuo([[0,0], [1,2], [1,3], [0,1]], 6, 5)
            >>> mutante = ind.mutar()
            >>> mutante.toques
            [[0, 0], [1, 2], [1, 3], [0, 1]]
        '''        
        gene = [[random.randrange(0,self.linhas), random.randrange(0,self.colunas)]]        
        return Individuo(gene + self.obterToques(1, self.tamanho()),
                         self.linhas, self.colunas)
        
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
