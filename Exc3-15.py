# 间接测量的表达
import numpy as np
from sympy import symbols, diff

R_a = 10.0
U_a = 100.0
delta_R = 1/100
delta_U = 1/100

P_a = U_a**2 / R_a

S_R = R_a * delta_R / 3
S_U = U_a * delta_U / 3

U, R = symbols('U, R')
P = U**2 / R
P_p_U = float(diff(P, U).subs(U, U_a).subs(R, R_a))
P_p_R = float(diff(P, R).subs(R, R_a).subs(U, U_a))

S_P = np.sqrt(P_p_U**2 * S_U**2 + P_p_R**2 * S_R**2)
lambda_P = 3 * S_P
delta_P = lambda_P / P_a
print(f"电功率的测量结果为：({P_a:.2f} \pm {lambda_P:.2f}) W"
      f"或{P_a:.2f} W \pm {delta_P:.2%}")
