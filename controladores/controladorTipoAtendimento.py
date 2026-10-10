from abstractClasses.abstractControladorTipoAtendimento import AbstractControladorTipoAtendimento
from model.tipoAtendimento import TipoAtendimento

class ControladorTipoAtendimento(AbstractControladorTipoAtendimento):
    def __init__(self):
        super().__init__()

    @property
    def tipo_atendimentos_registrados(self):
        return super().tipo_atendimentos_registrados

    def registrar_tipo_atendimento(self, tipo_atendimento:TipoAtendimento):
        self.__tipo_atendimentos_registrados.append(tipo_atendimento)