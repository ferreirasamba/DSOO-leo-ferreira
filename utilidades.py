from decimal import Decimal

class ErroDeRegra(Exception):
    pass

def dinheiro(valor) -> Decimal:
    return Decimal(str(valor)).quantize(Decimal("0.01"))

def so_digitos(texto) -> str:
    return "".join(c for c in str(texto) if c.isdigit())