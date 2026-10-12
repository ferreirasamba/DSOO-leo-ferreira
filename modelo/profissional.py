from datetime import date
from modelo.pessoa import Pessoa
from utilidades import ErroDeRegra

class Profissional(Pessoa):
    def __init__(self, nome:str, 
                       celular:str, 
                       cpf:str, 
                       data_nascimento:date,
                       especialidade:str,
                       registro:str):
        super().__init__(nome, celular, cpf, data_nascimento)
        self.especialidade = especialidade
        self.registro = registro

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, especialidade: str):
        if not especialidade.strip():
            raise ErroDeRegra("Especialidade não pode ser vazia.")
        self.__especialidade = especialidade.strip()

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, registro: str):
        if not registro.strip():
            raise ErroDeRegra("Registro profissional não pode ser vazio.")
        self.__registro = registro.strip()

    def descricao(self):
        return f"{self.nome} - {self.especialidade} ({self.registro})"
