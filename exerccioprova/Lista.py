##1. Lista Encadeada (básico)

##Crie uma função que imprima apenas os apartamentos que têm vaga.
class Apartamento:
    def __init__(self, numero):
        self.numero = numero
        self.vaga = None
        self.proximo = None
    def imprimir_com_vaga(inicio):
        aux = inicio
    while aux:
        if aux.vaga is not None:
            print(aux.numero)
        aux = aux.proximo










##2. Lista Encadeada (médio)

##Crie uma função que conte quantos apartamentos existem na lista.
def contar(inicio):
    aux = inicio
    contador = 0

    while aux:
        contador += 1
        aux = aux.proximo

    return contador
