from abstractClasses.abstractClinica import AbstractClinica
from datetime import time
class Clinica(AbstractClinica):
    def __init__(self, nome:str, cidade:str, descricao:str, abre:time, fecha:time) -> None:
        super().__init__(nome, cidade, descricao, abre, fecha)

    @property
    def nome(self):
        return super().nome

    @property
    def cidade(self):
        return super().cidade

    @property
    def descricao(self):
        return super().descricao

    @property
    def abre(self):
        return super().abre

    @property
    def fecha(self):
        return super().fecha

    def funciona_em(self, abertura, fechamento) -> bool:
        return super().funciona_em(abertura, fechamento)
    