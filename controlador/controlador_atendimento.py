from controlador.abstract_controlador import AbstractControlador
from modelo.atendimento import Atendimento
from modelo.procedimento import Procedimento
from utilidades import ErroDeRegra
from visao.tela_atendimento import TelaAtendimento


class ControladorAtendimento(AbstractControlador):
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__atendimentos = []
        self.__tela = TelaAtendimento()

    @property
    def atendimentos(self):
        return list(self.__atendimentos)

    def abre_tela(self):
        self.executa_menu(self.__tela, {
            1: self.agendar,
            2: self.registrar_procedimento,
            3: self.listar,
            4: self.detalhar,
            5: self.alterar,
            6: self.excluir,
            7: self.alterar_procedimento,
            8: self.excluir_procedimento,
            9: self.listar_procedimentos,
        })

    def agendar(self):
        sistema = self.controlador_sistema
        clinica = self.exige_escolha(sistema.controlador_clinica.seleciona())
        paciente = self.exige_escolha(sistema.controlador_paciente.seleciona())
        profissional = self.exige_escolha(sistema.controlador_profissional.seleciona())
        tipo = self.exige_escolha(sistema.controlador_tipo_atendimento.seleciona())
        d = self.__tela.le_dados_agendamento()
        novo = Atendimento(clinica, paciente, profissional, d["data"],
                           d["inicio"], d["fim"], tipo, d["valor"])
        self.__verifica_conflitos(novo.profissional, novo.paciente, novo.data,
                                  novo.hora_inicio, novo.hora_fim)
        self.__atendimentos.append(novo)
        self.__tela.mostra_mensagem("Atendimento agendado!")

    def __verifica_conflitos(self, profissional, paciente, data, inicio, fim,
                             ignorar=None):
        for atendimento in self.__atendimentos:
            if atendimento is ignorar:
                continue
            erro = atendimento.conflita_com(profissional, paciente, data, inicio, fim)
            if erro is not None:
                raise ErroDeRegra(erro)

    def registrar_procedimento(self):
        atendimento = self.exige_escolha(self.seleciona())
        responsavel = self.exige_escolha(
            self.controlador_sistema.controlador_profissional.seleciona())
        d = self.__tela.le_dados_procedimento()
        atendimento.adicionar_procedimento(Procedimento(d["descricao"], d["custo"], responsavel))
        self.__tela.mostra_mensagem("Procedimento registrado!")

    def listar(self):
        self.__tela.mostra_atendimentos(self.__atendimentos)

    def listar_procedimentos(self):
        linhas = []
        for atendimento in self.__atendimentos:
            for procedimento in atendimento.procedimentos:
                pago = atendimento.valor_pago_procedimento(procedimento)
                restante = atendimento.valor_restante_procedimento(procedimento)
                linhas.append(
                    f"{atendimento} -> {procedimento} | Pago: R$ {pago} "
                    f"| Restante: R$ {restante}"
                )
        self.__tela.mostra_procedimentos(linhas)

    def alterar(self):
        atendimento = self.exige_escolha(self.seleciona())
        sistema = self.controlador_sistema
        clinica = self.exige_escolha(sistema.controlador_clinica.seleciona())
        paciente = self.exige_escolha(sistema.controlador_paciente.seleciona())
        profissional = self.exige_escolha(sistema.controlador_profissional.seleciona())
        tipo = self.exige_escolha(sistema.controlador_tipo_atendimento.seleciona())
        d = self.__tela.le_dados_edicao_atendimento()
        self.__verifica_conflitos(profissional, paciente, d["data"], d["inicio"],
                                  d["fim"], ignorar=atendimento)
        atendimento.atualizar(clinica, paciente, profissional, d["data"],
                              d["inicio"], d["fim"], tipo, d["valor"])
        self.__tela.mostra_mensagem("Atendimento alterado!")

    def excluir(self):
        atendimento = self.exige_escolha(self.seleciona())
        if self.__tela.confirma_acao(
                "Excluir este atendimento e seus procedimentos e pagamentos?"):
            self.__atendimentos.remove(atendimento)
            self.__tela.mostra_mensagem("Atendimento excluído!")

    def alterar_procedimento(self):
        atendimento = self.exige_escolha(self.seleciona())
        procedimento = self.exige_escolha(self.__tela.seleciona_procedimento(atendimento))
        responsavel = self.exige_escolha(
            self.controlador_sistema.controlador_profissional.seleciona())
        d = self.__tela.le_dados_edicao_procedimento()
        if d["custo"] < atendimento.valor_pago_procedimento(procedimento):
            raise ErroDeRegra("O custo não pode ser menor que os pagamentos já registrados.")
        procedimento.descricao = d["descricao"]
        procedimento.custo = d["custo"]
        procedimento.responsavel = responsavel
        self.__tela.mostra_mensagem("Procedimento alterado!")

    def excluir_procedimento(self):
        atendimento = self.exige_escolha(self.seleciona())
        procedimento = self.exige_escolha(self.__tela.seleciona_procedimento(atendimento))
        if self.__tela.confirma_acao(f"Excluir o procedimento {procedimento.descricao}?"):
            atendimento.remover_procedimento(procedimento)
            self.__tela.mostra_mensagem("Procedimento excluído!")

    def detalhar(self):
        atendimento = self.exige_escolha(self.seleciona())
        self.__tela.mostra_detalhes(atendimento)

    def seleciona(self):
        indice = self.__tela.escolhe_da_lista(
            "Escolha o atendimento", [str(a) for a in self.__atendimentos])
        return None if indice is None else self.__atendimentos[indice]
