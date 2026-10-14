from decimal import Decimal, InvalidOperation

class ErroDeRegra(Exception):
    pass

def dinheiro(valor) -> Decimal:
    try:
        return Decimal(str(valor)).quantize(Decimal("0.01"))
    except (InvalidOperation, ValueError):
        raise ErroDeRegra("Valor monetário inválido.") from None

def so_digitos(texto) -> str:
    return "".join(c for c in str(texto) if c.isdigit())
