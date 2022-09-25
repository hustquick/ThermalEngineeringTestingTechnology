import numpy as np
from thermocouples_reference import thermocouples as tc
from scipy.optimize import fsolve

T_1 = 10
tau = 5
t = 3
Delta_V = 4.344

type_K = tc['K']    # K型热电偶
# V_1 = type_K.emf_mVC(T_1)
# V_2 = V_1 + Delta_V
# T_2 = type_K.inverse_CmV(V_2)
T_2 = type_K.inverse_CmV(Delta_V, Tref=T_1)


def T(T_f):
    return T_1 + (T_f - T_1) * (1 - np.exp(-t/tau)) - T_2


T_f = fsolve(T, np.array([200]))[0]
print(f"炉内实际温度为：{T_f:.2f}°C")
