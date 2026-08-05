from Torre import Torre

class Apartamento:

    def __init__(self, id = 0,numero = None, torre = Torre()):#eu posso chamar a torre assim :Torre() sem parametros pq na classe torre eu ja defini
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = None
        self.proximo = None

    def __str__(self):
        txt= "Apartamento: " + str(self.id)
        txt += "\nNúmero: " + self.numero
        txt += "\n " + str(self.torre)
        if self.vaga:
            txt +="\nVaga: " + str(self.vaga)
        else:
            txt +="\nVaga: " + str(self.vaga)
        return txt
    def imprimir(self):
        print(self)
         
