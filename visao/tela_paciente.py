from visao.abstract_tela import AbstractTela


class TelaPaciente(AbstractTela):
    def mostra_menu(self) -> int:
        return self.le_opcao_menu("PACIENTES", ["Cadastrar paciente", "Listar pacientes"])

    def le_dados_paciente(self) -> dict:
        self.mostra_titulo("Novo paciente")
        return {
            "nome": self.le_texto("Nome: "),
            "celular": self.le_texto("Celular: "),
            "cpf": self.le_texto("CPF: "),
            "data_nascimento": self.le_data("Data de nascimento (dd/mm/aaaa): "),
        }

    def mostra_pacientes(self, pacientes: list):
        linhas = []
        for p in pacientes:
            linha = (f"{p.nome} | CPF {p.cpf} | cel. {p.celular} | "
                     f"nasc. {p.data_nascimento:%d/%m/%Y}")
            if p.responsavel is not None:
                linha += f" | responsável: {p.responsavel.nome}"
            linhas.append(linha)
        self.mostra_lista("Pacientes cadastrados", linhas)