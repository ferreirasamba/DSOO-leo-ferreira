from decimal import Decimal

class ErroDeRegra(Exception):
    pass

def so_digito(texto) -> str:
    return "".join(c for c in str(texto) if c.isdigit())

def dinheiro(valor) -> Decimal:
    return Decimal(str(valor)).quantize(Decimal("0.01"))