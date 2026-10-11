from datetime import date
from controlador.abstract_controlador import AbstractControlador
from modelo.paciente import Paciente
from utilidades import ErroDeRegra
from visao.tela_paciente import TelaPaciente


class ControladorPaciente(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__pacientes = []
        self.__tela = TelaPaciente()

    @property
    def pacientes(self):
        return list(self.__pacientes)

    def abre_tela(self):
        self.executa_menu(self.__tela, {1: self.cadastrar, 2: self.listar})

    def cadastrar(self):
        dados = self.__tela.le_dados_paciente()
        paciente = Paciente(dados["nome"], dados["celular"], dados["cpf"], dados["data_nascimento"])

        if any(p.cpf == paciente.cpf for p in self.__pacientes):
            raise ErroDeRegra("Já existe paciente com esse CPF.")

        if not paciente.pode_atender_sozinho(date.today()):
            self.__tela.mostra_mensagem("Paciente menor de 18 anos: informe o responsável.")
            responsavel = self.__escolhe_responsavel()
            if responsavel is not None:
                paciente.definir_responsavel(responsavel)

        self.__pacientes.append(paciente)
        self.__tela.mostra_mensagem("Paciente cadastrado!")

    def __escolhe_responsavel(self):
        adultos = [p for p in self.__pacientes if p.pode_atender_sozinho(date.today())]
        indice = self.__tela.escolhe_da_lista(
            "Responsável (0 = sem responsável por enquanto)", [str(p) for p in adultos])
        return None if indice is None else adultos[indice]

    def listar(self):
        self.__tela.mostra_pacientes(self.__pacientes)

    def seleciona(self):
        indice = self.__tela.escolhe_da_lista("Escolha o paciente", [str(p) for p in self.__pacientes])
        return None if indice is None else self.__pacientes[indice]