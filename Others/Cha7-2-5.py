import numpy as np
from CoolProp.CoolProp import PropsSI as psi
from scipy.constants import convert_temperature

p = 1.35e6
t = 550
q_u = 55
q_m_max = 70
q_m_min = 28
Delta_p_max = 6e4
D = 233e-3
# 全开闸阀

T = convert_temperature(t, 'C', 'K')
mu = psi('V', 'P', p, 'T', T, 'water')
rho = psi('D', 'P', p, 'T', T, 'water')
q_v = q_u / rho

Re_D = 4 * q_u / (np.pi * D * mu)

Delta_p_u = (q_u / q_m_max)**2 * Delta_p_max


def get_beta_square_alpha(d, Delta_p_u):
    epsilon = 1
    beta_square_alpha = q_v / (epsilon * np.pi * D**2 / 4 *np.sqrt(2 * Delta_p_u/rho))
    return beta_square_alpha

L_1 = L_2_p = 0
M_2_p = 2 * L_2_p / (1 - beta)
