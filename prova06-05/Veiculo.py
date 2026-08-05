class Veiculo:
    def __init__(self,marca=None,modelo=None):
        self.marca = marca
        self.modelo = modelo
    def __str__(self):
        txt = "Marca: " + self.marca
        txt += " Modelo: " + self.modelo
        return txt

        