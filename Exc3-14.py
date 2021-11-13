# 一元线性回归分析
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

x = np.array([19.1, 25.0, 30.1, 36.0, 40.0, 45.1, 50.0])
y = np.array([76.30, 77.80, 79.75, 80.80, 82.35, 83.90, 85.10])

plt.scatter(x, y)

x = x.reshape(-1, 1)
y = y.reshape(-1, 1)
reg = linear_model.LinearRegression()
reg.fit(x, y)
B_1 = reg.coef_
B_0 = reg.intercept_
R = np.sqrt(reg.score(x, y))
x_fit = np.linspace(x[0], x[-1], 1000)
y_fit = np.polyval([B_1, B_0], x_fit)
plt.plot(x_fit, y_fit, 'r-', label='regression')
plt.savefig('Exc3-14')
plt.show()
R_0 = B_0
alpha = B_1 / R_0
print("拟合的直线方程为：y = {:.3f}(1 + {:.3f}x)".format(float(B_0), float(B_1)))
print("相关系数R={:.3f}".format(R))
