# 🌡️ Controlador Fuzzy P - Sistema de Climatização Inteligente

Este projeto implementa um **Controlador Fuzzy Tipo P em Python** para ajustar de forma inteligente e gradual a potência de um sistema de climatização *(ar condicionado/aquecedor)* com base no erro de temperatura do ambiente.

---

# 🚀 Como Executar o Projeto

## 1. Pré-requisitos

Certifique-se de ter o **Python 3** instalado no seu computador.

Você precisará instalar as bibliotecas:

- `scikit-fuzzy`
- `numpy`
- `matplotlib`
- `networkx`
- `scipy`

Instale as dependências executando o comando abaixo no terminal:

```bash
pip install scikit-fuzzy numpy matplotlib networkx scipy
```

---

## 2. Execução

Com as bibliotecas instaladas, execute o arquivo principal pelo terminal:

```bash
python controlador_fuzzy_p.py
```

---

# 📥 Valores de Entrada (O que digitar?)

O programa é interativo via linha de comando e solicitará duas entradas:

## 1. Modo de Operação (Menu Inicial)

- Digite **`1`** para o modo **Frio**  
  *(Configura automaticamente o Setpoint para 18 °C)*

- Digite **`2`** para o modo **Normal**  
  *(Configura automaticamente o Setpoint para 25 °C)*

- Digite **`3`** para o modo **Quente**  
  *(Configura automaticamente o Setpoint para 32 °C)*

## 2. Temperatura Atual (°C)

Digite a temperatura medida atualmente no ambiente.

Aceita números inteiros ou decimais.

**Exemplos:**

```text
30
24.5
15.2
```

---

# ⚙️ Como o Sistema Funciona

### 1. Cálculo do Erro
O sistema calcula a diferença:

```text
Erro = Temperatura Atual - Setpoint
```

### 2. Fuzzificação
O erro é classificado em categorias lógicas:

- Muito Negativo
- Pouco Negativo
- Zero
- Pouco Positivo
- Muito Positivo

### 3. Regras Fuzzy
O motor processa as regras de controle.

- Se o erro estiver próximo de zero, a potência reduz.
- Se o erro for muito alto *(positivo ou negativo)*, a potência aumenta.

### 4. Defuzzificação
O sistema converte os conjuntos lógicos em um valor exato de:

**Potência de Saída (0% a 100%)**

Esse valor é exibido ao final da execução.
