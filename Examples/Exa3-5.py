# 利用格拉布斯准则去除疏失误差引起的坏值
import numpy as np


# Table 3-2
def Grubbs_Table(n, alpha):
    table = np.array([[1.15, 1.15, 1.15],
                      [1.46, 1.48, 1.49],
                      [1.67, 1.71, 1.75],
                      [1.82, 1.89, 1.94],
                      [1.94, 2.02, 2.10],
                      [2.03, 2.13, 2.22],
                      [2.11, 2.21, 2.32],
                      [2.18, 2.29, 2.41],
                      [2.23, 2.36, 2.48],
                      [2.29, 2.41, 2.55],
                      [2.33, 2.46, 2.61],
                      [2.37, 2.51, 2.66],
                      [2.41, 2.55, 2.71],
                      [2.44, 2.59, 2.75],
                      [2.47, 2.62, 2.79],
                      [2.50, 2.65, 2.82],
                      [2.53, 2.68, 2.85],
                      [2.56, 2.71, 2.88],
                      [2.58, 2.73, 2.91],
                      [2.60, 2.76, 2.94],
                      [2.62, 2.78, 2.96],
                      [2.64, 2.80, 2.99],
                      [2.66, 2.82, 3.01],
                      [2.75, 2.91],
                      [2.82, 2.93],
                      [2.87, 3.04],
                      [2.92, 3.09],
                      [2.96, 3.13],
                      [3.03, 3.20],
                      [3.09, 3.24],
                      [3.14, 3.31],
                      [3.18, 3.35],
                      [3.21, 3.38], ], dtype=object)

    n_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
              13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
              23, 24, 25, 30, 35, 40, 45, 50, 60, 70,
              80, 90, 100]
    alpha_list = [0.05, 0.025, 0.01]
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
