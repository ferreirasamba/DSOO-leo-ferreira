from abstractClasses.abstractAtendimento import AbstractAtendimento
from model.clinica import Clinica
from model.paciente import Paciente
from model.profissional import Profissional
from datetime import date
from datetime import time
from model.tipoAtendimento import TipoAtendimento


class Atendimento(AbstractAtendimento):
    def __init__(self, clinica:Clinica, 
                       paciente:Paciente, 
                       profissional:Profissional, 
                       data:date, 
                       horario_inicio:time, 
                       horario_fim:time, 
                       tipo_atendimento:TipoAtendimento, 
                       valor):
        super().__init__(clinica, paciente, profissional, data, horario_inicio, horario_fim, tipo_atendimento, valor)

    @property
    def clinica(self):
        return super().clinica

    @property
    def paciente(self):
        return super().paciente

    @property
    def profissional(self):
        return super().profissional

    @property
    def data(self):
        return super().data

    @property
    def horario_inicio(self):
        return super().horario_inicio

    @property
    def horario_fim(self):
        return super().horario_fim

    @property
    def tipo_atendimento(self):
        return super().tipo_atendimento

    @property
    def valor(self):
        return super().valor