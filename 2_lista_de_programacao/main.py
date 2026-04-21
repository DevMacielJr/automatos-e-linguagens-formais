from fsm_numero import FSMNumero

while True:
    entrada = input("Número (ou 's' para sair): ")

    if entrada.lower() == 's':
        break

    try:
        numero = int(entrada)

        if not (0 <= numero <= 999999):
            raise ValueError

        idioma = input("Idioma (pt/en): ")

        fsm = FSMNumero(numero, idioma)
        print("Resultado:", fsm.processar())

    except:
        print("Entrada inválida\n")