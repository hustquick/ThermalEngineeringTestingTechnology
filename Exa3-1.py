import numpy as np

x = np.array([28.03, 28.01, 27.98, 27.94, 27.96,
              28.02, 28.00, 27.93, 27.95, 27.90])

stdev = np.std(x, ddof=1)


def left(l):
    l_bar = np.mean(x)
    nu = l - l_bar
    sum = 0
    for i in range(len(l) - 1):
        sum += nu[i]*nu[i+1]
    return abs(sum)


right = np.sqrt(len(x)-1) * stdev**2
left = left(x)

if left > right:
    print("该组数据存在周期性系统误差")
else:
    print("该组数据不存在周期性系统误差")
