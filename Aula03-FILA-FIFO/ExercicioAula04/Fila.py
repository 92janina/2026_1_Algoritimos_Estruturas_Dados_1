from Carro import Carro
class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self,car):
        if self.inicio is None:
            self.inicio = car
        else:
            self.fim.prox = car
        self.fim = car
    
    def imprimir(self):
        print("-----------------------------------")
        if self.inicio is None:
            print("Fila de Carros vazia!")
        else:
            aux = self.inicio
            while aux:
                print( aux )
    
    def lavar(self):
        if self.inicio is None:
            print("Não há carros para lavar.")
        else:
            print("Carro Lavado: ")
            print( self.inicio )
            aux = self.inicio
            self.inicio = self.inicio.prox
            del( aux )
            if self.inicio is None:
                self.fim =None

