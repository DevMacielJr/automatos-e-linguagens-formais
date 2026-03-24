# 🧠 Máquina de Estados Finitos (FSM)

Este projeto foi desenvolvido para a disciplina **Autômatos e Linguagens Formais** e tem como objetivo implementar uma **Máquina de Estados Finitos (FSM)** de forma interativa.

---

## 📌 Objetivo

Modelar e simular máquinas de estados finitos permitindo:

* Definir estados, entradas e saídas
* Criar a tabela de transição de estados
* Executar a máquina de forma interativa
* Resetar para o estado inicial
* Testar múltiplas máquinas

---

## ⚙️ Estrutura do Projeto

O programa é baseado em dois componentes principais:

### 🔹 Tabela de Transição (TE)

Define para qual estado a máquina vai com base no estado atual e na entrada.

### 🔹 Vetor de Saída (VS)

Define a saída associada a cada estado.

---

## 🔄 Funcionamento

A lógica da máquina segue o fluxo:

```
estado atual + entrada → próximo estado → saída
```

---

## ▶️ Como executar

1. Certifique-se de ter o Python instalado
2. Execute o arquivo:

```
python MSF.py
```

---

## 🕹️ Como usar

Ao iniciar o programa, você verá um menu:

```
1 - Máquina do enunciado
2 - Máquina detectora de '11'
0 - Sair
```

### Entradas válidas:

* `0` ou `1` → entradas da máquina
* `r` → reset (volta para o estado inicial)

---

## 🧪 Máquinas implementadas

### 🔸 Máquina 1 (Enunciado)

* Baseada no exemplo fornecido pelo professor
* Possui 3 estados: s0, s1, s2

---

### 🔸 Máquina 2 (Detectora de "11")

* Detecta duas entradas consecutivas iguais a `1`
* Retorna saída `1` quando a sequência é identificada

---

## 📌 Exemplo de execução

```
Entrada: 1
Estado: s1 | Saída: 0

Entrada: 1
Estado: s2 | Saída: 1
```

---

## 🔁 Reset

```
Entrada: r
Reset → s0
```

---

## 💡 Observações

* O programa aceita apenas entradas válidas (`0`, `1` ou `r`)
* Qualquer outro valor será rejeitado
* A estrutura é genérica e pode ser adaptada para outras FSMs

---

## 🎥 Demonstração

Um vídeo de até 5 minutos foi gravado demonstrando:

* Explicação do funcionamento
* Execução das máquinas
* Testes práticos

---

## 👨‍💻 Autor

Edson Maciel de Barros Junior

---

## 📚 Disciplina

Autômatos e Linguagens Formais
UFRN – 2026.1
