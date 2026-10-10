from abstractClasses.abstractTipoAtendimento import AbstractTipoAtendimento

class TipoAtendimento(AbstractTipoAtendimento):
    def __init__(self, tipo_atendimento:str):
        super().__init__(tipo_atendimento)

    @property
    def tipo_atendimento(self):
        return super().tipo_atendimento