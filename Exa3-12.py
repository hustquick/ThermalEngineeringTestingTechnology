# 一元线性回归分析
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

x = np.array([1.0, 1.6, 3.4, 4.0, 5.2])
y = np.array([1.2, 2.0, 2.4, 3.5, 3.5])

plt.scatter(x, y)

x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
reg = linear_model.LinearRegression()
reg.fit(x, y)
B_1 = float(reg.coef_)
B_0 = float(reg.intercept_)
R = np.sqrt(reg.score(x, y))
x_fit = np.linspace(x[0], x[-1], 1000)
y_fit = np.polyval([B_1, B_0], x_fit)
plt.plot(x_fit, y_fit, 'r-', label='regression')
plt.savefig('Exa3-12')
plt.show()
print(f"拟合的直线方程为：y = {B_0:.3f} + {B_1:.3f}x")
print(f"相关系数R={R:.3f}")
