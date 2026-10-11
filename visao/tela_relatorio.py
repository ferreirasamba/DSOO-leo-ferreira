from visao.abstract_tela import AbstractTela


class TelaRelatorio(AbstractTela):
    def mostra_menu(self) -> int:
        return self.le_opcao_menu(
            "RELATÓRIOS",
            ["Clínicas com mais atendimentos",
             "Atendimentos mais caros",
             "Atendimentos mais baratos",
             "Procedimentos mais realizados",
             "Procedimentos mais caros",
             "Procedimentos mais baratos"],
        )

    def mostra_ranking_clinicas(self, pares: list):
        self.mostra_lista("Clínicas com mais atendimentos",
                          [f"{clinica} - {qtd} atendimento(s)" for clinica, qtd in pares])

    def mostra_atendimentos(self, titulo: str, atendimentos: list):
        self.mostra_lista(titulo, [str(a) for a in atendimentos])

    def mostra_ranking_procedimentos(self, pares: list):
        self.mostra_lista("Procedimentos mais realizados",
                          [f"{descricao} - {qtd}x" for descricao, qtd in pares])

    def mostra_procedimentos(self, titulo: str, procedimentos: list):
        self.mostra_lista(titulo, [str(p) for p in procedimentos])