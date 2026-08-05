
class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        txt = "Id: " + str(self.id)
        txt += "Nome: " + self.nome
        txt += "Endereço: " + self.endereco
        return txt
    

