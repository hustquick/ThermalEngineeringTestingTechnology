import numpy as np
from scipy.optimize import fsolve

t_0 = 30
t_f = 60
t_th = 58
tau = 10

y = (t_th - t_0)/ (t_f - t_0)
guess = tau

t = fsolve(lambda t: 1 - np.e**(-t/tau) - y, guess)[0]
print(f"t = {t:.2f} s")
