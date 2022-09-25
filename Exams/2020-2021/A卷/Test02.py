import numpy as np

g_N = 9.80665
H = 3e3
phi = np.deg2rad(29)
R = 6356766

g_phi = g_N / (1 + 2 * H/R) * (1 - 0.00265*np.cos(2*phi))
print(f"重力加速度应该取{g_phi:.4f} m/s^2")
