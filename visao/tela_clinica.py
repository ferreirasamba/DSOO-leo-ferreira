from visao.abstract_tela import AbstractTela


class TelaClinica(AbstractTela):
    def mostra_menu(self) -> int:
        return self.le_opcao_menu("CLÍNICAS", ["Cadastrar clínica", "Listar clínicas"])

    def le_dados_clinica(self) -> dict:
        self.mostra_titulo("Nova clínica")
        return {
            "nome": self.le_texto("Nome: "),
            "cidade": self.le_texto("Cidade: "),
            "descricao": self.le_texto("Descrição: "),
            "abertura": self.le_hora("Abertura (HH:MM): "),
            "fechamento": self.le_hora("Fechamento (HH:MM): "),
        }

    def mostra_clinicas(self, clinicas: list):
        self.mostra_lista("Clínicas cadastradas", [
            f"{c.nome} - {c.cidade} | {c.descricao} | {c.abertura:%H:%M} às {c.fechamento:%H:%M}"
            for c in clinicas
        ])