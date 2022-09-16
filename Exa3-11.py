# 多项式回归分析
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False

x = np.array(range(8)) + 1
y = np.array([4.86, 5.14, 5.15, 4.85,
              4.24, 3.36, 2.16, 0.67])

plt.scatter(x, y)
plt.grid(True)


reg = np.polyfit(x, y, deg=2)
x_fit = np.linspace(x[0], x[-1], 1000)
y_fit = np.polyval(reg, x_fit)
plt.plot(x_fit, y_fit, 'r-', label='regression')
x0 = 6.8
y0 = np.polyval(reg, x0)
plt.annotate(fr"拟合的直线方程为：$y = {reg[0]:.3f}x^2 + {reg[1]:.3f}x + {reg[2]:.3f}$", xy=(x0, y0), xytext=(-260, -30),
             textcoords='offset points', fontsize=10, color='blue',
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
plt.savefig('Exa3-11.png')
print(f"拟合的直线方程为：y = {reg[0]:.3f}x^2 + {reg[1]:.3f}x + {reg[2]:.3f}")
plt.show()
