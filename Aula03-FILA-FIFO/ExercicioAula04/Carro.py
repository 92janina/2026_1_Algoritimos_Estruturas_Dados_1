#Exercício para 08/04/2026
#Implemente uma fila de carros de um lava jato
# Cada carro deve conter modelo, placa e ano
# implemente um método para adicionar carro na fila, 
# um méto para lavar um carro e um método para imprimir 
# a fila de carros
class Carro:
    def __init__(self,modelo=None, placa=None, ano=2026):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.prox = None

    def __str__(self):
        ##return super().__str__()super classe subescrita
        txt = "\nModelo: " + self.modelo
        txt = "\nPlaca: " + self.placa
        txt = "\nAno: " + str(self.ano)
        return txt
