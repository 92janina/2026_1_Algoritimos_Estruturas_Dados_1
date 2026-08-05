from Veiculo import Veiculo
class Carro:
    def __init__(self,veiculo = Veiculo(),portas=0):
        self.veiculo = veiculo
        self._portas = portas
        self.proximo = None
    
    def setPortas(self, valor):
        if valor != "" and valor !=  0:
            self._portas = valor
    
    def getPortas(self):
        return self._portas


    def __str__(self):
        txt= "\nCarro: " + self.veiculo
        txt += "\nPortas: " + str( self._portas )
        return txt