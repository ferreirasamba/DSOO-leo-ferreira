from datetime import date, time
from decimal import Decimal
from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.profissional import Profissional
from modelo.tipo_atendimento import TipoAtendimento
from modelo.procedimento import Procedimento
from modelo.pagamento import Pagamento
from utilidades import ErroDeRegra, dinheiro

class Atendimento:
    def __init__(self, clinica:Clinica,
                       paciente:Paciente,
                       profissional:Profissional,
                       data:date,
                       hora_inicio:time,
                       hora_fim:time,
                       tipo:TipoAtendimento,
                       valor):
        valor = dinheiro(valor)
        if data < date.today():
            raise ErroDeRegra("Data do atendimento não pode estar no passado.")
        if valor < 0:
            raise ErroDeRegra("Valor do atendimento não pode ser negativo.")
        if hora_inicio >= hora_fim:
            raise ErroDeRegra("Horário de início deve ser antes do fim.")
        if not clinica.funciona_em(hora_inicio, hora_fim):
            raise ErroDeRegra(
                f"Fora do horário da clínica ({clinica.abertura:%H:%M}-{clinica.fechamento:%H:%M})."
            )
        if not paciente.pode_atender_sozinho(data):
            resp = paciente.responsavel
            if resp is None or resp.idade_em(data) < 18:
                raise ErroDeRegra("Paciente menor de 18 anos precisa de responsável maior de idade.")
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__hora_inicio = hora_inicio
        self.__hora_fim = hora_fim
        self.__tipo = tipo
        self.__valor = valor
        self.__procedimentos = []
        self.__pagamentos = []

    @property
    def clinica(self): 
        return self.__clinica

    @property
    def paciente(self): 
        return self.__paciente

    @property
    def profissional(self): 
        return self.__profissional

    @property
    def data(self): 
        return self.__data

    @property
    def hora_inicio(self): 
        return self.__hora_inicio

    @property
    def hora_fim(self): 
        return self.__hora_fim

    @property
    def tipo(self): 
        return self.__tipo

    @property
    def valor(self): 
        return self.__valor

    @property
    def procedimentos(self):
        return list(self.__procedimentos)

    @property
    def pagamentos(self):
        return list(self.__pagamentos)

    def adicionar_procedimento(self, procedimento:Procedimento):
        self.__procedimentos.append(procedimento)

    @property
    def valor_procedimentos(self) -> Decimal:
        return sum((p.custo for p in self.__procedimentos), Decimal("0.00"))

    @property
    def valor_total(self) -> Decimal:
        return self.__valor + self.valor_procedimentos

    def valor_pago_procedimento(self, procedimento: Procedimento) -> Decimal:
        return sum((p.valor for p in self.__pagamentos
                    if p.procedimento is procedimento), Decimal("0.00"))

    def valor_restante_procedimento(self, procedimento: Procedimento) -> Decimal:
        return procedimento.custo - self.valor_pago_procedimento(procedimento)

    @property
    def valor_pago_atendimento(self) -> Decimal:
        return sum((p.valor for p in self.__pagamentos
                    if p.procedimento is None), Decimal("0.00"))

    @property
    def valor_restante_atendimento(self) -> Decimal:
        return self.__valor - self.valor_pago_atendimento

    @property
    def valor_pago(self) -> Decimal:
        return sum((p.valor for p in self.__pagamentos), Decimal("0.00"))

    @property
    def valor_restante(self) -> Decimal:
        return self.valor_total - self.valor_pago

    @property
    def quitado(self) -> bool:
        return self.valor_restante == 0

    def registrar_pagamento(self, pagamento:Pagamento):
        if pagamento.atendimento is not self:
            raise ErroDeRegra("Pagamento pertence a outro atendimento.")
        if pagamento.paciente is not self.__paciente:
            raise ErroDeRegra("Paciente do pagamento difere do paciente do atendimento.")
        if pagamento.data > self.__data:
            raise ErroDeRegra("Pagamento deve ser feito até a data do atendimento.")
        procedimento = pagamento.procedimento
        if procedimento is None:
            restante = self.valor_restante_atendimento
        else:
            if procedimento not in self.__procedimentos:
                raise ErroDeRegra("Procedimento não pertence a este atendimento.")
            restante = self.valor_restante_procedimento(procedimento)
        if pagamento.valor > restante:
            raise ErroDeRegra(f"Valor excede o restante (R$ {restante}).")
        self.__pagamentos.append(pagamento)

    def __str__(self):
        return (f"{self.data:%d/%m/%Y} {self.hora_inicio:%H:%M}-{self.hora_fim:%H:%M} | "
                f"{self.clinica.nome} | {self.tipo} | {self.paciente.nome} c/ "
                f"{self.profissional.nome} | R$ {self.valor_total}")
