from Carro import Carro
from Drones import Drones

class Pilha:
    def __init__(self):
        self.topo = None

    def add(self, carro):
        if self.topo is not None:
            carro.prox = self.topo
        self.topo = carro
        self.imprimir()

    def add(self, drones):
        if self.topo is not None:
            drones.prox = self.topo
        self.topo = drones
        self.imprimir()
        
    def remover(self):
        if self.topo is not None:
            aux = self.topo
            self.topo = self.topo.prox
            del(aux)
        self.imprimir()
    
    def imprimir(self):
        if self.topo is None:
            print("\nPilha de carros vazia")
        else:
            print("\nPilha de Carros")
            aux = self.topo
            while aux:
                print( aux )
                aux = aux.prox

    def imprimir(self):
        if self.topo is None:
            print("\nPilha de drones vazia")
        else:
            print("\nPilha de drones")
            aux = self.topo
            while aux:
                print( aux )
                aux = aux.prox
