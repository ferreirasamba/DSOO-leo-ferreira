from abc import ABC, abstractmethod
from utilidades import ErroDeRegra

class AbstractControlador(ABC):
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @abstractmethod
    def abre_tela(self):
        pass

    def executa_menu(self, tela, acoes: dict):
        while True:
            opcao = tela.mostra_menu()
            if opcao == 0:
                return
            try:
                acoes[opcao]()
            except ErroDeRegra as erro:
                tela.mostra_mensagem(f"Não foi possível: {erro}")

    def exige_escolha(self, escolhido):
        if escolhido is None:
            raise ErroDeRegra("Operação cancelada (ou não há itens cadastrados).")
        return escolhido