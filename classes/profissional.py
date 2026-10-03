from pessoa import Pessoa

class Profissional(Pessoa):
    def __init__(self, nome, celular, pdf, especialidade, registro_profissional):
        super().__init__(nome, celular, pdf)
        self.__especialidade = especialidade
        self.__registro_profissional = registro_profissional

    @property
    def nome(self):
        return super().nome

    @property
    def celular(self):
        return super().celular

    @property
    def pdf(self):
        return super().pdf

    @property
    def especialidade(self):
        return self.__especialidade

    @property
    def registro_profissional(self):
        return self.__registro_profissional    