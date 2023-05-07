from computador import Computador

class Notebook(Computador):
    def __init__(self, modelo=None, cor=None, preco=None, tempoDeBateria=None):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        super().getInformacoes()
        print(self.__tempoDeBateria)

    def cadastrar(self, modelo, cor, preco, tempoDeBateria):
        super().cadastrar()
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.__tempoDeBateria = tempoDeBateria