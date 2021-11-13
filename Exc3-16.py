# 线性化后进行多项式回归分析
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

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
B_1 = reg.coef_
B_0 = reg.intercept_
R = np.sqrt(reg.score(X, Y))
b = float(B_1)
a = float(np.exp(B_0))

x_fit = np.linspace(min(x), max(x), 1000)
y_fit = a * x_fit ** b
plt.plot(x_fit, y_fit, 'r-', label='regression')
plt.savefig('Exa3-16')
x0, y0 = 20, a * 20 ** b
plt.annotate(r"拟合的方程为：y = {:.3f}x^({:.3f})".format(float(a), float(b)), xy=(x0, y0), xytext=(+30, +30), textcoords='offset points', fontsize=10, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
plt.show()
plt.close()
print("拟合的方程为：y = {:.3f}x^({:.3f})".format(float(a), float(b)))
print("X和Y的相关系数R={:.3f}".format(R))
