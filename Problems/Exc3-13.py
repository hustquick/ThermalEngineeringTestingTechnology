# 利用莱依特准则(3 sigma准则)去除疏失误差引起的坏值
import numpy as np


def use_Leyte(l):
    l = np.sort(l)
    l_bar = np.mean(l)
    sigma_caret = np.std(l, ddof=1)
    nu = l - l_bar
    if max(-nu[0], nu[-1]) < 3 * sigma_caret:
        print(f"上述{len(l)}个数据中不存在坏值！")
    elif nu[-1] < -nu[0]:
        print(f"删除坏值{l[0]}")
        l = np.delete(l, 0)
        use_Leyte(l)
    else:
        print(f"删除坏值{l[-1]}")
        l = np.delete(l, -1)
        use_Leyte(l)


x = np.array([20.42, 20.43, 20.40, 20.43, 20.42,
              20.43, 20.39, 20.30, 20.40, 20.43,
              20.42, 20.41, 20.39, 20.39, 20.40])

use_Leyte(x)
