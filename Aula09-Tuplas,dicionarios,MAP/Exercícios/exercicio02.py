##Construa um algoritmo que peça ao usuário para informar o nome, a
##nota01 e a nota02 de um aluno. Guarde estas informações em um
##dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02) /2]
##e adicione ao dicionário. Ao final, imprima todos os dados do
##dicionário.

nome = input("Digite o nome: ")

nota01 = input("Digite a nota 01: ")
nota01 = nota01.replace("," , ".")

nota02 = input("Digite a nota 02: ")
nota02 = nota02.replace("," , ".")

aluno = {
    "nome": nome,
    "nota01": float(nota01),
    "nota02": float(nota02)
} 
aluno["notaFinal"] = (aluno["nota01"] + aluno["nota02"])/2
print( aluno )