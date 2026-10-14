from controlador.abstract_controlador import AbstractControlador
from modelo.clinica import Clinica
from utilidades import ErroDeRegra
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
        self.executa_menu(self.__tela, {
            1: self.cadastrar, 2: self.listar, 3: self.alterar, 4: self.excluir,
        })

    def cadastrar(self):
        dados = self.__tela.le_dados_clinica()
        clinica = Clinica(dados["nome"], dados["cidade"], dados["descricao"],
                          dados["abertura"], dados["fechamento"])
        self.__clinicas.append(clinica)
        self.__tela.mostra_mensagem("Clínica cadastrada!")

    def listar(self):
        self.__tela.mostra_clinicas(self.__clinicas)

    def alterar(self):
        clinica = self.exige_escolha(self.seleciona())
        d = self.__tela.le_dados_clinica()
        atendimentos = [a for a in self.controlador_sistema.controlador_atendimento.atendimentos
                        if a.clinica is clinica]
        if any(d["abertura"] > a.hora_inicio or d["fechamento"] < a.hora_fim
               for a in atendimentos):
            raise ErroDeRegra("O novo horário da clínica não pode excluir horários já agendados.")
        clinica.atualizar(d["nome"], d["cidade"], d["descricao"],
                          d["abertura"], d["fechamento"])
        self.__tela.mostra_mensagem("Clínica alterada!")

    def excluir(self):
        clinica = self.exige_escolha(self.seleciona())
        atendimentos = self.controlador_sistema.controlador_atendimento.atendimentos
        if any(a.clinica is clinica for a in atendimentos):
            raise ErroDeRegra("Não é possível excluir uma clínica vinculada a atendimentos.")
        if self.__tela.confirma_acao(f"Excluir a clínica {clinica.nome}?"):
            self.__clinicas.remove(clinica)
            self.__tela.mostra_mensagem("Clínica excluída!")

    def seleciona(self):
        indice = self.__tela.escolhe_da_lista("Escolha a clínica", [str(c) for c in self.__clinicas])
        return None if indice is None else self.__clinicas[indice]
