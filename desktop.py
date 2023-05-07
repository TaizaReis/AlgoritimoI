from computador import Computador

class Desktop(Computador):
    def __init__(self, modelo=None, cor=None, preco=None, potenciaDaFonte=None):
        super().__init__(modelo, cor, preco)
        self._potenciaDaFonte = potenciaDaFonte

    def getInformacoes(self):
        super().getInformacoes()
        print(self._potenciaDaFonte)

    def cadastrar(self, modelo, cor, preco, potenciaDaFonte):
        super().cadastrar()
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self._potenciaDaFonte = potenciaDaFonte


