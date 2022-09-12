import numpy as np
from scipy.stats import norm


def table3_1_a(k):
    """
    给定k值求2*phi(k)的值，即测量误差落在(-k*sigma, k*sigma)的概率
    """
    return norm.cdf(k) - norm.cdf(-k)


def table3_1_b(p):
    """
    给定2*phi(k)的值求k值，即已知置信度，求解k值
    """
    return norm.ppf((1+p)/2)


result = norm.cdf(2.4) - norm.cdf(-1.6)
print(f"结果为：{result:.6f}")
