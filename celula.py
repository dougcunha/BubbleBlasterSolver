# -*- coding: latin1 -*-
'''
    Classe que representa uma célula de um tabuleiro de 
    Blubble Blast
'''
class Celula:
    vizinhos = []
    def __init__(self, nivel):
        self.nivel = nivel
    def atribuirVizinhos(self, vizinhos):
        self.vizinhos = vizinhos
    def obterNivel(self):
        return self.nivel
    def tocar(self):
        '''
            >>> celula = Celula(1)
            >>> celula2 = Celula(1)
            >>> celula.atribuirVizinhos([celula2])
            >>> celula.tocar()
            >>> celula.obterNivel()
            2
            >>> celula.tocar()
            >>> celula.obterNivel()
            3
            >>> celula.tocar()
            >>> celula.obterNivel()
            4
            >>> celula2.obterNivel()
            1
            >>> celula.tocar()
            >>> celula.obterNivel()
            0
            >>> celula2.obterNivel()
            2
        '''        
        if self.nivel in range(1, 5):
            self.nivel += 1
        if (self.nivel > 4):
            self.nivel = 0
            for vizinho in self.vizinhos:
                vizinho.tocar()
        
    def __repr__(self):
        return 'Celula nivel: %d\n' % (self.nivel)
                    
        
def _doctest():
    import doctest
    doctest.testmod()
    
if __name__ == '__main__':
    _doctest()
        
        