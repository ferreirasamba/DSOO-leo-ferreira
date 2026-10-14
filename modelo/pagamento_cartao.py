from __future__ import annotations
from modelo.pagamento import Pagamento
from datetime import date
from typing import TYPE_CHECKING
from modelo.paciente import Paciente
from utilidades import ErroDeRegra, so_digitos

if TYPE_CHECKING:
    from modelo.atendimento import Atendimento
    from modelo.procedimento import Procedimento
class PagamentoCartao(Pagamento):
    def __init__(self, data:date, 
                       atendimento:Atendimento, 
                       paciente:Paciente, 
                       valor, 
                       numero_cartao: str, 
                       bandeira: str,
                       procedimento: Procedimento | None = None):
        super().__init__(data, atendimento, paciente, valor, procedimento)
        self.numero_cartao = numero_cartao
        self.bandeira = bandeira

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: str):
        numero = so_digitos(numero_cartao)
        if not 13 <= len(numero) <= 19:
            raise ErroDeRegra("Número de cartão inválido.")
        self.__numero_cartao = numero

    @property
    def bandeira(self):
        return self.__bandeira

    @bandeira.setter
    def bandeira(self, bandeira: str):
        bandeira = bandeira.strip()
        if not bandeira:
            raise ErroDeRegra("Bandeira do cartão não pode ser vazia.")
        self.__bandeira = bandeira

    def modalidade(self):
        return f"Cartão de crédito {self.__bandeira} (final {self.__numero_cartao[-4:]})"
