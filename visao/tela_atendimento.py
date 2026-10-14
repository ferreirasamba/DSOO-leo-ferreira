from visao.abstract_tela import AbstractTela


class TelaAtendimento(AbstractTela):
    def mostra_menu(self) -> int:
        return self.le_opcao_menu(
            "ATENDIMENTOS",
            ["Agendar atendimento", "Registrar procedimento realizado",
             "Listar atendimentos", "Ver detalhes de um atendimento",
             "Alterar atendimento", "Excluir atendimento",
             "Alterar procedimento", "Excluir procedimento"],
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

    def le_dados_edicao_atendimento(self) -> dict:
        self.mostra_titulo("Novos dados do atendimento")
        return {
            "data": self.le_data("Data (dd/mm/aaaa): "),
            "inicio": self.le_hora("Horário de início (HH:MM): "),
            "fim": self.le_hora("Horário de fim (HH:MM): "),
            "valor": self.le_decimal("Valor do atendimento (R$): "),
        }

    def le_dados_edicao_procedimento(self) -> dict:
        self.mostra_titulo("Novos dados do procedimento")
        return {
            "descricao": self.le_texto("Descrição: "),
            "custo": self.le_decimal("Custo (R$): "),
        }

    def seleciona_procedimento(self, atendimento, titulo="Escolha o procedimento"):
        indice = self.escolhe_da_lista(titulo, [str(p) for p in atendimento.procedimentos])
        return None if indice is None else atendimento.procedimentos[indice]

    def mostra_atendimentos(self, atendimentos: list):
        self.mostra_lista("Atendimentos", [str(a) for a in atendimentos])

    def mostra_detalhes(self, atendimento):
        self.mostra_titulo("Detalhes do atendimento")
        print(atendimento)
        print(f"Total: R$ {atendimento.valor_total} | Pago: R$ {atendimento.valor_pago} "
              f"| Restante: R$ {atendimento.valor_restante}")
        print("Procedimentos:")
        if not atendimento.procedimentos:
            print("  (nenhum)")
        for procedimento in atendimento.procedimentos:
            pago = atendimento.valor_pago_procedimento(procedimento)
            restante = atendimento.valor_restante_procedimento(procedimento)
            print(f"  - {procedimento} | Pago: R$ {pago} | Restante: R$ {restante}")
        print("Pagamentos:")
        if not atendimento.pagamentos:
            print("  (nenhum)")
        for pagamento in atendimento.pagamentos:
            print(f"  - {pagamento}")
