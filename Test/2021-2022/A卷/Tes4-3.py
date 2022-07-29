import numpy as np
from scipy.optimize import fsolve

T_1 = 20
tau = 10
t = 15
Delta_V = 4.321
K_thermalelectric_protential = np.array([
    [0, 0],
    [10, 0.3969],
    [20, 0.7981],
    [30, 1.2033],
    [40, 1.6118],
    [50, 2.0231],
    [60, 2.4365],
    [70, 2.8512],
    [80, 3.2666],
    [90, 3.6819],
    [100, 4.0962],
    [110, 4.5091],
    [120, 4.9199],
    [130, 5.3284],
    [140, 5.7345],
    [150, 6.1383],
    [160, 6.5402],
    [170, 6.9406],
    [180, 7.3400],
    [190, 7.7391],
    [200, 8.1385],
    [210, 8.5386],
    [220, 8.9399],
    [230, 9.3427],
    [240, 9.7472],
    [250, 10.151],
    ])

T_list = K_thermalelectric_protential[:, 0]
V_list = K_thermalelectric_protential[:, 1]
V_1 = np.interp(T_1, T_list, V_list)
V_2 = V_1 + Delta_V
T_2 = np.interp(V_2, V_list, T_list)


def T(T_f):
    return T_1 + (T_f - T_1) * (1 - np.exp(-t/tau)) - T_2


T_f = fsolve(T, np.array([200]))[0]
print("炉内实际温度为：{:.2f}°C".format(T_f))
