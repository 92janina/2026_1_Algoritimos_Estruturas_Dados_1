class Autor:
    def __init__(self, nome = "Sem nome", ano = 2020): 
##nunca posso declara valor default no meio começo da direitapra esquerda mas nunca so do meio
        self._nome = nome 
#usado assim modificado self._ fracamente privado é regra de acesso que pode ser privado protegido e publico
        self.__ano = ano

    #método modificador- para setar tem regras-altera com validação
    def setNome(self, valor):
        if valor != "" and valor !=  "Adalto":
            self._nome = valor

    #método acessor-pega
    def getNome(self):
        return self._nome
    
    @property ##faz um método funcionar como se fosse um atributo,
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, valor):
        if valor < 2026:
            self.__ano = valor
    
    def __str__(self):
        txt = "Autor: " + self._nome
        txt += " - Ano: " + str(self.__ano )
        return txt


