import time
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def controlador_climatizacao():
    print("="*60)
    print("SISTEMA DE CLIMATIZACAO INTELIGENTE (CONTROLADOR FUZZY)")
    print("="*60)

    # 1. Definir modos e setpoints
    modos = {
        "1": {"nome": "frio", "setpoint": 18},
        "2": {"nome": "normal", "setpoint": 25},
        "3": {"nome": "quente", "setpoint": 32}
    }

    # 2. Ler modo de operacao
    print("\nEscolha o modo de operacao desejado:")
    print(" [1] Frio   (Setpoint: 18 C)")
    print(" [2] Normal (Setpoint: 25 C)")
    print(" [3] Quente (Setpoint: 32 C)")
    
    escolha = input("\nDigite o numero do modo (1, 2 ou 3): ").strip()
    while escolha not in modos:
        escolha = input("Opcao invalida. Por favor, digite 1, 2 ou 3: ").strip()
        
    modo_selecionado = modos[escolha]["nome"]
    setpoint = modos[escolha]["setpoint"]
    
    print(f"\nModo '{modo_selecionado.capitalize()}' ativado.")
    print(f"O sistema vai buscar a temperatura alvo de {setpoint} C.")

    # 3. Ler temperatura atual
    while True:
        try:
            temp_atual = float(input("\nQual a temperatura atual do ambiente (C)? "))
            break
        except ValueError:
            print("Erro: Digite apenas numeros (ex: 28.5).")

    # 5. Calcular erro
    erro_calc = temp_atual - setpoint
    print(f"Calculando o erro termico (Atual - Setpoint): {erro_calc:.1f} C")
    
    print("\nIniciando motor de inferencia Fuzzy...")
    time.sleep(1.5)

    # =====================================================================
    # CONSTRUCAO DO SISTEMA FUZZY
    # =====================================================================

    # 6. Definir variavel fuzzy de entrada (erro)
    erro = ctrl.Antecedent(np.arange(-20, 21, 1), 'erro')

    # 7. Definir variavel fuzzy de saida (potencia)
    potencia = ctrl.Consequent(np.arange(0, 101, 1), 'potencia')

    # 8. Criar funcoes de pertinencia (Membership Functions)
    erro['muito_negativo'] = fuzz.trapmf(erro.universe, [-20, -20, -10, -5])
    erro['pouco_negativo'] = fuzz.trimf(erro.universe, [-10, -5, 0])
    erro['zero']           = fuzz.trimf(erro.universe, [-2, 0, 2])
    erro['pouco_positivo'] = fuzz.trimf(erro.universe, [0, 5, 10])
    erro['muito_positivo'] = fuzz.trapmf(erro.universe, [5, 10, 20, 20])

    potencia['desligado'] = fuzz.trimf(potencia.universe, [0, 0, 10])
    potencia['baixa']     = fuzz.trimf(potencia.universe, [5, 25, 50])
    potencia['media']     = fuzz.trimf(potencia.universe, [30, 50, 70])
    potencia['alta']      = fuzz.trapmf(potencia.universe, [60, 80, 100, 100])

    # 9. Criar regras fuzzy
    regra1 = ctrl.Rule(erro['muito_negativo'], potencia['alta'])   
    regra2 = ctrl.Rule(erro['pouco_negativo'], potencia['media'])  
    regra3 = ctrl.Rule(erro['zero'],           potencia['desligado'])
    regra4 = ctrl.Rule(erro['pouco_positivo'], potencia['media'])  
    regra5 = ctrl.Rule(erro['muito_positivo'], potencia['alta'])   

    # 10. Montar sistema fuzzy
    sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5])
    simulador = ctrl.ControlSystemSimulation(sistema_controle)

    # 11. Enviar erro para o sistema
    erro_limitado = max(min(erro_calc, 20), -20)
    simulador.input['erro'] = erro_limitado

    # 12. Executar inferencia fuzzy
    simulador.compute()

    # 13. Mostrar potencia de saida
    potencia_saida = simulador.output['potencia']
    
    print("\n" + "="*60)
    print("RESULTADO DA ANALISE FUZZY")
    print("="*60)
    print(f"Modo Operacao:      {modo_selecionado.capitalize()}")
    print(f"Temperatura Atual:  {temp_atual:.1f} C")
    print(f"Setpoint Alvo:      {setpoint} C")
    print(f"Erro Calculado:     {erro_calc:+.1f} C") 
    print(f"Potencia Aplicada:  {potencia_saida:.1f}%")
    print("-" * 60)
    
    if potencia_saida < 8:
        print("Status: Ambiente na temperatura ideal. Equipamento em stand-by.")
    elif erro_calc > 0:
        print("Status: Acionando o sistema de resfriamento...")
    else:
        print("Status: Acionando o sistema de aquecimento...")
        
    print("="*60)
    
    # 14. Exibir o grafico
    print("\nGerando grafico da potencia de saida. Feche a janela do grafico para encerrar o programa...")
    potencia.view(sim=simulador)
    plt.show()

if __name__ == "__main__":
    controlador_climatizacao()