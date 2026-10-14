from visao.abstract_tela import AbstractTela
from utilidades import ErroDeRegra


class TelaPagamento(AbstractTela):
    def mostra_menu(self) -> int:
        return self.le_opcao_menu(
            "PAGAMENTOS",
            ["Registrar pagamento", "Consultar pagamentos de um atendimento",
             "Consultar pagamentos de um procedimento", "Alterar pagamento",
             "Excluir pagamento"],
        )

    def le_destino_pagamento(self, atendimento):
        opcoes = [f"Atendimento (restante R$ {atendimento.valor_restante_atendimento})"]
        opcoes.extend(
            f"Procedimento: {p.descricao} (restante R$ "
            f"{atendimento.valor_restante_procedimento(p)})"
            for p in atendimento.procedimentos
        )
        indice = self.escolhe_da_lista("Onde registrar o pagamento?", opcoes)
        if indice is None:
            raise ErroDeRegra("Operação cancelada.")
        if indice == 0:
            return None
        return atendimento.procedimentos[indice - 1]

    def seleciona_procedimento(self, atendimento):
        indice = self.escolhe_da_lista(
            "Escolha o procedimento",
            [f"{p.descricao} - R$ {p.custo}" for p in atendimento.procedimentos],
        )
        return None if indice is None else atendimento.procedimentos[indice]

    def le_modalidade(self) -> int:
        """1 = dinheiro, 2 = PIX, 3 = cartão, 0 = cancelar."""
        return self.le_opcao_menu("Modalidade", ["Dinheiro", "PIX", "Cartão de crédito"],
                                  rotulo_zero="Cancelar")

    def le_dados_comuns(self) -> dict:
        return {
            "data": self.le_data("Data do pagamento (dd/mm/aaaa): "),
            "valor": self.le_decimal("Valor pago (R$): "),
        }

    def le_dados_edicao_pagamento(self) -> dict:
        self.mostra_titulo("Novos dados do pagamento")
        return {
            "data": self.le_data("Data do pagamento (dd/mm/aaaa): "),
            "valor": self.le_decimal("Valor pago (R$): "),
        }

    def le_dados_edicao_cartao(self) -> dict:
        return {
            "numero": self.le_texto("Número do cartão: "),
            "bandeira": self.le_texto("Bandeira (Visa, Mastercard...): "),
        }

    def seleciona_pagamento(self, atendimento):
        indice = self.escolhe_da_lista(
            "Escolha o pagamento", [str(p) for p in atendimento.pagamentos])
        return None if indice is None else atendimento.pagamentos[indice]

    def le_cpf_pagador(self) -> str:
        return self.le_texto("CPF do pagador: ")

    def le_dados_cartao(self) -> dict:
        return {
            "numero": self.le_texto("Número do cartão: "),
            "bandeira": self.le_texto("Bandeira (Visa, Mastercard...): "),
        }

    def mostra_pagamentos(self, atendimento):
        self.mostra_lista(f"Pagamentos - {atendimento}", [str(p) for p in atendimento.pagamentos])
        print(f"Total: R$ {atendimento.valor_total} | Pago: R$ {atendimento.valor_pago} "
              f"| Restante: R$ {atendimento.valor_restante}")

    def mostra_pagamentos_procedimento(self, atendimento, procedimento, pagamentos,
                                       valor_pago, valor_restante):
        self.mostra_lista(
            f"Pagamentos do procedimento: {procedimento.descricao}",
            [str(p) for p in pagamentos],
        )
        print(f"Atendimento: {atendimento}")
        print(f"Custo: R$ {procedimento.custo} | Pago: R$ {valor_pago} "
              f"| Restante: R$ {valor_restante}")
