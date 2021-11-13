# 利用t检验准则去除疏失误差引起的坏值
import numpy as np

x = np.array([20.42, 20.43, 20.40, 20.43, 20.42,
              20.43, 20.39, 20.30, 20.40, 20.43,
              20.42, 20.41, 20.39, 20.39, 20.40])


# Table 3-2
def t_table(n, alpha):
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
                      [2.08, 2.81],])

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


alpha = 0.05


def use_t(x, alpha):
    K = t_table(len(x), alpha)
    # print(K)  # 可用于检验
    x_bar = np.mean(x)
    sigma_caret = np.std(x, ddof=1)
    nu = x - x_bar
    if max(abs(max(nu)), abs(min(nu))) / sigma_caret < K:
        print("上述{}个数据中不存在坏值！".format(len(x)))
    elif abs(max(nu)) < abs(min(nu)):
        print("删除坏值{}".format(x[np.argmin(nu)]))
        x = np.delete(x, np.argmin(nu))
        use_t(x, alpha)
    else:
        print("删除坏值{}".format(x[np.argmax(nu)]))
        x = np.delete(x, np.argmax(nu))
        use_t(x, alpha)


use_t(x, alpha)
