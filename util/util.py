def so_digito(texto) -> str:
    return "".join(c for c in str(texto) if c.isdigit())