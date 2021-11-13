import numpy as np
from scipy.constants import convert_temperature, R
from CoolProp.CoolProp import PropsSI as psi
from scipy.optimize import fsolve

delta_p = 19.7e3
p = 100e3
t = 15
zeta = 1
Ma_epsilon_table = np.array([
    [0.1, 0.0025],
    [0.2, 0.0100],
    [0.3, 0.0225],
    [0.4, 0.0400],
    [0.5, 0.0620],
    [0.6, 0.0900],
    [0.7, 0.1280],
    [0.8, 0.1730],
    [0.9, 0.2190],
    [1.0, 0.2750],
    ])

kappa = 1.4
T = convert_temperature(t, 'C', 'K')
rho = psi('D', 'T', T, 'P', p, 'air')
v_i = zeta * np.sqrt(2 * delta_p / rho)

p_0 = p + delta_p

Ma = fsolve(lambda Ma: p_0 / p - np.power(1 + (kappa - 1)/2 * Ma**2, kappa / (kappa - 1)), 0.8)[0]

Ma_list = Ma_epsilon_table[:, 0]
epsilon_list = Ma_epsilon_table[:, 1]
epsilon = np.interp(Ma, Ma_list, epsilon_list)
v = zeta * np.sqrt(2 * delta_p / (rho * (1+epsilon)))

print('(1) 空气可压缩时，空气的流速为：{:.2f} m/s'.format(v))
print('(2) 空气不可压缩时，空气的流速为：{:.2f} m/s'.format(v_i))

M = 29e-3
v_c = np.sqrt(kappa * R/M * T)
v_r = Ma * v_c
print('(3) 由马赫数算得的空气可压缩时，空气的流速为：{:.2f} m/s'.format(v_r))
