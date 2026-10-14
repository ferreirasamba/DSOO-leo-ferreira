from controlador.controlador_sistema import ControladorSistema

if __name__ == "__main__":
    try:
        ControladorSistema().abre_tela()
    except (KeyboardInterrupt, EOFError):
        print("Programa encerrado.")
