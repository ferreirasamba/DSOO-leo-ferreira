from modelo.pagamento import Pagamento


class PagamentoDinheiro(Pagamento):
    def modalidade(self):
        return "Dinheiro"