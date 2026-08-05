class Lista: 
    def __init__(self):
        self.inicio = None

    def inserir_ordenado(self, apartamento):
        if self.inicio is None or apartamento.vaga < self.inicio.vaga:
            apartamento.proximo = self.inicio
            self.inicio = apartamento
        else:
            atual = self.inicio
            while atual.proximo and atual.proximo.vaga < apartamento.vaga:
                atual = atual.proximo
            
            apartamento.proximo = atual.proximo
            atual.proximo = apartamento

    def remover_por_vaga(self, vaga):
        atual = self.inicio
        anterior = None

        while atual:
            if atual.vaga == vaga:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return atual
            anterior = atual
            atual = atual.proximo

        return None

    def imprimir(self):
        print("=== LISTA DE APARTAMENTOS COM VAGA ===")
        aux = self.inicio
        while aux:
            print(aux)
            aux = aux.proximo