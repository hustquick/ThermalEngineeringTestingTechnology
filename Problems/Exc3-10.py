R = 0.5e-2
A = 10e6
p = 8.5e6

Delta_p = R * A
delta_p = Delta_p / p

print(f"测量值的最大绝对误差为：{Delta_p/1e6} MPa")
print(f"测量值的最大相对误差为：{delta_p:.2%}")
