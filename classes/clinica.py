from abstractClasses.abstractClinica import Clinica as AbstractClinica

class Clinica(AbstractClinica):
    def __init__(self, nome, localizacao, descricao):
        super().__init__(nome, localizacao, descricao)

    @property
    def nome(self):
        return super().nome

    @property
    def localizacao(self):
        return super().localizacao

    @property
    def descricao(self):
        return super().descricao