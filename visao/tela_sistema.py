from visao.abstract_tela import AbstractTela


class TelaSistema(AbstractTela):
    def mostra_menu(self) -> int:
        return self.le_opcao_menu(
            "SISTEMA DE CLÍNICAS",
            ["Clínicas", "Pacientes", "Profissionais", "Tipos de atendimento",
             "Atendimentos", "Pagamentos", "Relatórios"],
            rotulo_zero="Sair",
        )