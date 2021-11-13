# 多项式回归分析
import numpy as np
import matplotlib.pyplot as plt

x = np.array(range(8)) + 1
y = np.array([4.86, 5.14, 5.15, 4.85,
              4.24, 3.36, 2.16, 0.67])

plt.scatter(x, y)
plt.grid(True)


reg = np.polyfit(x, y, deg=2)
x_fit = np.linspace(x[0], x[-1], 1000)
y_fit = np.polyval(reg, x_fit)
plt.plot(x_fit, y_fit, 'r-', label='regression')
plt.savefig('Exa3-11')
plt.show()
