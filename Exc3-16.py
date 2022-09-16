# 线性化后进行多项式回归分析
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

plt.rcParams['font.sans-serif'] = 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False

x = np.array([10, 15, 20, 25, 30,
              35, 40, 45, 50, 55,
              60, 65, 70, 75, 80])
y = np.array([4.24, 3.51, 2.92, 2.52, 2.20,
              2.00, 1.81, 1.70, 1.60, 1.50,
              1.43, 1.37, 1.32, 1.29, 1.25])
X = np.log(x)
Y = np.log(y)

plt.scatter(x, y)
plt.grid(True)


X = X.reshape(-1, 1)
Y = Y.reshape(-1, 1)
reg = linear_model.LinearRegression()
reg.fit(X, Y)
B_1 = float(reg.coef_)
B_0 = float(reg.intercept_)
R = np.sqrt(reg.score(X, Y))
b = B_1
a = np.exp(B_0)

x_fit = np.linspace(min(x), max(x), 1000)
y_fit = a * x_fit ** b
plt.plot(x_fit, y_fit, 'r-', label='regression')
x0, y0 = 20, a * 20 ** b
plt.annotate(fr"拟合的方程为：y = {a:.3f}x$^{{{b:.3f}}}$", xy=(x0, y0), xytext=(+30, +30),
             textcoords='offset points', fontsize=10,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
plt.savefig('Exc3-16.png')
plt.show()
plt.close()
print(f"拟合的方程为：y = {a:.3f}x^({b:.3f})")
print(f"X和Y的相关系数R={R:.3f}")
