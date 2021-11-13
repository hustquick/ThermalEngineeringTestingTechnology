import numpy as np
from scipy.constants import convert_temperature
from sympy import symbols, diff, log

t_s = 1300
lamda = 0.65e-6
epsilon_a = 0.7
delta_epsilon = 0.05
C_2 = 1.438e-2
T_s = convert_temperature(t_s, 'C', 'K')

T = 1 / (1 / T_s - lamda/C_2*np.log(1 / epsilon_a))
t = convert_temperature(T, 'K', 'C')
print('（1）炉膛内的实际温度为{:.2f}°C'.format(t))

epsilon = symbols('epsilon')
T = 1 / (1 / T_s - lamda/C_2*log(1 / epsilon))
T_p = diff(T, epsilon).subs(epsilon, epsilon_a)
delta_T = T_p * delta_epsilon
print('（2）由epsilon变化引起的测温误差为：{:.2f}°C'.format(abs(delta_T)))
