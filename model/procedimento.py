from abstractClasses.abstractProcedimento import AbstractProcedimento
from model.profissional import Profissional

class Procedimento(AbstractProcedimento):
    def __init__(self, descricao:str, custo, profissional:Profissional):
        super().__init__(descricao, custo, profissional)

    @property
    def descricao(self):
        return super().descricao

    @property
    def custo(self):
        return super().custo

    @property
    def profissional(self):
        return super().profissional