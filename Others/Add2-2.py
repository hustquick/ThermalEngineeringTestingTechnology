import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

T_original = 30
T_f = 60
T_t = 58
tau = 10

t = np.linspace(0, 50, 1000)
x = 1
y = 1 - np.e**(-t/tau)

z = T_original + (T_f - T_original) * x
T = T_original + (T_f - T_original) * y

# 利用fsolve函数和表达式求解时间
time = fsolve(lambda time: T_t - (T_original + (T_f - T_original) * (1 - np.e ** (-time / tau))), 40)[0]
print("热电偶测量值达到58°C所需要的时间为{:.2f} s".format(time))
plt.plot(t, T)
plt.savefig('T-t图.png')
plt.show()
plt.close()
