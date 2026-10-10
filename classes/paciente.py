from abstractClasses.abstractPessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, celular, cpf):
        super().__init__(nome, celular, cpf)

    @property
    def nome(self):
        return super().nome

    @property
    def celular(self):
        return super().celular

    @property
    def cpf(self):
        return super().cpf