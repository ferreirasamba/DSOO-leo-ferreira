from visao.abstract_tela import AbstractTela


class TelaTipoAtendimento(AbstractTela):
    def mostra_menu(self) -> int:
        return self.le_opcao_menu("TIPOS DE ATENDIMENTO", ["Cadastrar tipo", "Listar tipos",
                                                            "Alterar tipo", "Excluir tipo"])

    def le_nome_tipo(self) -> str:
        return self.le_texto("Nome do tipo (ex.: Consulta, Exame, Retorno): ")

    def mostra_tipos(self, tipos: list):
        self.mostra_lista("Tipos de atendimento", [t.nome for t in tipos])
