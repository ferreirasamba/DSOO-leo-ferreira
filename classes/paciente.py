from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, celular, pdf):
        super().__init__(nome, celular, pdf)

    @property
    def nome(self):
        return super().nome

    @property
    def celular(self):
        return super().celular

    @property
    def pdf(self):
        return super().pdf