import numpy as np

n = np.array([3002, 3004, 3000, 2998,
              2995, 3001, 3006, 3002])
T = np.array([15.2, 15.3, 15.0, 15.2,
              15.0, 15.2, 15.4, 15.3])

n_bar = np.mean(n)
T_bar = np.mean(T)
S_n = np.std(n, ddof=1) / np.sqrt(len(n))
S_T = np.std(T, ddof=1) / np.sqrt(len(T))
lambda_n = 3 * S_n
lambda_T = 3 * S_T
P_bar = T_bar * n_bar / 9550
S_P = np.sqrt((n_bar / 9550) ** 2 * S_T ** 2 + (T_bar / 9550) ** 2 * S_n ** 2)
lambda_P = 3 * S_P
delta_P = lambda_P / P_bar
print(f"该工况下的有效功率为：{P_bar:.2f} \pm {lambda_P:.2f} kW")
print(f"或：{P_bar:.2f} kW \pm {delta_P:.2%}")
