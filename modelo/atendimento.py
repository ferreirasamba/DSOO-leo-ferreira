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

    @clinica.setter
    def clinica(self, clinica: Clinica):
        if not isinstance(clinica, Clinica):
            raise ErroDeRegra("Clínica inválida.")
        if not clinica.funciona_em(self.__hora_inicio, self.__hora_fim):
            raise ErroDeRegra("Horário do atendimento fica fora do funcionamento da clínica.")
        self.__clinica = clinica

    @property
    def paciente(self): 
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente: Paciente):
        if not isinstance(paciente, Paciente):
            raise ErroDeRegra("Paciente inválido.")
        if not paciente.pode_atender_sozinho(self.__data):
            responsavel = paciente.responsavel
            if responsavel is None or responsavel.idade_em(self.__data) < 18:
                raise ErroDeRegra("Paciente menor de 18 anos precisa de responsável maior de idade.")
        if any(p.paciente is not paciente for p in self.__pagamentos):
            raise ErroDeRegra("Não é possível trocar o paciente após registrar pagamentos.")
        self.__paciente = paciente

    @property
    def profissional(self): 
        return self.__profissional

    @profissional.setter
    def profissional(self, profissional: Profissional):
        if not isinstance(profissional, Profissional):
            raise ErroDeRegra("Profissional inválido.")
        self.__profissional = profissional

    @property
    def data(self): 
        return self.__data

    @data.setter
    def data(self, data: date):
        if data < date.today():
            raise ErroDeRegra("Data do atendimento não pode estar no passado.")
        if not self.__paciente.pode_atender_sozinho(data):
            responsavel = self.__paciente.responsavel
            if responsavel is None or responsavel.idade_em(data) < 18:
                raise ErroDeRegra("Paciente menor de 18 anos precisa de responsável maior de idade.")
        if any(p.data > data for p in self.__pagamentos):
            raise ErroDeRegra("A nova data não pode ser anterior à data de um pagamento registrado.")
        self.__data = data

    @property
    def hora_inicio(self): 
        return self.__hora_inicio

    @hora_inicio.setter
    def hora_inicio(self, hora_inicio: time):
        self._validar_horarios(hora_inicio, self.__hora_fim, self.__clinica)
        self.__hora_inicio = hora_inicio

    @property
    def hora_fim(self): 
        return self.__hora_fim

    @hora_fim.setter
    def hora_fim(self, hora_fim: time):
        self._validar_horarios(self.__hora_inicio, hora_fim, self.__clinica)
        self.__hora_fim = hora_fim

    @property
    def tipo(self): 
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: TipoAtendimento):
        if not isinstance(tipo, TipoAtendimento):
            raise ErroDeRegra("Tipo de atendimento inválido.")
        self.__tipo = tipo

    @property
    def valor(self): 
        return self.__valor

    @valor.setter
    def valor(self, valor):
        valor = dinheiro(valor)
        if valor < 0:
            raise ErroDeRegra("Valor do atendimento não pode ser negativo.")
        valor_pago = sum((p.valor for p in self.__pagamentos if p.procedimento is None),
                         Decimal("0.00"))
        if valor < valor_pago:
            raise ErroDeRegra("O valor não pode ser menor que os pagamentos já registrados.")
        self.__valor = valor

    @property
    def procedimentos(self):
        return list(self.__procedimentos)

    @property
    def pagamentos(self):
        return list(self.__pagamentos)

    def adicionar_procedimento(self, procedimento:Procedimento):
        self.__procedimentos.append(procedimento)

    @staticmethod
    def _validar_horarios(inicio: time, fim: time, clinica: Clinica):
        if inicio >= fim:
            raise ErroDeRegra("Horário de início deve ser antes do fim.")
        if not clinica.funciona_em(inicio, fim):
            raise ErroDeRegra("Horário do atendimento fica fora do funcionamento da clínica.")

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

    def _validar_pagamento(self, pagamento, data, paciente, valor, procedimento):
        if paciente is not self.__paciente:
            raise ErroDeRegra("Paciente do pagamento difere do paciente do atendimento.")
        if data > self.__data:
            raise ErroDeRegra("Pagamento deve ser feito até a data do atendimento.")
        if procedimento is None:
            limite = self.__valor
        else:
            if procedimento not in self.__procedimentos:
                raise ErroDeRegra("Procedimento não pertence a este atendimento.")
            limite = procedimento.custo
        valor_ja_pago = sum((p.valor for p in self.__pagamentos
                             if p is not pagamento and p.procedimento is procedimento),
                            Decimal("0.00"))
        restante = limite - valor_ja_pago
        if valor > restante:
            raise ErroDeRegra(f"Valor excede o restante (R$ {restante}).")

    def registrar_pagamento(self, pagamento:Pagamento):
        if pagamento.atendimento is not self:
            raise ErroDeRegra("Pagamento pertence a outro atendimento.")
        if pagamento in self.__pagamentos:
            raise ErroDeRegra("Pagamento já registrado neste atendimento.")
        self._validar_pagamento(pagamento, pagamento.data, pagamento.paciente,
                                pagamento.valor, pagamento.procedimento)
        self.__pagamentos.append(pagamento)

    def __str__(self):
        return (f"{self.data:%d/%m/%Y} {self.hora_inicio:%H:%M}-{self.hora_fim:%H:%M} | "
                f"{self.clinica.nome} | {self.tipo} | {self.paciente.nome} c/ "
                f"{self.profissional.nome} | R$ {self.valor_total}")
