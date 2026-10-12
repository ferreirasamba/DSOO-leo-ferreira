from modelo.profissional import Profissional
from utilidades import ErroDeRegra, dinheiro


class Procedimento:
    def __init__(self, descricao: str, 
                       custo, 
                       responsavel: Profissional):
        custo = dinheiro(custo)
        if custo < 0:
            raise ErroDeRegra("Custo não pode ser negativo.")
        self.descricao = descricao
        self.custo = custo
        self.responsavel = responsavel

    @property
    def descricao(self): 
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        descricao = descricao.strip()
        if not descricao:
            raise ErroDeRegra("Descrição do procedimento não pode ser vazia.")
        self.__descricao = descricao

    @property
    def custo(self): 
        return self.__custo

    @custo.setter
    def custo(self, custo):
        custo = dinheiro(custo)
        if custo < 0:
            raise ErroDeRegra("Custo não pode ser negativo.")
        self.__custo = custo

    @property
    def responsavel(self): 
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, responsavel: Profissional):
        if not isinstance(responsavel, Profissional):
            raise ErroDeRegra("Responsável pelo procedimento deve ser um profissional.")
        self.__responsavel = responsavel

    def __str__(self):
        return f"{self.descricao} - R$ {self.custo} (resp.: {self.responsavel.nome})"
