def somarAte( n ):
    if n == 1:
        return 1
    else:
        return n + somarAte( n - 1 )

def fatorial( x ):
    if x == 0:
        return 1
    else:
        return x * fatorial( x-1 )    
    
print( "Soma de 1 até 5: ", somarAte(5) )
print( "Soma de 5 é: ", fatorial(5) )

#1)Implemente uma função recursiva para cálculo de potência
#2)Implemente uma função recursiva para contagem regressiva
#3)Implemente uma função recursiva para inverter uma string

#1)
def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base,( expoente - 1))
print( "3 elevado a 5: ",potencia(3,5))

#2)
def contagem_regressiva( n ):
    if n <= 0:
        print(" Fim!")
    else:
        print(n)
        contagem_regressiva( n-1)
contagem_regressiva(6)       


#3)
def inverterString(s):
    if len(s) == 1:
        return s
    return inverterString( s[1:]) + s[0]

print( inverterString("Janina"))



  