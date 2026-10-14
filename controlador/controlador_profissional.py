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
        self.executa_menu(self.__tela, {
            1: self.cadastrar, 2: self.listar, 3: self.alterar, 4: self.excluir,
        })

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

    def alterar(self):
        profissional = self.exige_escolha(self.seleciona())
        d = self.__tela.le_dados_profissional()
        atualizado = Profissional(d["nome"], d["celular"], d["cpf"], d["data_nascimento"],
                                  d["especialidade"], d["registro"])
        if any(p is not profissional and p.cpf == atualizado.cpf for p in self.__profissionais):
            raise ErroDeRegra("Já existe profissional com esse CPF.")
        profissional.nome = atualizado.nome
        profissional.celular = atualizado.celular
        profissional.cpf = atualizado.cpf
        profissional.data_nascimento = atualizado.data_nascimento
        profissional.especialidade = atualizado.especialidade
        profissional.registro = atualizado.registro
        self.__tela.mostra_mensagem("Profissional alterado!")

    def excluir(self):
        profissional = self.exige_escolha(self.seleciona())
        atendimentos = self.controlador_sistema.controlador_atendimento.atendimentos
        if any(a.profissional is profissional
               or any(p.responsavel is profissional for p in a.procedimentos)
               for a in atendimentos):
            raise ErroDeRegra("Não é possível excluir um profissional vinculado a atendimentos ou procedimentos.")
        if any(p.responsavel is profissional
               for p in self.controlador_sistema.controlador_paciente.pacientes):
            raise ErroDeRegra("Não é possível excluir um profissional responsável por pacientes.")
        if self.__tela.confirma_acao(f"Excluir o profissional {profissional.nome}?"):
            self.__profissionais.remove(profissional)
            self.__tela.mostra_mensagem("Profissional excluído!")

    def seleciona(self):
        indice = self.__tela.escolhe_da_lista(
            "Escolha o profissional", [str(p) for p in self.__profissionais])
        return None if indice is None else self.__profissionais[indice]
