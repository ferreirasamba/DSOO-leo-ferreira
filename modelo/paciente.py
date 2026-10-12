from datetime import date
from modelo.pessoa import Pessoa
from utilidades import ErroDeRegra

class Paciente(Pessoa):
    def __init__(self, nome:str, 
                       celular:str, 
                       cpf:str, 
                       data_nascimento:date):
        super().__init__(nome, celular, cpf, data_nascimento)
        self.__responsavel = None

    @property
    def responsavel(self):
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, responsavel: Pessoa | None):
        if responsavel is not None and not isinstance(responsavel, Pessoa):
            raise ErroDeRegra("Responsável deve ser uma pessoa cadastrada.")
        if responsavel is not None and responsavel.cpf == self.cpf:
            raise ErroDeRegra("O paciente não pode ser responsável por si mesmo.")
        self.__responsavel = responsavel

    def definir_responsavel(self, responsavel:Pessoa):
        self.responsavel = responsavel

    def pode_atender_sozinho(self, data:date) -> bool:
        return self.idade_em(data) >= 18

    def descricao(self):
        return f"{self.nome} (CPF {self.cpf})"
