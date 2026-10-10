from abstractClasses.abstractControladorClinicas import AbstractControladorClinicas
from model.clinica import Clinica

class ControladorClinicas(AbstractControladorClinicas):
    def __init__(self):
        super().__init__()

    @property
    def clinicas(self):
        return super().clinicas

    def registrar_clinica(self, clinica:Clinica):
        self.clinicas.append(clinica)
