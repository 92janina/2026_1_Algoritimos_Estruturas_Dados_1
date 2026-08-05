from Apartamento import Apartamento

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self,apartamento):
        if self.inicio is None:
            self.inicio = apartamento
        else:
            self.fim.proximo = apartamento
        self.fim = apartamento
        print(" Apartamento adicionado: ", apartamento)
    
   
    def remover(self):
        if self.inicio is not None:
            removido = self.inicio
            self.inicio = self.inicio.proximo

            if self.inicio is None:
                self.fim = None
            print("Apartamento removido: ",removido)
            self.imprimir()
            return removido
        else:
            print("Fila vazia")
            self.imprimir()
            return None
    
    def imprimir(self):
        print("-----------------------------------")
        if self.inicio is None:
            print(" Apartamento não cadastrado!")
        else:
            aux = self.inicio
            while aux:
                print( aux )
                aux = aux.proximo