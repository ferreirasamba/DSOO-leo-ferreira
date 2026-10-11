class TipoAtendimento:
    def __init__(self, nome: str):
        self.__nome = nome.strip()

    @property
    def nome(self): return self.__nome

    def __str__(self):
        return self.nome