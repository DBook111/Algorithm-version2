import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
import cv2
import scipy.stats as stats
from pathlib import Path

# 设置中文字体
try:
    font_path = font_manager.findfont(font_manager.FontProperties(family='SimHei'))
    plt.rcParams['font.family'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
except:
    print("未找到中文字体，将使用默认字体")

def analyze_image_distribution(image_path):
    """
    分析图像的像素值分布
    """
    # 读取图像
    img = cv2.imread(str(image_path))
    
    if img is None:
        raise FileNotFoundError(f"无法读取图像: {image_path}")
    
    # 转换为灰度图
    if len(img.shape) == 3:
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray_img = img
    
    # 获取像素值数组并展平
    pixel_values = gray_img.flatten()
    
    # 计算均值和标准差
    mean = np.mean(pixel_values)
    std = np.std(pixel_values)
    
    # 进行正态性检验
    shapiro_test = stats.shapiro(np.random.choice(pixel_values, size=min(5000, len(pixel_values)), replace=False))
    ks_test = stats.kstest(pixel_values, 'norm', args=(mean, std))
    
    normality_results = {
        'shapiro': {'statistic': shapiro_test[0], 'p_value': shapiro_test[1]},
        'ks': {'statistic': ks_test[0], 'p_value': ks_test[1]}
    }
    
    return pixel_values, mean, std, normality_results

def plot_distributions(natural_image_path, medical_image_path, output_path=None):
    """
    绘制两张图像的数据分布差异
    """
    # 分析两张图像
    try:
        natural_values, natural_mean, natural_std, natural_normality = analyze_image_distribution(natural_image_path)
        medical_values, medical_mean, medical_std, medical_normality = analyze_image_distribution(medical_image_path)
    except FileNotFoundError as e:
        print(f"错误: {e}")
        return
    
    # 创建画布和子图
    fig = plt.figure(figsize=(12, 8))
    # 子图布局: 1行1列
    ax1 = plt.subplot(111)  # 直方图和正态分布
    
    # 设置直方图的参数
    bins = 50
    alpha = 0.6
    
    # 绘制自然图像的直方图
    ax1.hist(natural_values, bins=bins, alpha=alpha, color='blue', 
            density=True, label=f'自然图像分布: μ={natural_mean:.2f}, σ={natural_std:.2f}')
    
    # 绘制医学图像的直方图
    ax1.hist(medical_values, bins=bins, alpha=alpha, color='red', 
            density=True, label=f'医学图像分布: μ={medical_mean:.2f}, σ={medical_std:.2f}')
    
    # 创建x轴数据点
    x = np.linspace(0, 255, 1000)
    
    # 绘制自然图像的正态分布曲线
    natural_normal = stats.norm.pdf(x, natural_mean, natural_std)
    ax1.plot(x, natural_normal, 'b-', linewidth=2, label='自然图像正态分布')
    
    # 绘制医学图像的正态分布曲线
    medical_normal = stats.norm.pdf(x, medical_mean, medical_std)
    ax1.plot(x, medical_normal, 'r-', linewidth=2, label='医学图像正态分布')
    
    # 添加图例和标签
    ax1.legend(fontsize=10)
    ax1.set_title('自然图像与医学图像的数据分布比较', fontsize=16)
    ax1.set_xlabel('像素值', fontsize=12)
    ax1.set_ylabel('概率密度', fontsize=12)
    ax1.grid(alpha=0.3)
    
    # 输出正态性检验结果
    print("\n正态性检验结果:")
    print("自然图像:")
    print(f"  Shapiro-Wilk检验: 统计量={natural_normality['shapiro']['statistic']:.4f}, p值={natural_normality['shapiro']['p_value']:.8f}")
    print(f"  Kolmogorov-Smirnov检验: 统计量={natural_normality['ks']['statistic']:.4f}, p值={natural_normality['ks']['p_value']:.8f}")
    print(f"  结论: {'不符合' if natural_normality['shapiro']['p_value'] < 0.05 else '可能符合'}正态分布 (Shapiro检验)")
    
    print("\n医学图像:")
    print(f"  Shapiro-Wilk检验: 统计量={medical_normality['shapiro']['statistic']:.4f}, p值={medical_normality['shapiro']['p_value']:.8f}")
    print(f"  Kolmogorov-Smirnov检验: 统计量={medical_normality['ks']['statistic']:.4f}, p值={medical_normality['ks']['p_value']:.8f}")
    print(f"  结论: {'不符合' if medical_normality['shapiro']['p_value'] < 0.05 else '可能符合'}正态分布 (Shapiro检验)")
    
    # 在图上添加检验结果
    natural_result = "符合" if natural_normality['shapiro']['p_value'] >= 0.05 else "不符合"
    medical_result = "符合" if medical_normality['shapiro']['p_value'] >= 0.05 else "不符合"
    fig.text(0.02, 0.02, f"自然图像: {natural_result}正态分布 (p={natural_normality['shapiro']['p_value']:.6f})\n"
             f"医学图像: {medical_result}正态分布 (p={medical_normality['shapiro']['p_value']:.6f})",
             fontsize=12)
    
    # 保存图像
    if output_path:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"图像已保存到: {output_path}")
    
    # 显示图像
    plt.tight_layout()
    plt.show()

def main():
    # 默认示例图像路径
    examples_dir = Path("C:\Yan3\Algorithm-version2\Tools\data")
    examples_dir.mkdir(exist_ok=True)
    
    natural_image_path = examples_dir / "5098.jpg_wh860.jpg"
    medical_image_path = examples_dir / "3_L_07.bmp"
    output_path = examples_dir / "distribution_comparison.png"
    
    # 检查示例图像是否存在
    if not natural_image_path.exists() or not medical_image_path.exists():
        print(f"请将自然图像保存为 {natural_image_path} 和医学图像保存为 {medical_image_path}")
        print("或者修改代码中的图像路径")
        return
    
    # 绘制分布
    plot_distributions(natural_image_path, medical_image_path, output_path)

if __name__ == "__main__":
    main()
