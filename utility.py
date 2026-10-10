class ErroDeRegra(Exception):
    pass

def cpf_valido(cpf) -> str:
    return "".join(c for c in str(cpf) if c.isdigit(cpf))
