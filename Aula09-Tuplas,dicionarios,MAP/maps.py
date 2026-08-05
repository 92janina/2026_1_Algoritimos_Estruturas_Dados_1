def imprimirNome( n ):
    print("Nome: ", n )
nomes = "João" , "Maria" , "José"
resultNomes = map( imprimirNome, nomes )
list( resultNomes )


print("--------------Próximooooooo------------------------")

def aumentarPreco( p ):
    return p * 1.1
precos = [ 1.99 , 20.50 , 10, 19.90 ]
print( "Preços antigos: ", precos)
novosPrecos = map( aumentarPreco , precos )
print( "Preços novos: ", list(novosPrecos) )


print("--------------Próximooooooo------------------------")

def somarValor( valores ):
    total = 0
    for v in valores:
        total += v
    return total

values = (1, 2) , [1, 2, 3] , (10, 20, 30, 40)
print(list(map(somarValor, values)))