from collections import Counter
from controlador.abstract_controlador import AbstractControlador
from visao.tela_relatorio import TelaRelatorio


class ControladorRelatorio(AbstractControlador):
    TOP = 3
    def __init__(self, controlador_sistema):
        super().__init__(controlador_sistema)
        self.__tela = TelaRelatorio()

    def abre_tela(self):
        self.executa_menu(self.__tela, {
            1: self.clinicas_com_mais_atendimentos,
            2: self.atendimentos_mais_caros,
            3: self.atendimentos_mais_baratos,
            4: self.procedimentos_mais_realizados,
            5: self.procedimentos_mais_caros,
            6: self.procedimentos_mais_baratos,
        })
    
    def __atendimentos(self):
        return self.controlador_sistema.controlador_atendimento.atendimentos

    def __procedimentos(self):
        return [p for a in self.__atendimentos() for p in a.procedimentos]
    
    def clinicas_com_mais_atendimentos(self):
        contagem = Counter(a.clinica for a in self.__atendimentos())
        self.__tela.mostra_ranking_clinicas(contagem.most_common(self.TOP))

    def atendimentos_mais_caros(self):
        ordenados = sorted(self.__atendimentos(), key=lambda a: a.valor_total, reverse=True)
        self.__tela.mostra_atendimentos("Atendimentos mais caros", ordenados[:self.TOP])

    def atendimentos_mais_baratos(self):
        ordenados = sorted(self.__atendimentos(), key=lambda a: a.valor_total)
        self.__tela.mostra_atendimentos("Atendimentos mais baratos", ordenados[:self.TOP])

    def procedimentos_mais_realizados(self):
        contagem = Counter(p.descricao.lower() for p in self.__procedimentos())
        self.__tela.mostra_ranking_procedimentos(contagem.most_common(self.TOP))

    def procedimentos_mais_caros(self):
        ordenados = sorted(self.__procedimentos(), key=lambda p: p.custo, reverse=True)
        self.__tela.mostra_procedimentos("Procedimentos mais caros", ordenados[:self.TOP])

    def procedimentos_mais_baratos(self):
        ordenados = sorted(self.__procedimentos(), key=lambda p: p.custo)
        self.__tela.mostra_procedimentos("Procedimentos mais baratos", ordenados[:self.TOP])
