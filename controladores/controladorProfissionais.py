from abstractClasses.abstractControladorProfissionais import AbstractControladorProfissionais
from model.profissional import Profissional

class controladorProfissionais(AbstractControladorProfissionais):
    def __init__(self):
        super().__init__()

    @property
    def profissionais(self):
        return super().profissionais

    def registrar_profissional(self, profissional:Profissional):
        self.__profissionais.append(profissional)