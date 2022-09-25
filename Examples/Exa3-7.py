# 利用狄克逊准则去除疏失误差引起的坏值
import numpy as np

x = np.array([20.42, 20.43, 20.40, 20.43, 20.42,
              20.43, 20.39, 20.30, 20.40, 20.43,
              20.42, 20.41, 20.39, 20.39, 20.40])
x = np.sort(x)


# Table 3-2
def r_table(n, alpha):
    table = np.array([[0.998, 0.341],
                      [0.889, 0.765],
                      [0.780, 0.642],
                      [0.698, 0.560],
                      [0.637, 0.507],
                      [0.683, 0.554],
                      [0.635, 0.512],
                      [0.597, 0.477],
                      [0.679, 0.576],
                      [0.642, 0.546],
                      [0.615, 0.521],
                      [0.641, 0.546],
                      [0.616, 0.525],
                      [0.595, 0.507],
                      [0.577, 0.490],
                      [0.561, 0.475],
                      [0.547, 0.462],
                      [0.535, 0.450],
                      [0.524, 0.440],
                      [0.514, 0.430],
                      [0.505, 0.421],
                      [0.497, 0.413],
                      [0.489, 0.406],])

    n_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
              13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
              23, 24, 25]
    alpha_list = [0.01, 0.05]
    if (n in n_list) and (alpha in alpha_list):
        n_index = n_list.index(n)
        alpha_index = alpha_list.index(alpha)
        return table[n_index][alpha_index]
    else:
        print("测量次数或显著度无法在表中查出！")
        return None


alpha = 0.05


def r_n(x):
    n = len(x)
    if n <= 7:
        return (x[n-1] - x[n-2]) / (x[n-1] - x[0])
    elif n <= 10:
        return (x[n-1] - x[n-2]) / (x[n-1] - x[1])
    elif n <= 13:
        return (x[n-1] - x[n-3]) / (x[n-1] - x[1])
    else:
        return (x[n-1] - x[n-3]) / (x[n-1] - x[2])


def r_1(x):
    n = len(x)
    if n <= 7:
        return (x[0] - x[1]) / (x[0] - x[n-1])
    elif n <= 10:
        return (x[0] - x[1]) / (x[0] - x[n-2])
    elif n <= 13:
        return (x[0] - x[2]) / (x[0] - x[n-2])
    else:
        return (x[0] - x[2]) / (x[0] - x[n-3])


def use_r(x, alpha):
    r_0 = r_table(len(x), alpha)
    # print(r_0)  # 可用于检验
    rn = r_n(x)
    r1 = r_1(x)
    if rn < r_0 and r1 < r_0:
        print(f"上述{len(x)}个数据中不存在坏值！")
    elif rn < r1:
        print(f"删除坏值{x[0]}")
        x = np.delete(x, 0)
        use_r(x, alpha)
    else:
        print(f"删除坏值{x[-1]}")
        x = np.delete(x, -1)
        use_r(x, alpha)


use_r(x, alpha)
