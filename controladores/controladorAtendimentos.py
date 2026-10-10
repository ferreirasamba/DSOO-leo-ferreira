from abstractClasses.abstractControladorAtendimento import AbstractControladorAtendimento
from model.paciente import Paciente
from model.atendimento import Atendimento
from utility import ErroDeRegra

class ControladorAtendimento(AbstractControladorAtendimento):
    def __init__(self):
        super().__init__()

    @property
    def atendimentos(self):
        return super().atendimentos

    def registrar_atendimentos(self, atendimento: Atendimento):
        idade = atendimento.paciente.idade(atendimento.data)
        if idade < 18:
            raise ErroDeRegra("Não pode registrar atendimento sendo menor de idade.")
        else:
            self.__atendimentos.append(atendimento)