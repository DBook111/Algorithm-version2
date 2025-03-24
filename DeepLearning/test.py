import numpy as np

# 参数
mu, sigma = 0, 1  # 均值和标准差

# 生成1000个符合正态分布的二维样本，每个样本有两个维度
samples = np.random.normal(mu, sigma, (1000, 6))
print(samples[:10])  # 打印前10个样本
