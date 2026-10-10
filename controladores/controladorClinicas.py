from abstractClasses.abstractControladoresClinicas import AbstractControladorClinicas
from model.clinica import Clinica

class ControladorClinicas(AbstractControladorClinicas):
    def __init__(self):
        super().__init__()

    def registrar_clinica(self, clinica:Clinica):
        self.clinicas.append(clinica)
