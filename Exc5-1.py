from scipy.constants import g

h = 500e-3
rho = 1000
delta_p = rho * g * h
print(f'左右两端介质的压力差为：{delta_p:.0f} Pa')
