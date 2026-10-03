from abstractClasses.abstractProcedimento import Procedimento as AbstractProcedimento

class Procedimento(AbstractProcedimento):
    def __init__(self, descricao, custo, profissional):
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

