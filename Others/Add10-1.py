import numpy as np
from scipy.optimize import fsolve

E = 28.68
Et = 6.28

T = fsolve(lambda T: 0.0107*T - 4.14 - Et, [1])[0]
phi = fsolve(lambda phi: 0.0496*T*np.log10(20.8/phi) - E, [1])[0]
print("所测的氧含量为：{:.1f}%".format(phi))
