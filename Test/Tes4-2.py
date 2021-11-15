# 利用莱依特准则去除疏失误差引起的坏值
import numpy as np

x = np.array([3.41, 3.43, 3.40, 3.38, 3.32,
              3.43, 3.39, 3.31, 3.40, 3.43,
              3.42, 3.57, 3.39])


def use_Leyte(l):
    l_bar = np.mean(l)
    sigma_caret = np.std(l, ddof=1)
    nu = l - l_bar
    if max(abs(max(nu)), abs(min(nu))) < 3 * sigma_caret:
        print("上述{}个数据中不存在坏值！".format(len(l)))
    elif abs(max(nu)) < abs(min(nu)):
        print("删除坏值{}".format(l[np.argmin(nu)]))
        l = np.delete(l, np.argmin(nu))
        use_Leyte(l)
    else:
        print("删除坏值{}".format(l[np.argmax(nu)]))
        l = np.delete(l, np.argmax(nu))
        use_Leyte(l)


use_Leyte(x)
