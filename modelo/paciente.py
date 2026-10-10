from modelo.pessoa import Pessoa
from datetime import date
from util import ErroDeRegra

class Paciente(Pessoa):
    def __init__(self, nome, celular, cpf, data_nascimento):
        super().__init__(nome, celular, cpf, data_nascimento)
        self.__responsavel = None

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

    def definir_responsavel(self, responsavel: Pessoa):
        if responsavel.__cpf == self.__cpf:
            raise ErroDeRegra("Responsável não pode ser o próprio paciente.")
        self.__responsavel = responsavel

    def pode_ir_sozinho(self, data:date) -> bool:
        return self.idade(data) >= 18

    def descricao(self):
        return f"NOME: {self.nome} | CPF: {self.cpf}"