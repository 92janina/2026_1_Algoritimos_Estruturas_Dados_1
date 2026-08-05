from Autor import Autor
from Livro import Livro
from Pilha import Pilha

# FUAQ implementa uma pilha de livro.
# Cada livro deverá conter o título, a quantidade de página e 
# o autor, sendo que o autor deverá conter nome, 
# e ano de nascimento.
# Implemente um método para adicionar livros na pilha,
# um método para imprimir a pilha de livros,
# um método para remover um livro da pilha 
# e um método que o usuário informa o nome do autor e 
# lhe é informado quantos livros tem na pilha com este auto



lifo = Pilha()
lifo.imprimir()

a1= Autor( "Machado de Assis", 1938)
a2= Autor( "Érico Veríssimo, 1905")

l1 = Livro( "Dom Casmurro", 288, a1 )
l2 = Livro ( "O tempo e o vento ", 3832, a2)
l3 = Livro ( "Viva a vida")
l4 = Livro ("Mémorias póstuma de Brás Cuba", 200, a1)

lifo.add(l1)
lifo.add(l3)
lifo.add(l2)
lifo.remover()
lifo.add(l4)

lifo.contLivrosPorAutor("Adalto")
lifo.contLivrosPorAutor("Machado de Assis")

