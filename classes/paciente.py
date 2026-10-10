from abstractClasses.pessoa import Pessoa
from datetime import date
class Paciente(Pessoa):
    def __init__(self, nome, celular, cpf, data_nascimento, responsavel):
        super().__init__(nome, celular, cpf, data_nascimento)
        self.__responsavel = responsavel

    @property
    def nome(self):
        return super().nome

    @property
    def celular(self):
        return super().celular

    @property
    def cpf(self):
        return super().cpf

    @property
    def data_nascimento(self):
        return super().data_nascimento

    def idade(self, data):
        return super().idade(data)

    @property
    def responsavel(self): 
        return self.__responsavel

    def pode_ir_sozinho(self, data:date) -> bool:
        return self.idade(data) >= 18