carros = "Uno" , "Doblo" , "Renegade" , "Toro"
print( carros [-1] )
print( carros[ -3 : -1 ] )
print( carros[ 2 : ] )
print( carros[ -2 : ] )
print("--------Próximo------------")
def calcular(x, y):
    return x+y, x-y , x*y , x/y

result = calcular( 5, 2 )
print( result )
for x in result:
    print("Resultado: ", x)

a, b, c, d = calcular( 10 , 5 )
print("Soma: ", a)
print("Subtração: ", b)
print("Multiplicação: ", c)
print("Divisão: ", d)