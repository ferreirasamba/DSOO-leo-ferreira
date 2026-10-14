from decimal import Decimal
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
        self.executa_menu(self.__tela, {
            1: self.registrar,
            2: self.consultar,
            3: self.consultar_procedimento,
            4: self.alterar,
            5: self.excluir,
        })

    def registrar(self):
        atendimento = self.exige_escolha(
            self.controlador_sistema.controlador_atendimento.seleciona())
        if atendimento.quitado:
            raise ErroDeRegra("Este atendimento já está quitado.")
        self.__tela.mostra_mensagem(
            f"Total: R$ {atendimento.valor_total} | Restante: R$ {atendimento.valor_restante}")
        procedimento = self.__tela.le_destino_pagamento(atendimento)
        if procedimento is None:
            restante_destino = atendimento.valor_restante_atendimento
        else:
            restante_destino = atendimento.valor_restante_procedimento(procedimento)
        self.__tela.mostra_mensagem(f"Restante do item selecionado: R$ {restante_destino}")

        modalidade = self.__tela.le_modalidade()
        if modalidade == 0:
            raise ErroDeRegra("Operação cancelada.")
        comuns = self.__tela.le_dados_comuns()
        paciente = atendimento.paciente

        if modalidade == 1:
            pagamento = PagamentoDinheiro(
                comuns["data"], atendimento, paciente, comuns["valor"], procedimento)
        elif modalidade == 2:
            cpf = self.__tela.le_cpf_pagador()
            pagamento = PagamentoPix(
                comuns["data"], atendimento, paciente, comuns["valor"], cpf, procedimento)
        else:
            cartao = self.__tela.le_dados_cartao()
            pagamento = PagamentoCartao(comuns["data"], atendimento, paciente, comuns["valor"],
                                        cartao["numero"], cartao["bandeira"], procedimento)
        atendimento.registrar_pagamento(pagamento)
        if procedimento is None:
            restante_destino = atendimento.valor_restante_atendimento
        else:
            restante_destino = atendimento.valor_restante_procedimento(procedimento)
        self.__tela.mostra_mensagem(
            f"Pagamento registrado! Restante do item: R$ {restante_destino}"
            f" | Restante total: R$ {atendimento.valor_restante}")

    def alterar(self):
        atendimento = self.exige_escolha(
            self.controlador_sistema.controlador_atendimento.seleciona())
        pagamento = self.exige_escolha(self.__tela.seleciona_pagamento(atendimento))
        dados = self.__tela.le_dados_edicao_pagamento()
        procedimento = pagamento.procedimento
        limite = atendimento.valor if procedimento is None else procedimento.custo
        pago_por_outros = sum(
            (p.valor for p in atendimento.pagamentos
             if p is not pagamento and p.procedimento is procedimento),
            start=Decimal("0.00"),
        )
        if dados["valor"] <= 0 or dados["valor"] > limite - pago_por_outros:
            raise ErroDeRegra("Valor inválido ou acima do restante do item.")
        if dados["data"] > atendimento.data:
            raise ErroDeRegra("Pagamento deve ser feito até a data do atendimento.")

        if isinstance(pagamento, PagamentoPix):
            pagamento.cpf_pagador = self.__tela.le_cpf_pagador()
        elif isinstance(pagamento, PagamentoCartao):
            cartao = self.__tela.le_dados_edicao_cartao()
            pagamento.numero_cartao = cartao["numero"]
            pagamento.bandeira = cartao["bandeira"]
        pagamento.data = dados["data"]
        pagamento.valor = dados["valor"]
        self.__tela.mostra_mensagem("Pagamento alterado!")

    def excluir(self):
        atendimento = self.exige_escolha(
            self.controlador_sistema.controlador_atendimento.seleciona())
        pagamento = self.exige_escolha(self.__tela.seleciona_pagamento(atendimento))
        if self.__tela.confirma_acao(f"Excluir o pagamento de R$ {pagamento.valor}?"):
            atendimento.remover_pagamento(pagamento)
            self.__tela.mostra_mensagem("Pagamento excluído!")

    def consultar(self):
        atendimento = self.exige_escolha(
            self.controlador_sistema.controlador_atendimento.seleciona())
        self.__tela.mostra_pagamentos(atendimento)

    def consultar_procedimento(self):
        atendimento = self.exige_escolha(
            self.controlador_sistema.controlador_atendimento.seleciona())
        procedimento = self.exige_escolha(
            self.__tela.seleciona_procedimento(atendimento))
        pagamentos = [p for p in atendimento.pagamentos if p.procedimento is procedimento]
        self.__tela.mostra_pagamentos_procedimento(
            atendimento, procedimento, pagamentos,
            atendimento.valor_pago_procedimento(procedimento),
            atendimento.valor_restante_procedimento(procedimento))
