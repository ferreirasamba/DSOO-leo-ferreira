from abstractClasses.abstractControladorPagamentos import AbstractControladorPagamentos
from model.pagamentoCartao import PagamentoCartao
from model.pagamentoDinheiro import PagamentoDinheiro
from model.pagamentoPix import PagamentoPix
from abstractClasses.abstractPagamento import AbstractPagamento
from typing import List

class ControladorPagamentos(AbstractControladorPagamentos):
    def __init__(self):
        super().__init__()

    @property
    def pagamentos(self) -> List:
        return super().pagamentos

    def registrar_pagamento(self):
        valor_pago_cartao = PagamentoCartao.valor_pago
        valor_pago_pix = PagamentoPix.valor_pago
        valor_pago_dinheiro = PagamentoDinheiro.valor_pago
        total_pagar = AbstractPagamento.atendimento.valor
        restante_devendo = 0
        troco_receber = 0
        while restante_devendo != total_pagar:
            if valor_pago_cartao < total_pagar:
                restante_devendo += total_pagar - valor_pago_cartao
                self.__pagamentos.append(valor_pago_cartao)
            elif valor_pago_cartao > total_pagar:
                restante_devendo = total_pagar
                troco_receber += valor_pago_cartao - total_pagar
                self.__pagamentos.append(valor_pago_cartao)
            if valor_pago_pix < total_pagar:
                restante_devendo += total_pagar - valor_pago_pix
                self.__pagamentos.append(valor_pago_pix)
            elif valor_pago_pix > total_pagar:
                restante_devendo = total_pagar
                troco_receber += valor_pago_pix - total_pagar
                self.__pagamentos.append(valor_pago_pix)
            if valor_pago_dinheiro < total_pagar:
                restante_devendo += total_pagar - valor_pago_dinheiro
                self.__pagamentos.append(valor_pago_dinheiro)
            elif valor_pago_dinheiro > total_pagar:
                restante_devendo = total_pagar
                troco_receber += valor_pago_dinheiro - total_pagar
                self.__pagamentos.append(valor_pago_dinheiro)            