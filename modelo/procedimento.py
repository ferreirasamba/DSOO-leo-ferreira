from modelo.profissional import Profissional
from utilidades import ErroDeRegra, dinheiro


class Procedimento:
    def __init__(self, descricao: str, 
                       custo, 
                       responsavel: Profissional):
        custo = dinheiro(custo)
        if custo < 0:
            raise ErroDeRegra("Custo não pode ser negativo.")
        self.__descricao = descricao.strip()
        self.__custo = custo
        self.__responsavel = responsavel

    @property
    def descricao(self): 
        return self.__descricao

    @property
    def custo(self): 
        return self.__custo

    @property
    def responsavel(self): 
        return self.__responsavel

    def __str__(self):
        return f"{self.descricao} - R$ {self.custo} (resp.: {self.responsavel.nome})"