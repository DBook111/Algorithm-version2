import numpy as np
from scipy.stats import ttest_rel
import matplotlib.pyplot as plt

# 模拟10个病例的分割结果（Dice coefficient）
dice_model_a = np.array([0.81, 0.79, 0.83, 0.80, 0.82, 0.78, 0.76, 0.84, 0.80, 0.81])
dice_model_b = np.array([0.85, 0.84, 0.86, 0.85, 0.87, 0.82, 0.80, 0.87, 0.85, 0.86])

# 打印平均值
print("模型 A 平均 Dice：", np.mean(dice_model_a))
print("模型 B 平均 Dice：", np.mean(dice_model_b))

# 进行配对 t 检验
t_stat, p_value = ttest_rel(dice_model_b, dice_model_a)
print(f"\n配对 t 检验结果：")
print(f"t 统计量 = {t_stat:.10f}")
print(f"p-value = {p_value:.10f}")

# 判断统计显著性
alpha = 0.05
if p_value < alpha:
    print("✅ 差异具有统计学意义，新模型显著更好。")
else:
    print("❌ 差异不具有统计学意义，可能只是巧合。")

# 可视化：每个病例的表现对比
plt.figure(figsize=(10, 5))
x = np.arange(1, len(dice_model_a)+1)
plt.plot(x, dice_model_a, marker='o', label='模型 A')
plt.plot(x, dice_model_b, marker='s', label='模型 B')
plt.title('每个病例的 Dice 系数对比')
plt.xlabel('病例编号')
plt.ylabel('Dice 系数')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
