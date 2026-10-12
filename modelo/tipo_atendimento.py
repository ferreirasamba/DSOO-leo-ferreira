from utilidades import ErroDeRegra

class TipoAtendimento:
    def __init__(self, nome: str):
        self.nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        nome = nome.strip()
        if not nome:
            raise ErroDeRegra("Nome do tipo de atendimento não pode ser vazio.")
        self.__nome = nome

    def __str__(self):
        return self.nome
