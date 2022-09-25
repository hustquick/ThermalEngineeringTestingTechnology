# 系统误差的估算
import numpy as np

R = 0.5/100
A_min = 0
A_max = 600e3
delta_p_s = 2e3
p = 300e3
Delta_p_s = 1
Delta_h = 0.05
Delta_T = 10
Delta_T_s = 4/100

rho = 1000
g = 9.8

# 仪表基本误差
Delta_p_1 = R * (A_max - A_min)
# 环境温度造成的误差
Delta_p_2 = Delta_T_s * Delta_T * Delta_p_1
# 安装误差
Delta_p_3 = Delta_h * rho * g
# 读数误差
Delta_p_4 = Delta_p_s * delta_p_s

Delta_p_list = np.array([Delta_p_1, Delta_p_2, Delta_p_3, Delta_p_4])
# 如果按照算数综合法
Delta_p = np.sum(Delta_p_list)
delta_p = Delta_p / p
print("按照算术综合法，绝对误差为：{:.2f} kPa，相对误差为：{:.2%}".format(Delta_p/1000, delta_p))

# 如果按照几何综合法
Delta_p = np.sqrt(np.sum(np.power(Delta_p_list, 2)))
delta_p = Delta_p / p
print("按照几何综合法，绝对误差为：{:.2f} kPa，相对误差为：{:.2%}".format(Delta_p/1000, delta_p))