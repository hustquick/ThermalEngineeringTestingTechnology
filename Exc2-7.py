import numpy as np

omega_n = 800
xi = 0.14
omega_d = 400

eta = omega_d/omega_n

A = 1 / np.sqrt((1 - eta**2)**2 + (2*xi*eta)**2)
phi = np.arctan((2*xi*eta)/(1-eta**2))

print(f"幅值为：{A:.2f}，相位为：{phi:.2f}")
