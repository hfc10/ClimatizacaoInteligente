# 🌡️ Controlador Fuzzy P - Sistema de Climatização Inteligente

Este projeto implementa um **Controlador Fuzzy em Python** para ajustar de forma inteligente a potência de um sistema de climatização *(resfriamento ou aquecimento)* com base no **erro térmico** entre a temperatura atual do ambiente e a temperatura alvo *(setpoint)*.

---

# 🚀 Como Executar o Projeto

## 1. Pré-requisitos

Certifique-se de possuir o **Python 3** instalado.

Instale as dependências necessárias:

```bash
pip install scikit-fuzzy numpy matplotlib networkx scipy
```

---

## 2. Execução

Após instalar as bibliotecas, execute o arquivo principal:

```bash
python controlador_fuzzy_p.py
```

---

# 📥 Entradas do Sistema

O programa funciona via linha de comando e solicitará duas entradas.

## 1. Modo de Operação

Selecione o modo desejado:

| Opção | Modo | Setpoint |
|---|---|---:|
| `1` | Frio | 18 °C |
| `2` | Normal | 25 °C |
| `3` | Quente | 32 °C |

O modo escolhido define automaticamente a **temperatura alvo (setpoint)**.

## 2. Temperatura Atual

Digite a temperatura atual do ambiente.

Aceita números inteiros ou decimais.

**Exemplos:**

```text
30
24.5
15.2
```

---

# ⚙️ Funcionamento do Sistema Fuzzy

O controlador segue as etapas abaixo:

## 1. Cálculo do Erro Térmico

O sistema calcula:

```text
Erro = Temperatura Atual - Setpoint
```

Esse erro representa a diferença entre a temperatura do ambiente e a temperatura desejada.

---

## 2. Fuzzificação

O erro térmico é convertido em conjuntos fuzzy por meio das seguintes categorias:

- Muito Negativo
- Pouco Negativo
- Zero
- Pouco Positivo
- Muito Positivo

---

## 3. Variável de Saída

A saída do sistema é a **Potência Aplicada (%)**, dividida em:

- Desligado
- Baixa
- Média
- Alta

---

## 4. Regras Fuzzy

O motor de inferência utiliza as seguintes regras:

| Erro | Potência |
|---|---|
| Muito Negativo | Alta |
| Pouco Negativo | Média |
| Zero | Desligado |
| Pouco Positivo | Média |
| Muito Positivo | Alta |

---

## 5. Inferência e Defuzzificação

Após aplicar as regras fuzzy, o sistema realiza a **defuzzificação** para converter os conjuntos fuzzy em um valor numérico de **potência aplicada (0% a 100%)**.

O resultado é exibido no terminal junto com:

- Modo de operação
- Temperatura atual
- Setpoint
- Erro calculado
- Potência aplicada
- Status do sistema

---

## 📊 Visualização Gráfica

Ao final da execução, o programa gera um **gráfico da potência de saída fuzzy**, permitindo visualizar o comportamento do controlador e o resultado da inferência.
