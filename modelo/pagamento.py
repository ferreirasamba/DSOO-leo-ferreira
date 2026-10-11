from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import date
from modelo.paciente import Paciente
from typing import TYPE_CHECKING
from utilidades import ErroDeRegra, dinheiro

if TYPE_CHECKING:
    from modelo.atendimento import Atendimento
    from modelo.procedimento import Procedimento

class Pagamento(ABC):
    def __init__(self, data:date,
                       atendimento:Atendimento,
                       paciente:Paciente,
                       valor,
                       procedimento:Procedimento | None = None):
        valor = dinheiro(valor)
        if valor <= 0:
            raise ErroDeRegra("Valor do pagamento deve ser positivo.")
        self.__data = data
        self.__atendimento = atendimento
        self.__paciente = paciente
        self.__valor = valor
        self.__procedimento = procedimento

    @property
    def data(self):
        return self.__data

    @property
    def atendimento(self):
        return self.__atendimento

    @property
    def paciente(self):
        return self.__paciente

    @property
    def valor(self):
        return self.__valor

    @property
    def procedimento(self):
        return self.__procedimento

    @abstractmethod
    def modalidade(self) -> str:
        pass

    def __str__(self):
        destino = (f" | Procedimento: {self.procedimento.descricao}"
                   if self.procedimento is not None else " | Atendimento")
        return f"{self.data:%d/%m/%Y} | R$ {self.valor} | {self.modalidade()}{destino}"

