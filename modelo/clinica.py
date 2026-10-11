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

    @property
    def cidade(self):
        return self.__cidade

    @property
    def descricao(self):
        return self.__descricao

    @property
    def abertura(self):
        return self.__abertura

    @property
    def fechamento(self):
        return self.__fechamento

    def funciona_em(self, inicio:time, fim:time) -> bool:
        return self.__abertura <= inicio and fim <= self.__fechamento

    def __str__(self):
        return f"{self.nome} ({self.cidade})"