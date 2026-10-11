from datetime import date
from modelo.pessoa import Pessoa
from utilidades import ErroDeRegra

class Paciente(Pessoa):
    def __init__(self, nome:str, 
                       celular:str, 
                       cpf:str, 
                       data_nascimento:str):
        super().__init__(nome, celular, cpf, data_nascimento)
        self.__responsavel = None

    @property
    def responsavel(self):
        return self.__responsavel

    def definir_responsavel(self, responsavel:Pessoa):
        if responsavel.cpf == self.cpf:
            raise ErroDeRegra("O paciente não pode ser responsável por si mesmo.")
        self.__responsavel = responsavel

    def pode_atender_sozinho(self, data:date) -> bool:
        return self.idade_em(data) >= 18

    def descricao(self):
        return f"{self.nome} (CPF {self.cpf})"