from Veiculo import Veiculo
class Drones:
    def __init__(self, veiculo= Veiculo(), quantidade_helices = 0):
        self.veiculo = veiculo
        self.__quantidade_helices = quantidade_helices
        self.proximo = None
   
    def setQuantidade_helices(self, valor):
        if valor != "" and valor !=  0:
            self._portas = valor
    
    def getPortas(self):
        return self.__quantidade_helices


    def __str__(self):
        txt= "\nDrones: " + self.veiculo
        txt += "\nQuantidade de helices: " + str( self.__quantidade_helices)
        return txt

    