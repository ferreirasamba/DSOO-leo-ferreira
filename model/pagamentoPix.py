from abstractClasses.abstractPagamento import AbstractPagamento
from model.paciente import Paciente
from model.atendimento import Atendimento
from datetime import date

class PagamentoPix(AbstractPagamento):
    def __init__(self, data:date, atendimento:Atendimento, paciente:Paciente, valor_pago):
        super().__init__(data, atendimento, paciente, valor_pago)

    @property
    def data(self) -> date:
        return super().data

    @property
    def atendimento(self) -> Atendimento:
        return super().atendimento

    @property
    def paciente(self) -> Paciente:
        return super().paciente

    @property
    def valor_pago(self):
        return super().valor_pago