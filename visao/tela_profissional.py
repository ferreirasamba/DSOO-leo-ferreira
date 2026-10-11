from visao.abstract_tela import AbstractTela


class TelaProfissional(AbstractTela):
    def mostra_menu(self) -> int:
        return self.le_opcao_menu("PROFISSIONAIS", ["Cadastrar profissional", "Listar profissionais"])

    def le_dados_profissional(self) -> dict:
        self.mostra_titulo("Novo profissional")
        return {
            "nome": self.le_texto("Nome: "),
            "celular": self.le_texto("Celular: "),
            "cpf": self.le_texto("CPF: "),
            "data_nascimento": self.le_data("Data de nascimento (dd/mm/aaaa): "),
            "especialidade": self.le_texto("Especialidade: "),
            "registro": self.le_texto("Registro profissional (ex.: CRM-SC 1234): "),
        }

    def mostra_profissionais(self, profissionais: list):
        self.mostra_lista("Profissionais cadastrados", [
            f"{p.nome} - {p.especialidade} ({p.registro}) | CPF {p.cpf} | cel. {p.celular}"
            for p in profissionais
        ])