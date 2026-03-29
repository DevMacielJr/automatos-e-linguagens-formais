# 🧠 FSM - Conversor de Números por Extenso

Projeto desenvolvido para a disciplina de **Autômatos e Linguagens Formais**, com o objetivo de implementar uma **Máquina de Estados Finitos (FSM)** capaz de converter números inteiros em sua forma por extenso.

---

## 🚀 Funcionalidades

* 🔢 Conversão de números de **0 até 999999**
* 🌎 Suporte a **Português (PT-BR)** e **Inglês (EN)**
* 🧠 Implementação baseada em **FSM com estados explícitos**
* 💻 Interface via terminal (CLI)
* 🖥️ Interface gráfica simples com Tkinter
* 🧪 Testes automatizados com pytest

---

## 🏗️ Estrutura do Projeto

```
2_lista_de_programacao/
│
├── src/
│   ├── fsm_numero.py
│   ├── main.py
│   └── interface.py
│
├── tests/
│   └── test_fsm.py
│
├── docs/
│   └── ALF_Lista_2.pdf
│
└── README.md
```

---

## 🧠 Modelagem da FSM

A solução foi implementada utilizando uma abordagem formal baseada em estados:

* `INICIO`
* `MILHAR`
* `CENTENA`
* `FIM`

Essa modelagem aproxima a implementação prática do conceito teórico de **Máquinas de Estados Finitos**.

---

## ▶️ Como executar

### 🔹 Terminal (CLI)

```
python src/main.py
```

---

### 🔹 Interface Gráfica

```
python src/interface.py
```

---

## 🧪 Testes

Instale o pytest:

```
pip install pytest
```

Execute os testes:

```
pytest
```

---

## 📌 Exemplo de uso

Entrada:

```
204328
```

Saída:

```
duzentos e quatro mil, trezentos e vinte e oito
```

---

## 🎯 Objetivo Acadêmico

Este projeto tem como objetivo aplicar conceitos de:

* Autômatos finitos
* Modelagem de estados
* Processamento de entrada sequencial
* Organização de código modular

---

## 👨‍💻 Autor

**Edson Maciel de Barros Junior**

---

## ⭐ Diferenciais

* Implementação fiel ao modelo formal de FSM
* Código modular e organizado
* Suporte multilíngue
* Interface gráfica simples
* Pronto para portfólio

---
