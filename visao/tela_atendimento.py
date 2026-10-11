from visao.abstract_tela import AbstractTela


class TelaAtendimento(AbstractTela):
    def mostra_menu(self) -> int:
        return self.le_opcao_menu(
            "ATENDIMENTOS",
            ["Agendar atendimento", "Registrar procedimento realizado",
             "Listar atendimentos", "Ver detalhes de um atendimento"],
        )

    def le_dados_agendamento(self) -> dict:
        self.mostra_titulo("Dados do agendamento")
        return {
            "data": self.le_data("Data (dd/mm/aaaa): "),
            "inicio": self.le_hora("Horário de início (HH:MM): "),
            "fim": self.le_hora("Horário de fim (HH:MM): "),
            "valor": self.le_decimal("Valor do atendimento (R$): "),
        }

    def le_dados_procedimento(self) -> dict:
        self.mostra_titulo("Novo procedimento")
        return {
            "descricao": self.le_texto("Descrição: "),
            "custo": self.le_decimal("Custo (R$): "),
        }

    def mostra_atendimentos(self, atendimentos: list):
        self.mostra_lista("Atendimentos", [str(a) for a in atendimentos])

    def mostra_detalhes(self, atendimento):
        self.mostra_titulo("Detalhes do atendimento")
        print(atendimento)
        print(f"Pago: R$ {atendimento.valor_pago} | Restante: R$ {atendimento.valor_restante}")
        print("Procedimentos:")
        if not atendimento.procedimentos:
            print("  (nenhum)")
        for procedimento in atendimento.procedimentos:
            print(f"  - {procedimento}")
        print("Pagamentos:")
        if not atendimento.pagamentos:
            print("  (nenhum)")
        for pagamento in atendimento.pagamentos:
            print(f"  - {pagamento}")