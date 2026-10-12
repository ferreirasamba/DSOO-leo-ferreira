from __future__ import annotations
from modelo.pagamento import Pagamento
from datetime import date
from typing import TYPE_CHECKING
from modelo.paciente import Paciente
from utilidades import ErroDeRegra, so_digitos

if TYPE_CHECKING:
    from modelo.atendimento import Atendimento
    from modelo.procedimento import Procedimento
class PagamentoPix(Pagamento):
    def __init__(self, data:date, 
                       atendimento:Atendimento, 
                       paciente:Paciente, 
                       valor, 
                       cpf_pagador: str,
                       procedimento: Procedimento | None = None):
        super().__init__(data, atendimento, paciente, valor, procedimento)
        self.cpf_pagador = cpf_pagador

    @property
    def cpf_pagador(self): 
        return f"***.***.***-{self.__final_cpf_pagador}"

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str):
        cpf = so_digitos(cpf_pagador)
        if len(cpf) != 11:
            raise ErroDeRegra("CPF do pagador deve ter 11 dígitos.")
        self.__final_cpf_pagador = cpf[-2:]

    def modalidade(self):
        return f"PIX (CPF pagador {self.cpf_pagador})"
