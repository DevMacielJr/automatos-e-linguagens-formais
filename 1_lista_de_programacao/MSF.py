def maquina1():
    print("\n--- Máquina 1 ---")

    ni = 1  # entradas: 0 e 1
    ns = 2  # estados: s0, s1, s2

    TE = [
        [1, 2],  # s0
        [1, 2],  # s1
        [2, 0]   # s2
    ]

    VS = [0, 1, 1]

    estado = 0

    while True:
        entrada = input("Entrada (0,1 ou r): ")

        if entrada == 'r':
            estado = 0
            print("Reset → s0")
            continue

        if entrada not in ['0', '1']:
            print("Entrada inválida")
            continue

        entrada = int(entrada)

        estado = TE[estado][entrada]

        print(f"Estado: s{estado} | Saída: {VS[estado]}")


def maquina2():
    print("\n--- Máquina 2 (detecta dois 1 seguidos) ---")

    ni = 1
    ns = 2

    TE = [
        [0, 1],  # s0
        [0, 2],  # s1
        [2, 2]   # s2 (estado final)
    ]

    VS = [0, 0, 1]

    estado = 0

    while True:
        entrada = input("Entrada (0,1 ou r): ")

        if entrada == 'r':
            estado = 0
            print("Reset → s0")
            continue

        if entrada not in ['0', '1']:
            print("Entrada inválida")
            continue

        entrada = int(entrada)

        estado = TE[estado][entrada]

        print(f"Estado: s{estado} | Saída: {VS[estado]}")

    
while True:
    print("\nEscolha a máquina:")
    print("1 - Máquina do enunciado")
    print("2 - Máquina detectora de '11'")
    print("0 - Sair")

    op = input("Opção: ")

    if op == '1':
        maquina1()
    elif op == '2':
        maquina2()
    elif op == '0':
        break
    else:
        print("Opção inválida")