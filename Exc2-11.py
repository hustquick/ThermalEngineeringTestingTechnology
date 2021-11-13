import numpy as np

A_d = 1.5
T_d = 2

xi = np.sqrt(1/((np.pi/np.log(A_d))**2+1))
omega_n = 2 * np.pi / (T_d * np.sqrt(1 - xi**2))
print("阻尼比为：{:.2f}，系统固有频率为：{:.2f} Hz".format(xi, omega_n))
