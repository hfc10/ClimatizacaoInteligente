import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# -------------------------
# REFERENCIA
# -------------------------

Tref = 25

# -------------------------
# VARIABLES DIFUSAS
# -------------------------

error = ctrl.Antecedent(np.arange(-10, 11, 1), 'error')
power = ctrl.Consequent(np.arange(0, 101, 1), 'power')

# -------------------------
# MEMBERSHIPS
# -------------------------

error['negative'] = fuzz.trimf(error.universe, [-10, -10, 0])
error['zero'] = fuzz.trimf(error.universe, [-5, 0, 5])
error['positive'] = fuzz.trimf(error.universe, [0, 10, 10])

power['low'] = fuzz.trimf(power.universe, [0, 0, 50])
power['medium'] = fuzz.trimf(power.universe, [25, 50, 75])
power['high'] = fuzz.trimf(power.universe, [50, 100, 100])

# -------------------------
# REGLAS
# -------------------------

rule1 = ctrl.Rule(error['negative'], power['low'])
rule2 = ctrl.Rule(error['zero'], power['medium'])
rule3 = ctrl.Rule(error['positive'], power['high'])

power_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

power_sim = ctrl.ControlSystemSimulation(power_ctrl)

# -------------------------
# ENTRADA DEL USUARIO
# -------------------------

Tactual = float(input("Ingrese temperatura actual: "))

# -------------------------
# CÁLCULO DEL ERROR
# -------------------------

e = Tref - Tactual

print(f"Error calculado: {e}")

# -------------------------
# CONTROL DIFUSO
# -------------------------

power_sim.input['error'] = e

power_sim.compute()

# -------------------------
# RESULTADO
# -------------------------

output_power = power_sim.output['power']

print(f"Potencia de salida: {output_power:.2f}%")