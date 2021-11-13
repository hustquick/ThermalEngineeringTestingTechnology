import numpy as np
from scipy.constants import convert_temperature
from sympy import symbols, diff, log

t_s = [726.85, 1726.85]
epsilon = 0.85
epsilon_e = 0.68

T_s = convert_temperature(t_s, 'C', 'K')

T = T_s * np.power(1/epsilon, 1/4)
# t = convert_temperature(T, 'K', 'C')
T_e = T_s * np.power(1/epsilon_e, 1/4)
# t_e = convert_temperature(T_e, 'K', 'C')
err = T_e - T
print('由此带来的误差分别为：{:.2f} K和{:.2f} K'.format(err[0], err[1]))
