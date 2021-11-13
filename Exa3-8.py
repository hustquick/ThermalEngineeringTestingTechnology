import numpy as np

x = np.array([3002, 3004, 3000, 2998,
              2995, 3001, 3006, 3002])

x_bar = np.mean(x)
stdev = np.std(x, ddof=1)
s = stdev / np.sqrt(len(x))
lambda_lim = 3 * s
delta_lim = lambda_lim / x_bar

print("测量结果为：({:.2f} \pm {:.2f}) r/min"
      "\n或:{:.2f} r/min \pm {:.2%}".format(x_bar, lambda_lim, x_bar, delta_lim))
