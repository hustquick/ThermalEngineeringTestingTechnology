# 一元线性回归分析
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

plt.rcParams['font.sans-serif'] = 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False

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
x0 = 3
y0 = np.polyval([B_1, B_0], x0)


def signed_Value(value: float, num_dig: int) -> str:
    """为正数添加正号

    :param value: 要显示的值
    :param num_dig: 结果保留的位数
    :return: 带有符号的值
    """
    return f"+{value:.{num_dig}f}" if value > 0 else f"{value:.{num_dig}f}"


plt.annotate(fr"拟合的直线方程为：y = {B_0:.3f}{signed_Value(B_1, 3)}x", xy=(x0, y0), xytext=(-150, +30),
             textcoords='offset points', fontsize=10, color='blue',
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
plt.savefig('Exa3-12.png')
plt.show()
print(f"拟合的直线方程为：y = {B_0:.3f}{signed_Value(B_1, 3)}x")
print(f"相关系数R={R:.3f}")
