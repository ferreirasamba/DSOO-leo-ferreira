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
        self.executa_menu(self.__tela, {
            1: self.cadastrar, 2: self.listar, 3: self.alterar, 4: self.excluir,
        })

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

    def alterar(self):
        paciente = self.exige_escolha(self.seleciona())
        dados = self.__tela.le_dados_paciente()
        atualizado = Paciente(dados["nome"], dados["celular"], dados["cpf"],
                              dados["data_nascimento"])
        if any(p is not paciente and p.cpf == atualizado.cpf for p in self.__pacientes):
            raise ErroDeRegra("Já existe paciente com esse CPF.")
        responsavel = paciente.responsavel
        if not atualizado.pode_atender_sozinho(date.today()):
            if responsavel is None or not responsavel.pode_atender_sozinho(date.today()):
                self.__tela.mostra_mensagem("Paciente menor de 18 anos: informe o responsável.")
                responsavel = self.__escolhe_responsavel()
            if responsavel is not None:
                atualizado.definir_responsavel(responsavel)
        atendimentos = self.controlador_sistema.controlador_atendimento.atendimentos
        if any(a.paciente is paciente and not atualizado.pode_atender_sozinho(a.data)
               and (atualizado.responsavel is None
                    or atualizado.responsavel.idade_em(a.data) < 18)
               for a in atendimentos):
            raise ErroDeRegra("A alteração deixaria um atendimento sem responsável maior de idade.")
        paciente.nome = atualizado.nome
        paciente.celular = atualizado.celular
        paciente.cpf = atualizado.cpf
        paciente.data_nascimento = atualizado.data_nascimento
        paciente.responsavel = atualizado.responsavel
        self.__tela.mostra_mensagem("Paciente alterado!")

    def excluir(self):
        paciente = self.exige_escolha(self.seleciona())
        atendimentos = self.controlador_sistema.controlador_atendimento.atendimentos
        if any(a.paciente is paciente for a in atendimentos):
            raise ErroDeRegra("Não é possível excluir um paciente vinculado a atendimentos.")
        if any(p.responsavel is paciente for p in self.__pacientes):
            raise ErroDeRegra("Não é possível excluir uma pessoa responsável por pacientes.")
        if self.__tela.confirma_acao(f"Excluir o paciente {paciente.nome}?"):
            self.__pacientes.remove(paciente)
            self.__tela.mostra_mensagem("Paciente excluído!")

    def seleciona(self):
        indice = self.__tela.escolhe_da_lista("Escolha o paciente", [str(p) for p in self.__pacientes])
        return None if indice is None else self.__pacientes[indice]
