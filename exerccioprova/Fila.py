##3. Fila (básico)

##Implemente a função:
##Deve retornar quantos apartamentos estão esperando vaga
def tamanho_fila(fila):
    aux = fila.inicio
    contador = 0

    while aux:
        contador += 1
        aux = aux.proximo

    return contador









##4. Fila (nível prova 👀)

##Corrija o código abaixo:
#👉 O que está errado?
def enfileirar(self, apto):
    if self.inicio == None:
        self.inicio = apto
    else:
        self.fim.proximo = apto
    self.fim = apto

#codigo corrigido
def enfileirar(self, apto):
    apto.proximo = None
    
    if self.inicio is None:
        self.inicio = self.fim = apto
    else:
        self.fim.proximo = apto
        self.fim = apto







##5. Lista Encadeada (nível prova 😈)

##Complete a função:
def buscar(self, numero):
    aux = self.inicio
    
    while aux:
        if aux.numero == numero:
            return ________
                   aux
        aux = aux.proximo
    
    return None