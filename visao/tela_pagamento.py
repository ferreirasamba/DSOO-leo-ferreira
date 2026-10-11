from visao.abstract_tela import AbstractTela


class TelaPagamento(AbstractTela):
    def mostra_menu(self) -> int:
        return self.le_opcao_menu(
            "PAGAMENTOS",
            ["Registrar pagamento", "Consultar pagamentos de um atendimento"],
        )

    def le_modalidade(self) -> int:
        """1 = dinheiro, 2 = PIX, 3 = cartão, 0 = cancelar."""
        return self.le_opcao_menu("Modalidade", ["Dinheiro", "PIX", "Cartão de crédito"],
                                  rotulo_zero="Cancelar")

    def le_dados_comuns(self) -> dict:
        return {
            "data": self.le_data("Data do pagamento (dd/mm/aaaa): "),
            "valor": self.le_decimal("Valor pago (R$): "),
        }

    def le_cpf_pagador(self) -> str:
        return self.le_texto("CPF do pagador: ")

    def le_dados_cartao(self) -> dict:
        return {
            "numero": self.le_texto("Número do cartão: "),
            "bandeira": self.le_texto("Bandeira (Visa, Mastercard...): "),
        }

    def mostra_pagamentos(self, atendimento):
        self.mostra_lista(f"Pagamentos - {atendimento}", [str(p) for p in atendimento.pagamentos])
        print(f"Valor: R$ {atendimento.valor} | Pago: R$ {atendimento.valor_pago} "
              f"| Restante: R$ {atendimento.valor_restante}")