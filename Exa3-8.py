import numpy as np

x = np.array([3002, 3004, 3000, 2998,
              2995, 3001, 3006, 3002])

x_bar = np.mean(x)
stdev = np.std(x, ddof=1)
s = stdev / np.sqrt(len(x))
lambda_lim = 3 * s
delta_lim = lambda_lim / x_bar

print(f"测量结果为：({x_bar:.2f} \pm {lambda_lim:.2f}) r/min"
      f"\n或:{x_bar:.2f} r/min (\pm {delta_lim:.2%})")
