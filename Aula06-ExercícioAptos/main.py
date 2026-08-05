from Apartamento import Apartamento
from Torre import Torre
from Fila import Fila
from Lista import Lista

def liberar_vaga(lista, fila, numero_vaga):
    apt_sem_vaga = lista.remover_por_vaga( numero_vaga )

    if apt_sem_vaga:
        apt_sem_vaga.vaga = None
        fila.add(apt_sem_vaga)

    apt_com_vaga = fila.remover()

    if apt_com_vaga:
        apt_com_vaga.vaga = numero_vaga
        lista.inserir_ordenado( apt_com_vaga )

t1 = Torre (1, "Torre A", "Centro")

a1 = Apartamento( 1 , "101", t1, 1)
a2 = Apartamento( 2 , "102", t1, 2)
a3 = Apartamento( 3 , "103", t1, None)
a4 = Apartamento( 4 , "104", t1, None)

lista = Lista()
fila = Fila()

# apartamentos com vaga
lista.inserir_ordenado(a1)

lista.inserir_ordenado(a2)

# fila de espera
fila.add(a3)
fila.add(a4)

lista.imprimir()
fila.imprimir()

print("\n--- Liberando vaga 1 ---")
liberar_vaga( lista, fila, 1)

lista.imprimir()
fila.imprimir()