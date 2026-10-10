from abstractClasses.abstractAtendimento import Atendimento as AbstractAtendimento
from clinica import Clinica
from paciente import Paciente
from profissional import Profissional
from tipoAtendimento import TipoAtendimento
from datetime import date as Date

class Atendimento(AbstractAtendimento):
    def __init__(self, clinica: Clinica, 
                       paciente:Paciente, 
                       profissional:Profissional, 
                       data:Date, 
                       horario_inicio:str, 
                       horario_fim:str, 
                       tipo_atendimento:TipoAtendimento, 
                       valor:float) -> None:
        
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

    @property
    def procedimentos(self):
        return super().procedimentos
    