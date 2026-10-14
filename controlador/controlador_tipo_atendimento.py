from controlador.abstract_controlador import AbstractControlador
from modelo.tipo_atendimento import TipoAtendimento
from utilidades import ErroDeRegra
from visao.tela_tipo_atendimento import TelaTipoAtendimento


class ControladorTipoAtendimento(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tipos = []
        self.__tela = TelaTipoAtendimento()

    @property
    def tipos(self):
        return list(self.__tipos)

    def abre_tela(self):
        self.executa_menu(self.__tela, {
            1: self.cadastrar, 2: self.listar, 3: self.alterar, 4: self.excluir,
        })

    def cadastrar(self):
        tipo = TipoAtendimento(self.__tela.le_nome_tipo())
        if any(t.nome.lower() == tipo.nome.lower() for t in self.__tipos):
            raise ErroDeRegra("Tipo de atendimento já cadastrado.")
        self.__tipos.append(tipo)
        self.__tela.mostra_mensagem("Tipo cadastrado!")

    def listar(self):
        self.__tela.mostra_tipos(self.__tipos)

    def alterar(self):
        tipo = self.exige_escolha(self.seleciona())
        nome = TipoAtendimento(self.__tela.le_nome_tipo()).nome
        if any(t is not tipo and t.nome.lower() == nome.lower() for t in self.__tipos):
            raise ErroDeRegra("Tipo de atendimento já cadastrado.")
        tipo.nome = nome
        self.__tela.mostra_mensagem("Tipo de atendimento alterado!")

    def excluir(self):
        tipo = self.exige_escolha(self.seleciona())
        atendimentos = self.controlador_sistema.controlador_atendimento.atendimentos
        if any(a.tipo is tipo for a in atendimentos):
            raise ErroDeRegra("Não é possível excluir um tipo vinculado a atendimentos.")
        if self.__tela.confirma_acao(f"Excluir o tipo {tipo.nome}?"):
            self.__tipos.remove(tipo)
            self.__tela.mostra_mensagem("Tipo de atendimento excluído!")

    def seleciona(self):
        indice = self.__tela.escolhe_da_lista("Escolha o tipo", [t.nome for t in self.__tipos])
        return None if indice is None else self.__tipos[indice]
