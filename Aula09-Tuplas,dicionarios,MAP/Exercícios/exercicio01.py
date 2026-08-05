##Construa um algoritmo que possua uma tupla com os números escritos
##por extenso de “zero” a “nove”. Peça ao usuário para digitar um número
##de 0 a 9 e retorne a ele o número por extenso, sem usar estruturas
#condicionais (if e switch).

numeros = "Zero","Um","Dois","Três","Quatro", "Cinco","Seis","Sete", "Oito","Nove"
sNum= input("Digite um número de 0 a 9: ")
if(sNum.isnumeric() ):
    num = int( sNum)
    print("Número digitado: ", numeros[num] )