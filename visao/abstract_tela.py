from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal, InvalidOperation

class AbstractTela(ABC):

    @abstractmethod
    def mostra_menu(self) -> int:
        pass

    def mostra_titulo(self, titulo:str):
        print(f"\n===== {titulo} =====")

    def mostra_mensagem(self, texto:str):
        print(f"\n>> {texto}")

    def mostra_lista(self, titulo:str, linhas:list):
        self.mostra_titulo(titulo)
        if not linhas:
            print("(nenhum registro)")
        for i, linha in enumerate(linhas, 1):
            print(f"{i}) {linha}")

    def le_texto(self, mensagem:str) -> str:
        while True:
            valor = input(mensagem).strip()
            if valor:
                return valor
            print("Valor vazio, tente novamente.")

    def confirma_acao(self, mensagem: str) -> bool:
        while True:
            resposta = input(f"{mensagem} [s/N]: ").strip().lower()
            if resposta in ("s", "sim"):
                return True
            if resposta in ("", "n", "nao", "não"):
                return False
            print("Responda com s ou n.")

    def le_inteiro(self, mensagem:str, validos=None) -> int:
        while True:
            try:
                numero = int(input(mensagem))
            except ValueError:
                print("Digite um número inteiro.")
                continue
            if validos is None or numero in validos:
                return numero
            print("Opção inválida.")

    def le_decimal(self, mensagem:str) -> Decimal:
        while True:
            entrada = input(mensagem).strip().replace(",", ".")
            if "e" in entrada.lower():
                print("Notação científica não permitida.")
                continue
            try:
                valor = Decimal(entrada)
            except InvalidOperation:
                print("Digite um valor numérico (ex.: 150,50).")
                continue
            if valor.is_finite() and Decimal("0") <= valor <= Decimal("1000000000"):
                return valor
            if valor > Decimal("1000000000"):
                print("Valor máximo permitido: R$ 1.000.000.000,00.")
            else:
                print("Valor inválido.")

    def le_data(self, mensagem:str):
        while True:
            try:
                return datetime.strptime(input(mensagem).strip(), "%d/%m/%Y").date()
            except ValueError:
                print("Data inválida. Use dd/mm/aaaa (ex.: 20/11/2026).")

    def le_hora(self, mensagem:str):
        while True:
            try:
                return datetime.strptime(input(mensagem).strip(), "%H:%M").time()
            except ValueError:
                print("Hora inválida. Use HH:MM (ex.: 14:30).")

    def le_opcao_menu(self, titulo:str, opcoes:list, rotulo_zero:str = "Voltar") -> int:
        self.mostra_titulo(titulo)
        for i, opcao in enumerate(opcoes, 1):
            print(f"{i} - {opcao}")
        print(f"0 - {rotulo_zero}")
        return self.le_inteiro("Escolha: ", range(0, len(opcoes) + 1))

    def escolhe_da_lista(self, titulo:str, linhas:list):
        if not linhas:
            self.mostra_mensagem("Nenhum item disponível para escolher.")
            return None
        self.mostra_lista(titulo, linhas)
        escolha = self.le_inteiro("Número (0 para cancelar): ", range(0, len(linhas) + 1))
        return None if escolha == 0 else escolha - 1
