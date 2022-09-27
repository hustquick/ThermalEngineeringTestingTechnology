t_l = 10
t_m = 70
t_B = 20
t_A = 25

gamma = 0.00016

n = t_m - t_l
Delta_t = gamma * n * (t_B - t_A)
t = t_m + Delta_t
print(f"被测介质实际温度为：{t:.2f}°C")
