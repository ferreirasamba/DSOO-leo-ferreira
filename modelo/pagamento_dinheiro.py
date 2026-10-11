from __future__ import annotations

from datetime import date
from modelo.pagamento import Pagamento
from modelo.paciente import Paciente
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modelo.atendimento import Atendimento
    from modelo.procedimento import Procedimento


class PagamentoDinheiro(Pagamento):
    def __init__(self, data: date, atendimento: Atendimento, paciente: Paciente,
                 valor, procedimento: Procedimento | None = None):
        super().__init__(data, atendimento, paciente, valor, procedimento)

    def modalidade(self):
        return "Dinheiro"
