from Torre import Torre
class Apartamento:
    def __init__(self, id,numero, torre, vaga = None):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None

    def __str__(self):
        txt= "\nId: " + str(self.id)
        txt += "\nNúmero: " + self.numero
        txt += "\nTorre: " + str(self.torre)
        txt += "\nVaga: " + str(self.vaga)
        return txt
    

