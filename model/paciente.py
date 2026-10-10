from abstractClasses.pessoa import Pessoa
from datetime import date
from utility import ErroDeRegra

class Paciente(Pessoa):
    def __init__(self, nome:str, celular:str, cpf:str, data_nascimento:date) -> None:
        super().__init__(nome, celular, cpf)
        if data_nascimento > date.today():
            raise ErroDeRegra("Data inválida.")
        self.__data_nascimento = data_nascimento
        
    @property
    def nome(self):
        return super().nome

    @property
    def celular(self):
        return super().celular

    @property
    def cpf(self):
        return super().cpf

    def data_nascimento(self):
        return self.__data_nascimento

    def idade(self, data:date) -> int:
        c = self.__data_nascimento
        fez_aniversario = (data.month, data.day) >= (c.month, c.day)
        return data.year - c.year - (0 if fez_aniversario else 1)
    
    def pode_atender_sozinho(self, data:date) -> bool:
        return self.idade(data) >= 18
    