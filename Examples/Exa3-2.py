import numpy as np


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


x_0 = 10e3
deviation = np.array([0.5, 0.7, 0.4, 0.5,
              0.3, 0.6, 0.5, 0.6, 0.4])

x = deviation + x_0
D, max_nu = dev(x)

if D <= max_nu:
    print("无显著的线性系统误差")
else:
    print("有显著的线性系统误差")
