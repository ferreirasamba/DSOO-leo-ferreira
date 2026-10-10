from datetime import time
from util import ErroDeRegra

class Clinica:
    def __init__(self, nome:str, cidade:str, descricao:str, aberto:time, fechado:time):
        if aberto >= fechado:
            raise ErroDeRegra("A clínica não pode abrir após o horário de fechamento.")
        self.__nome = nome
        self.__cidade = cidade
        self.__descricao = descricao
        self.__aberto = aberto
        self.__fechado = fechado

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
    def aberto(self):
        return self.__aberto

    @property
    def fechado(self):
        return self.__fechado

    def funciona_em(self, inicio:time, fim:time) -> bool:
        return self.__aberto <= inicio and fim <= self.__fechado

    def __str__(self):
        return f"CLÍNICA: {self.nome} | CIDADE: {self.__cidade}"
    