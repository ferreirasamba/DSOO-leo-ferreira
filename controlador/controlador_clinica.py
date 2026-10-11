from controlador.abstract_controlador import AbstractControlador
from modelo.clinica import Clinica
from visao.tela_clinica import TelaClinica


class ControladorClinica(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__clinicas = []
        self.__tela = TelaClinica()

    @property
    def clinicas(self):
        return list(self.__clinicas)

    def abre_tela(self):
        self.executa_menu(self.__tela, {1: self.cadastrar, 2: self.listar})

    def cadastrar(self):
        dados = self.__tela.le_dados_clinica()
        clinica = Clinica(dados["nome"], dados["cidade"], dados["descricao"],
                          dados["abertura"], dados["fechamento"])
        self.__clinicas.append(clinica)
        self.__tela.mostra_mensagem("Clínica cadastrada!")

    def listar(self):
        self.__tela.mostra_clinicas(self.__clinicas)

    def seleciona(self):
        indice = self.__tela.escolhe_da_lista("Escolha a clínica", [str(c) for c in self.__clinicas])
        return None if indice is None else self.__clinicas[indice]