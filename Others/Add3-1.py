import numpy as np

x = np.array([3.24, 3.26, 3.21, 3.23, 3.25,
              3.24, 3.27, 3.25, 3.22, 3.24])

x_bar = np.mean(x)
stdev = np.std(x, ddof=1)
s = stdev / np.sqrt(len(x))
lambda_lim = 3 * s
delta_lim = lambda_lim / x_bar

print("测量结果为：({:.3f} \pm {:.3f}) m/s"
      "\n或:{:.3f} m/s \pm {:.2%}".format(x_bar, lambda_lim, x_bar, delta_lim))
