import numpy as np

Lpi = np.array([90, 90, 90])

Lpt = 10*np.log10(np.sum(10**(0.1*Lpi)))
print("三台压气机同时工作时的噪声级为：{:.2f} dB".format(Lpt))
