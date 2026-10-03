from pessoa import Pessoa

class Profissional(Pessoa):
    def __init__(self, nome, celular, cpf, especialidade, registro_profissional):
        super().__init__(nome, celular, cpf)
        self.__especialidade = especialidade
        self.__registro_profissional = registro_profissional

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
    def registro_profissional(self):
        return self.__registro_profissional    