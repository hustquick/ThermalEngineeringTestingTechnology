import numpy as np


x = np.array([47.4, 47.5, 47.8, 47.7, 47.8,
              47.3, 47.6, 47.9, 47.7, 47.4])


def dev(l):
    l_bar = l.mean()
    nu = l - l_bar
    le = len(nu)
    if le % 2 == 0:
        nu1 = nu[:le//2]
        nu2 = nu[le//2:]
    else:
        nu1 = nu[:(le-1)//2]
        nu2 = nu[int(le+1)//2:]
    return sum(nu1) - sum(nu2), max(max(abs(nu1)), max(abs(nu2)))


D, max_nu = dev(x)

if D <= max_nu:
    print("无显著的线性系统误差")
else:
    print("有显著的线性系统误差")
