# 利用格拉布斯准则去除疏失误差引起的坏值
import numpy as np


# Table 3-2
def Grubbs_Table(n, alpha):
    table = np.array([[4.97, 11.46],
                      [3.56, 6.53],
                      [3.04, 5.04],
                      [2.78, 4.36],
                      [2.62, 3.96],
                      [2.51, 3.71],
                      [2.43, 3.54],
                      [2.37, 3.41],
                      [2.33, 3.31],
                      [2.29, 3.23],
                      [2.26, 3.17],
                      [2.24, 3.12],
                      [2.22, 3.08],
                      [2.20, 3.04],
                      [2.18, 3.01],
                      [2.17, 3.00],
                      [2.16, 2.95],
                      [2.15, 2.93],
                      [2.14, 2.91],
                      [2.13, 2.90],
                      [2.11, 2.88],
                      [2.11, 2.86],
                      [2.10, 2.84],
                      [2.09, 2.83],
                      [2.09, 2.82],
                      [2.08, 2.81], ])

    n_list = [4, 5, 6, 7, 8, 9, 10, 11, 12,
              13, 14, 15, 16, 17, 18, 19, 20, 21,
              22, 23, 24, 25, 26, 27, 28, 29, 30]
    alpha_list = [0.05, 0.01]
    if (n in n_list) and (alpha in alpha_list):
        n_index = n_list.index(n)
        alpha_index = alpha_list.index(alpha)
        return table[n_index][alpha_index]
    else:
        print("测量次数或显著度无法在表中查出！")
        return None


def use_Grubbs(x, alpha):
    T = Grubbs_Table(len(x), alpha)
    x = np.sort(x)
    x_bar = np.mean(x)
    sigma_caret = np.std(x, ddof=1)
    nu = x - x_bar
    if max(-nu[0], nu[-1]) / sigma_caret < T:
        print(f"上述{len(x)}个数据中不存在坏值！")
    elif nu[-1] < -nu[0]:
        print(f"删除坏值{x[0]}")
        x = np.delete(x, 0)
        use_Grubbs(x, alpha)
    else:
        print(f"删除坏值{x[-1]}")
        x = np.delete(x, -1)
        use_Grubbs(x, alpha)


alpha = 0.05
x = np.array([20.42, 20.43, 20.40, 20.43, 20.42,
              20.43, 20.39, 20.30, 20.40, 20.43,
              20.42, 20.41, 20.39, 20.39, 20.40])
use_Grubbs(x, alpha)
