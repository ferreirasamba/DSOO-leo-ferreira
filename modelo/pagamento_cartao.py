from __future__ import annotations
from modelo.pagamento import Pagamento
from datetime import date
from typing import TYPE_CHECKING
from modelo.paciente import Paciente
from utilidades import ErroDeRegra, so_digitos

if TYPE_CHECKING:
    from modelo.atendimento import Atendimento
class PagamentoCartao(Pagamento):
    def __init__(self, data:date, 
                       atendimento:Atendimento, 
                       paciente:Paciente, 
                       valor, 
                       numero_cartao: str, 
                       bandeira: str):
        super().__init__(data, atendimento, paciente, valor)
        numero = so_digitos(numero_cartao)
        if not 13 <= len(numero) <= 19:
            raise ErroDeRegra("Número de cartão inválido.")
        self.__numero = numero
        self.__bandeira = bandeira

    @property
    def numero_cartao(self): return self.__numero

    @property
    def bandeira(self): return self.__bandeira

    def modalidade(self):
        return f"Cartão de crédito {self.__bandeira} (final {self.__numero[-4:]})"