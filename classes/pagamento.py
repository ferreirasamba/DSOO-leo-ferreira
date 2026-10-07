from abstractClasses.abstractPagamento import Pagamento as AbstractPagamento
from datetime import date as Date
from classes.atendimento import Atendimento
from classes.paciente import Paciente

class Pagamento(AbstractPagamento):
    def __init__(self, data, atendimento, paciente, valor):
        super().__init__(data, atendimento, paciente, valor)

    @property
    def data(self):
        return super().data

    @property
    def atendimento(self):
        return super().atendimento

    @property
    def paciente(self):
        return super().paciente

    @property
    def valor(self):
        return super().valor

    def pagar(self, total):
        return super().pagar(total)
