from controlador.abstract_controlador import AbstractControlador
from modelo.pagamento_cartao import PagamentoCartao
from modelo.pagamento_dinheiro import PagamentoDinheiro
from modelo.pagamento_pix import PagamentoPix
from utilidades import ErroDeRegra
from visao.tela_pagamento import TelaPagamento


class ControladorPagamento(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela = TelaPagamento()

    def abre_tela(self):
        self.executa_menu(self.__tela, {1: self.registrar, 2: self.consultar})

    def registrar(self):
        atendimento = self.exige_escolha(
            self.controlador_sistema.controlador_atendimento.seleciona())
        if atendimento.quitado:
            raise ErroDeRegra("Este atendimento já está quitado.")
        self.__tela.mostra_mensagem(f"Valor restante: R$ {atendimento.valor_restante}")

        modalidade = self.__tela.le_modalidade()
        if modalidade == 0:
            raise ErroDeRegra("Operação cancelada.")
        comuns = self.__tela.le_dados_comuns()
        paciente = atendimento.paciente

        if modalidade == 1:
            pagamento = PagamentoDinheiro(comuns["data"], atendimento, paciente, comuns["valor"])
        elif modalidade == 2:
            cpf = self.__tela.le_cpf_pagador()
            pagamento = PagamentoPix(comuns["data"], atendimento, paciente, comuns["valor"], cpf)
        else:
            cartao = self.__tela.le_dados_cartao()
            pagamento = PagamentoCartao(comuns["data"], atendimento, paciente, comuns["valor"],
                                        cartao["numero"], cartao["bandeira"])
        atendimento.registrar_pagamento(pagamento)
        self.__tela.mostra_mensagem(
            f"Pagamento registrado! Restante: R$ {atendimento.valor_restante}")

    def consultar(self):
        atendimento = self.exige_escolha(
            self.controlador_sistema.controlador_atendimento.seleciona())
        self.__tela.mostra_pagamentos(atendimento)