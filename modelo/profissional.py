from datetime import date
from modelo.pessoa import Pessoa

class Profissional(Pessoa):
    def __init__(self, nome:str, 
                       celular:str, 
                       cpf:str, 
                       data_nascimento:date,
                       especialidade:str,
                       registro:str):
        super().__init__(nome, celular, cpf, data_nascimento)
        self.__especialidade = especialidade
        self.__registro = registro

    @property
    def especialidade(self):
        return self.__especialidade

    @property
    def registro(self):
        return self.__registro

    def descricao(self):
        return f"{self.nome} - {self.especialidade} ({self.registro})"