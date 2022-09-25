# 计算多组数据的结果表达
import numpy as np

x_A = np.array([60.2, 60.3, 60.1, 60.3, 60.5,
                60.4, 60.4, 60.3])
x_B = np.array([60.18, 60.29, 60.08, 60.29, 60.48, 60.39,
                60.35, 60.32, 60.25])

x_bar_A = np.mean(x_A)
x_bar_B = np.mean(x_B)
sigma_A = np.std(x_A, ddof=1)
sigma_B = np.std(x_B, ddof=1)
S_A = sigma_A / np.sqrt(len(x_A))
S_B = sigma_B / np.sqrt(len(x_B))
lambda_A = 3 * S_A
lambda_B = 3 * S_B
print(f"实验者A的测温结果为：{x_bar_A:.2f} \pm {lambda_A:.2f}")
print(f"实验者B的测温结果为：{x_bar_B:.2f} \pm {lambda_B:.2f}")

P_A = (1 / S_A ** 2) / ((1 / S_A ** 2) + (1 / S_B ** 2))
P_B = (1 / S_B ** 2) / ((1 / S_A ** 2) + (1 / S_B ** 2))

x_bar = x_bar_A * P_A + x_bar_B * P_B

S = np.sqrt(1 / ((1 / S_A) ** 2 + (1 / S_B) ** 2))
print(f"两组数据的组合测温结果为：{x_bar:.2f} \pm {3*S:.2f}")
