import numpy as np

x = np.array([102.25, 101.84, 102.15, 102.27, 101.85,
              102.22, 102.05, 102.15, 101.97, 102.13])

x_bar = np.mean(x)
sigma_caret = np.std(x, ddof=1)
s = sigma_caret / np.sqrt(len(x))
lambda_lim = 3 * s
delta_lim = lambda_lim / x_bar

print(f"测量结果为：({x_bar:.3f} \pm {lambda_lim:.3f}) kPa"
      f"\n或:{x_bar:.3f} kPa \pm {delta_lim:.2%}")
