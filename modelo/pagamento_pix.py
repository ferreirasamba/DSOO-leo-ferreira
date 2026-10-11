from modelo.pagamento import Pagamento
from datetime import date
from modelo.atendimento import Atendimento
from modelo.paciente import Paciente
from utilidades import ErroDeRegra, so_digitos


class PagamentoPix(Pagamento):
    def __init__(self, data:date, 
                       atendimento:Atendimento, 
                       paciente:Paciente, 
                       valor, 
                       cpf_pagador: str):
        super().__init__(data, atendimento, paciente, valor)
        cpf = so_digitos(cpf_pagador)
        if len(cpf) != 11:
            raise ErroDeRegra("CPF do pagador deve ter 11 dígitos.")
        self.__cpf_pagador = cpf

    @property
    def cpf_pagador(self): 
        return self.__cpf_pagador

    def modalidade(self):
        return f"PIX (CPF pagador {self.__cpf_pagador})"