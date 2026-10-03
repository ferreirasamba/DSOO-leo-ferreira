from abstractClasses.abstractTipoAtendimento import TipoAtendimento as AbstractTipoAtendimento

class TipoAtendimento(AbstractTipoAtendimento):
    def __init__(self, tipo_atendimento):
        super().__init__(tipo_atendimento)

    @property
    def tipo_atendimento(self):
        return super().tipo_atendimento

    