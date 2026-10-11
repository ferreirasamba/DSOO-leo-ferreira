from controlador.abstract_controlador import AbstractControlador
from modelo.profissional import Profissional
from utilidades import ErroDeRegra
from visao.tela_profissional import TelaProfissional


class ControladorProfissional(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__profissionais = []
        self.__tela = TelaProfissional()

    @property
    def profissionais(self):
        return list(self.__profissionais)

    def abre_tela(self):
        self.executa_menu(self.__tela, {1: self.cadastrar, 2: self.listar})

    def cadastrar(self):
        d = self.__tela.le_dados_profissional()
        profissional = Profissional(d["nome"], d["celular"], d["cpf"], d["data_nascimento"],
                                    d["especialidade"], d["registro"])
        if any(p.cpf == profissional.cpf for p in self.__profissionais):
            raise ErroDeRegra("Já existe profissional com esse CPF.")
        self.__profissionais.append(profissional)
        self.__tela.mostra_mensagem("Profissional cadastrado!")

    def listar(self):
        self.__tela.mostra_profissionais(self.__profissionais)

    def seleciona(self):
        indice = self.__tela.escolhe_da_lista(
            "Escolha o profissional", [str(p) for p in self.__profissionais])
        return None if indice is None else self.__profissionais[indice]