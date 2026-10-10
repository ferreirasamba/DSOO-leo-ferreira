class tipoAtendimento:
    def __init__(self, tipo_atendimento:str):
        self.__tipo_atendimento = tipo_atendimento.strip()

    @property
    def tipo_atendimento(self):
        return self.__tipo_atendimento

    def __str__(self):
        return self.tipo_atendimento