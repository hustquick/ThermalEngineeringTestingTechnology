import numpy as np
from scipy.optimize import fsolve

tau = 10
ratio = 90/100

guess_time = 40
t = fsolve(lambda t: 1 - np.e**(-t/tau) - ratio, guess_time)[0]
print(f"t = {t:.2f} s")
