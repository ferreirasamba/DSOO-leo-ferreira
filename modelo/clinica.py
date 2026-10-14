from datetime import time
from utilidades import ErroDeRegra

class Clinica:
    def __init__(self, nome:str, 
                       cidade:str, 
                       descricao:str, 
                       abertura:time, 
                       fechamento:time):
        if abertura >= fechamento:
            raise ErroDeRegra("Abertura deve ser antes do fechamento.")
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        self.__abertura = abertura
        self.__fechamento = fechamento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, cidade: str):
        self.__cidade = cidade

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def abertura(self):
        return self.__abertura

    @abertura.setter
    def abertura(self, abertura: time):
        if abertura >= self.__fechamento:
            raise ErroDeRegra("Abertura deve ser antes do fechamento.")
        self.__abertura = abertura

    @property
    def fechamento(self):
        return self.__fechamento

    @fechamento.setter
    def fechamento(self, fechamento: time):
        if self.__abertura >= fechamento:
            raise ErroDeRegra("Fechamento deve ser depois da abertura.")
        self.__fechamento = fechamento

    def funciona_em(self, inicio:time, fim:time) -> bool:
        return self.__abertura <= inicio and fim <= self.__fechamento

    def atualizar(self, nome: str, cidade: str, descricao: str,
                  abertura: time, fechamento: time):
        if abertura >= fechamento:
            raise ErroDeRegra("Abertura deve ser antes do fechamento.")
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        self.__abertura = abertura
        self.__fechamento = fechamento

    def __str__(self):
        return f"{self.nome} ({self.cidade})"
