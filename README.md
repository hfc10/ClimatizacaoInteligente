# Controlador Fuzzy P - Sistema de Climatizacao Inteligente

Este projeto implementa um Controlador Fuzzy Tipo P em Python para ajustar de forma inteligente e gradual a potencia de um sistema de climatizacao (ar condicionado/aquecedor) com base no erro de temperatura do ambiente.

---

## Como Executar o Projeto

### 1. Pre-requisitos
Certifique-se de ter o Python 3 instalado no seu computador. Voce precisara instalar as bibliotecas `scikit-fuzzy`, `numpy` e `matplotlib` (para a geracao do grafico ao final).

Instale as dependencias executando o comando abaixo no seu terminal:
```bash
pip install scikit-fuzzy numpy matplotlib networkx scipy

---

### 2. Execucao
Com as bibliotecas instaladas, basta executar o arquivo principal pelo terminal:
`bash
python controlador_fuzzy_p.py
`

---

## Valores de Entrada (O que digitar?)

O programa e interativo via linha de comando e solicitara duas entradas:

1. **Modo de Operacao (Menu Inicial):**
   * Digite **`1`** para o modo **Frio** *(Configura automaticamente o Setpoint para 18 C)*.
   * Digite **`2`** para o modo **Normal** *(Configura automaticamente o Setpoint para 25 C)*.
   * Digite **`3`** para o modo **Quente** *(Configura automaticamente o Setpoint para 32 C)*.

2. **Temperatura Atual (C):**
   * Digite a temperatura medida atualmente no ambiente. Aceita numeros inteiros ou decimais.
   * *Exemplos:* `30`, `24.5`, `15.2`

---

## Como o Sistema Funciona

1. **Calculo do Erro:** O sistema calcula a diferenca: `Erro = Temperatura Atual - Setpoint`.
2. **Fuzzificacao:** O erro e classificado em categorias logicas (*Muito Negativo, Pouco Negativo, Zero, Pouco Positivo, Muito Positivo*).
3. **Regras Fuzzy:** O motor processa as regras de controle. Se o erro estiver proximo de zero, a potencia reduz. Se o erro for muito alto (positivo ou negativo), a potencia sobe.
4. **Defuzzificacao:** O sistema converte os conjuntos logicos de volta para um valor exato de **Potencia de Saida (0% a 100%)**, exibido no final da execucao.
