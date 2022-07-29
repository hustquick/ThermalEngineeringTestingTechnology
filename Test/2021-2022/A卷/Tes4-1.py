import numpy as np

x = np.array([2.45, 2.50, 2.51, 2.43, 2.48,
              2.52, 2.50, 2.51, 2.47, 2.49])

x_bar = np.mean(x)
stdev = np.std(x, ddof=1)
s = stdev / np.sqrt(len(x))
lambda_lim = 3 * s
delta_lim = lambda_lim / x_bar

print("测量结果为：({:.3f} \pm {:.3f}) m/s"
      "\n或:{:.3f} m/s \pm {:.2%}".format(x_bar, lambda_lim, x_bar, delta_lim))
