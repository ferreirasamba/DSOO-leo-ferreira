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
        self._validar_campos(data, atendimento, paciente, valor, procedimento)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: date):
        self._validar_campos(data, self.__atendimento, self.__paciente,
                             self.__valor, self.__procedimento)
        self.__data = data

    @property
    def atendimento(self):
        return self.__atendimento

    @atendimento.setter
    def atendimento(self, atendimento: Atendimento):
        from modelo.atendimento import Atendimento as AtendimentoModelo
        if not isinstance(atendimento, AtendimentoModelo):
            raise ErroDeRegra("Atendimento inválido.")
        if atendimento is self.__atendimento:
            return
        if self in self.__atendimento.pagamentos:
            raise ErroDeRegra("Não é possível trocar o atendimento de um pagamento já registrado.")
        self._validar_campos(self.__data, atendimento, self.__paciente,
                             self.__valor, self.__procedimento)
        self.__atendimento = atendimento

    @property
    def paciente(self):
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        self._validar_campos(self.__data, self.__atendimento, paciente,
                             self.__valor, self.__procedimento)
        self.__paciente = paciente

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        valor = dinheiro(valor)
        if valor <= 0:
            raise ErroDeRegra("Valor do pagamento deve ser positivo.")
        self._validar_campos(self.__data, self.__atendimento, self.__paciente,
                             valor, self.__procedimento)
        self.__valor = valor

    @property
    def procedimento(self):
        return self.__procedimento

    @procedimento.setter
    def procedimento(self, procedimento: Procedimento | None):
        self._validar_campos(self.__data, self.__atendimento, self.__paciente,
                             self.__valor, procedimento)
        self.__procedimento = procedimento

    def _validar_campos(self, data, atendimento, paciente, valor, procedimento):
        from modelo.atendimento import Atendimento as AtendimentoModelo
        if not isinstance(atendimento, AtendimentoModelo):
            raise ErroDeRegra("Atendimento inválido.")
        if not isinstance(paciente, Paciente):
            raise ErroDeRegra("Paciente inválido.")
        if not isinstance(data, date):
            raise ErroDeRegra("Data do pagamento inválida.")
        if valor <= 0:
            raise ErroDeRegra("Valor do pagamento deve ser positivo.")
        atendimento._validar_pagamento(self, data, paciente, valor, procedimento)

    @abstractmethod
    def modalidade(self) -> str:
        pass

    def __str__(self):
        destino = (f" | Procedimento: {self.procedimento.descricao}"
                   if self.procedimento is not None else " | Atendimento")
        return f"{self.data:%d/%m/%Y} | R$ {self.valor} | {self.modalidade()}{destino}"

