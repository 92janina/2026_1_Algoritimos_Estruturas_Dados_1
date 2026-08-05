from Pilha import Pilha
from Drones import Drones
from Carro import Carro

lifo = Pilha()
lifo.imprimir()

c1= Carro( "Chevrolet","2012", 4)
d1= Drones( "Sansung","Digital",2)
c2= Carro("Ford","2008",4)
d2= Drones("Paraguai","Analógico",3)

lifo.add(c1)
lifo.add(c2)
lifo.add(d1)
lifo.remover()
lifo.add(d2)

def menu():
    print(" --------------------------- ")
    print("| 1) Adicionar Carro |")
    print("| 2) Adicionar Drone          |")
    print("| 3) Imprimir Fila de Drones  |")
    print("| 4) Imprimir Fila de Carros   |")
    print("| 5) Remover Drones   |")
 
    print("| 0) Sair                   |")
    print(" --------------------------- ")