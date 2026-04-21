import tkinter as tk
from fsm_numero import FSMNumero

def converter():
    entrada = entry.get()
    idioma = var_idioma.get()

    try:
        numero = int(entrada)

        if not (0 <= numero <= 999999):
            raise ValueError

        fsm = FSMNumero(numero, idioma)
        resultado = fsm.processar()

        label_resultado.config(text=resultado)

    except:
        label_resultado.config(text="Entrada inválida")

janela = tk.Tk()
janela.title("FSM - Número por Extenso")

tk.Label(janela, text="Digite um número (0 a 999999):").pack()

entry = tk.Entry(janela)
entry.pack()

var_idioma = tk.StringVar(value="pt")

tk.Radiobutton(janela, text="Português", variable=var_idioma, value="pt").pack()
tk.Radiobutton(janela, text="English", variable=var_idioma, value="en").pack()

tk.Button(janela, text="Converter", command=converter).pack()

label_resultado = tk.Label(janela, text="", wraplength=300)
label_resultado.pack()

janela.mainloop()