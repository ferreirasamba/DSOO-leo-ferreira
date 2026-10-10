from modelo.pessoa import Pessoa
from datetime import date

class Profissional(Pessoa):
    def __init__(self, nome:str, celular:str, cpf:str, data_nascimento:date, especialidade:str, registro:str):
        super().__init__(nome, celular, cpf, data_nascimento)
        self.__especialidade = especialidade
        self.__registro = registro

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
    def especialidade(self):
        return self.__especialidade

    @property
    def registro(self):
        return self.__registro

    def descricao(self):
        return f"NOME: {self.nome} | ESPECIALIDADE: {self.especialidade} | REGISTRO: {self.registro}"