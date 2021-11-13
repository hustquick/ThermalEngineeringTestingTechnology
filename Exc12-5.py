import numpy as np

L_p = np.array([80, 81, 83, 80, 81, 83, 82, 81])
r  = 1
r_p = 2
# (1)
L_pm = 10*np.log10(np.mean(np.power(10, 0.1*L_p)))
L_w = L_pm + 20*np.log10(r) + 8
print("（1）平均声压级为{:.2f} dB，平均声功率级为{:.2f} dB".format(L_pm, L_w))

# (2)
L_pm_p = L_pm + 20*np.log10(r) - 20*np.log10(r_p)
print("（2）当测量球面半径变为2 m时， 平均声压级的测量值将变成{:.2f} dB".format(L_pm_p))
