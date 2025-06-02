import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

Combination_name = "Combination_4" # Combination_1, Combination_2, Combination_3, Combination_4

# img_path = r"C:\Yan3\Algorithm-version2\CaiLiaoCode\input\235_airplane.png"
# img_path = r"C:\Yan3\Algorithm-version2\CaiLiaoCode\input\330_automobile.png"
img_path = r"C:\Yan3\Algorithm-version2\CaiLiaoCode\input\000000005836.jpg"
class_name = img_path.split('\\')[-1].split('.')[0]
# 读取灰度图像
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
# cv2.imwrite(f"D:\\gray_{class_name}.png", img)


# 自定义 Sobel 卷积核
sobel_kernel_x = np.array([[1, 0, -1],
                           [1, 0, -1],
                           [1, 0, -1]], dtype=np.float32)

sobel_kernel_y = np.array([[1, 1, 1],
                           [0, 0, 0],
                           [-1, -1, -1]], dtype=np.float32)

sobel_kernel_z =  np.array([[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, -1]], dtype=np.float32)

if Combination_name == "Combination_1":
    # 1 外延
    sobel_kernel_x_industry_1 = np.array([[1.108e-10, 2.3731e-11, -1.108e-10],
                            [1.108e-10, 2.3731e-11, -1.108e-10],
                            [1.108e-10, 2.3731e-11, -1.108e-10]], dtype=np.float32)

    sobel_kernel_y_industry_1 = np.array([[1.108e-10, 1.108e-10, 1.108e-10],
                            [2.3731e-11, 2.3731e-11, 2.3731e-11],
                            [-1.108e-10, -1.108e-10, -1.108e-10]], dtype=np.float32)

    sobel_kernel_z_industry_1 =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
                            [2.3731e-11, 1.108e-10, 2.3731e-11],
                            [2.3731e-11, 2.3731e-11, -1.108e-10]], dtype=np.float32)
    # 2 非外延
    sobel_kernel_x_industry_2 = np.array([[1.80e-10, 1.75e-10, -1.80e-10],
                            [1.80e-10, 1.75e-10, -1.80e-10],
                            [1.80e-10,1.75e-10, -1.80e-10]], dtype=np.float32)

    sobel_kernel_y_industry_2 = np.array([[1.80e-10, 1.80e-10, 1.80e-10],
                            [1.75e-10, 1.75e-10, 1.75e-10],
                            [-1.80e-10, -1.80e-10, -1.80e-10]], dtype=np.float32)

    sobel_kernel_z_industry_2 = np.array([[1.75e-10, 1.75e-10, 1.75e-10],
                            [1.75e-10, 1.80e-10, 1.75e-10],
                            [1.75e-10, 1.75e-10, -1.80e-10]], dtype=np.float32)
elif Combination_name == "Combination_2":
    # 1 外延
    sobel_kernel_x_industry_1 = np.array([[2.738e-10, 2.3731e-11, -2.738e-10],
                            [2.738e-10, 2.3731e-11, -2.738e-10],
                            [2.738e-10, 2.3731e-11, -2.738e-10]], dtype=np.float32)

    sobel_kernel_y_industry_1 = np.array([[2.738e-10, 2.738e-10, 2.738e-10],
                            [2.3731e-11, 2.3731e-11, 2.3731e-11],
                            [-2.738e-10, -2.738e-10, -2.738e-10]], dtype=np.float32)

    sobel_kernel_z_industry_1 =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
                            [2.3731e-11, 2.738e-10, 2.3731e-11],
                            [2.3731e-11, 2.3731e-11, -2.738e-10]], dtype=np.float32)

    # 2 非外延
    sobel_kernel_x_industry_2 = np.array([[2.16e-10, 1.75e-10, -2.16e-10],
                           [2.16e-10, 1.75e-10, -2.16e-10],
                           [2.16e-10,1.75e-10, -2.16e-10]], dtype=np.float32)

    sobel_kernel_y_industry_2 = np.array([[2.16e-10, 2.16e-10, 2.16e-10],
                            [1.75e-10, 1.75e-10, 1.75e-10],
                            [-2.16e-10, -2.16e-10, -2.16e-10]], dtype=np.float32)

    sobel_kernel_z_industry_2 = np.array([[1.75e-10, 1.75e-10, 1.75e-10],
                            [1.75e-10, 2.16e-10, 1.75e-10],
                            [1.75e-10, 1.75e-10, -2.16e-10]], dtype=np.float32)
elif Combination_name == "Combination_3":
    # 1 外延
    sobel_kernel_x_industry_1 = np.array([[1.125e-9, 2.3731e-11, -1.125e-9],
                            [1.125e-9, 2.3731e-11, -1.125e-9],
                            [1.125e-9, 2.3731e-11, -1.125e-9]], dtype=np.float32)

    sobel_kernel_y_industry_1 = np.array([[1.125e-9, 1.125e-9, 1.125e-9],
                            [2.3731e-11, 2.3731e-11, 2.3731e-11],
                            [-1.125e-9, -1.125e-9, -1.125e-9]], dtype=np.float32)

    sobel_kernel_z_industry_1 =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
                            [2.3731e-11, 1.125e-9, 2.3731e-11],
                            [2.3731e-11, 2.3731e-11, -1.125e-9]], dtype=np.float32)
    # 2 非外延
    sobel_kernel_x_industry_2 = np.array([[6.04e-10, 1.75e-10, -6.04e-10],
                           [6.04e-10, 1.75e-10, -6.04e-10],
                           [6.04e-10,1.75e-10, -6.04e-10]], dtype=np.float32)

    sobel_kernel_y_industry_2 = np.array([[6.04e-10, 6.04e-10, 6.04e-10],
                            [1.75e-10, 1.75e-10, 1.75e-10],
                            [-6.04e-10, -6.04e-10, -6.04e-10]], dtype=np.float32)

    sobel_kernel_z_industry_2 = np.array([[1.75e-10, 1.75e-10, 1.75e-10],
                            [1.75e-10, 6.04e-10, 1.75e-10],
                            [1.75e-10, 1.75e-10, -6.04e-10]], dtype=np.float32)
elif Combination_name == "Combination_4":
    # 1 外延
    sobel_kernel_x_industry_1 = np.array([[1.771e-9, 2.3731e-11, -1.771e-9],
                           [1.771e-9, 2.3731e-11, -1.771e-9],
                           [1.771e-9, 2.3731e-11, -1.771e-9]], dtype=np.float32)

    sobel_kernel_y_industry_1 = np.array([[1.771e-9, 1.771e-9, 1.771e-9],
                            [2.3731e-11, 2.3731e-11, 2.3731e-11],
                            [-1.771e-9, -1.771e-9, -1.771e-9]], dtype=np.float32)

    sobel_kernel_z_industry_1 =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
                            [2.3731e-11, 1.771e-9, 2.3731e-11],
                            [2.3731e-11, 2.3731e-11, -1.771e-9]], dtype=np.float32)
    # 2 非外延
    sobel_kernel_x_industry_2 = np.array([[1.06e-9, 1.75e-10, -1.06e-9],
                           [1.06e-9, 1.75e-10, -1.06e-9],
                           [1.06e-9,1.75e-10, -1.06e-9]], dtype=np.float32)

    sobel_kernel_y_industry_2 = np.array([[1.06e-9, 1.06e-9, 1.06e-9],
                            [1.75e-10, 1.75e-10, 1.75e-10],
                            [-1.06e-9, -1.06e-9, -1.06e-9]], dtype=np.float32)

    sobel_kernel_z_industry_2 = np.array([[1.75e-10, 1.75e-10, 1.75e-10],
                            [1.75e-10, 1.06e-9, 1.75e-10],
                            [1.75e-10, 1.75e-10, -1.06e-9]], dtype=np.float32)
else:
    raise ValueError(f"Combination_name: {Combination_name} is not valid")



# 使用自定义卷积核计算梯度
sobelx = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_x)
sobely = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_y)
sobelz = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_z)

sobelx_industry_1 = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_x_industry_1)
sobely_industry_1 = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_y_industry_1)
sobelz_industry_1 = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_z_industry_1)

sobelx_industry_2 = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_x_industry_2)
sobely_industry_2 = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_y_industry_2)
sobelz_industry_2 = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_z_industry_2)

# 分别计算 x 和 y 梯度，取加权和
# slbelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# 输出统计信息
print(f"Min value: {sobelx.min()}, Max value: {sobelx.max()}")
print(f"Mean value: {sobelx.mean()}, Std Dev: {sobelx.std()}")

# 手动裁剪掉边缘像素 (适配无填充输出尺寸)
crop_size = 1  # 卷积核大小为 3x3 时，每边裁剪 (3-1)/2 = 1 像素
sobelx_cropped = sobelx[crop_size:-crop_size, crop_size:-crop_size]
sobely_cropped = sobely[crop_size:-crop_size, crop_size:-crop_size]
sobelz_cropped = sobelz[crop_size:-crop_size, crop_size:-crop_size]

crop_size = 1  # 卷积核大小为 3x3 时，每边裁剪 (3-1)/2 = 1 像素
sobelx_industry_cropped_1 = sobelx_industry_1[crop_size:-crop_size, crop_size:-crop_size]
sobely_industry_cropped_1 = sobely_industry_1[crop_size:-crop_size, crop_size:-crop_size]
sobelz_industry_cropped_1 = sobelz_industry_1[crop_size:-crop_size, crop_size:-crop_size]

sobelx_industry_cropped_2 = sobelx_industry_2[crop_size:-crop_size, crop_size:-crop_size]
sobely_industry_cropped_2 = sobely_industry_2[crop_size:-crop_size, crop_size:-crop_size]
sobelz_industry_cropped_2 = sobelz_industry_2[crop_size:-crop_size, crop_size:-crop_size]

# # 计算 结构相似性指数ssim
# ssim_x_1 = ssim(sobelx_cropped, sobelx_industry_cropped_1, data_range=sobelx_cropped.max() - sobelx_industry_cropped_1.min())
# ssim_y_1 = ssim(sobely_cropped, sobely_industry_cropped_1, data_range=sobely_cropped.max() - sobely_industry_cropped_1.min())
# ssim_z_1 = ssim(sobelz_cropped, sobelz_industry_cropped_1, data_range=sobelz_cropped.max() - sobelz_industry_cropped_1.min())
# ssim_x_2 = ssim(sobelx_cropped, sobelx_industry_cropped_2, data_range=sobelx_cropped.max() - sobelx_industry_cropped_2.min())
# ssim_y_2 = ssim(sobely_cropped, sobely_industry_cropped_2, data_range=sobely_cropped.max() - sobely_industry_cropped_2.min())
# ssim_z_2 = ssim(sobelz_cropped, sobelz_industry_cropped_2, data_range=sobelz_cropped.max() - sobelz_industry_cropped_2.min())

# 合并六个数组
# 由于已经单独归一化每个数组，不再需要这一步
# combined_sobel = np.stack((sobelx_industry_cropped_1, 
#                          sobely_industry_cropped_1,
#                          sobelz_industry_cropped_1,
#                          sobelx_industry_cropped_2,
#                          sobely_industry_cropped_2,
#                          sobelz_industry_cropped_2), axis=-1)

# 将结果归一化到 0-255 范围
normalized_sobelx = cv2.normalize(sobelx_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobely = cv2.normalize(sobely_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobelz = cv2.normalize(sobelz_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 分别归一化每个工业版Sobel结果
normalized_sobelx_industry_1 = cv2.normalize(sobelx_industry_cropped_1, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobely_industry_1 = cv2.normalize(sobely_industry_cropped_1, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobelz_industry_1 = cv2.normalize(sobelz_industry_cropped_1, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobelx_industry_2 = cv2.normalize(sobelx_industry_cropped_2, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobely_industry_2 = cv2.normalize(sobely_industry_cropped_2, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobelz_industry_2 = cv2.normalize(sobelz_industry_cropped_2, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 计算结构相似性指数SSIM，对每对图像使用其共同的数据范围
ssim_x_1 = ssim(normalized_sobelx, normalized_sobelx_industry_1, data_range=255)
ssim_y_1 = ssim(normalized_sobely, normalized_sobely_industry_1, data_range=255)
ssim_z_1 = ssim(normalized_sobelz, normalized_sobelz_industry_1, data_range=255)
ssim_x_2 = ssim(normalized_sobelx, normalized_sobelx_industry_2, data_range=255)
ssim_y_2 = ssim(normalized_sobely, normalized_sobely_industry_2, data_range=255)
ssim_z_2 = ssim(normalized_sobelz, normalized_sobelz_industry_2, data_range=255)

# 保存到指定文件夹
save_name = os.path.split(img_path)[-1].split('.')[0]
current_dir = os.path.dirname(os.path.abspath(__file__))
result_dir = os.path.join(current_dir, 'save_result', Combination_name, save_name)
show_kernels = os.path.join(current_dir, 'save_result', Combination_name)
os.makedirs(result_dir, exist_ok=True)

# 将卷积核可视化为矩阵图像并保存
def create_kernel_comparison(kernels, titles, filename):
    rows = 3  # X, Y, Z方向
    cols = 3  # 标准, 外延, 非外延
    
    plt.figure(figsize=(15, 12))
    
    for i in range(len(kernels)):
        plt.subplot(rows, cols, i+1)
        ax = plt.gca()
        im = ax.imshow(kernels[i], cmap='viridis')
        
        # 添加数值标签到每个单元格
        for r in range(kernels[i].shape[0]):
            for c in range(kernels[i].shape[1]):
                value = kernels[i][r, c]
                if abs(value) < 0.001:
                    # 科学计数法显示小数，保留四位有效数字
                    text = f'{value:.4g}'
                else:
                    # 保留四位有效数字
                    text = f'{value:.4g}'
                ax.text(c, r, text, ha='center', va='center', 
                       color='white' if abs(value) > 0.0001 else 'black',
                       fontsize=8)
        
        plt.title(titles[i])
        plt.colorbar(im)
    
    plt.tight_layout()
    plt.savefig(filename, dpi=600)
    plt.close()

# 创建所有卷积核的比较图
all_kernels = [
    sobel_kernel_x, sobel_kernel_x_industry_1, sobel_kernel_x_industry_2,
    sobel_kernel_y, sobel_kernel_y_industry_1, sobel_kernel_y_industry_2,
    sobel_kernel_z, sobel_kernel_z_industry_1, sobel_kernel_z_industry_2
]
all_titles = [
    'Standard Sobel X', 'WaiYan Sobel X', 'FeiWaiYan Sobel X',
    'Standard Sobel Y', 'WaiYan Sobel Y', 'FeiWaiYan Sobel Y',
    'Standard Sobel Z', 'WaiYan Sobel Z', 'FeiWaiYan Sobel Z'
]
create_kernel_comparison(all_kernels, all_titles, os.path.join(show_kernels, 'all_kernels.png'))

cv2.imwrite(os.path.join(result_dir, f"sobelx_{class_name}.png"), normalized_sobelx)
cv2.imwrite(os.path.join(result_dir, f"sobelx_industry_{class_name}_1.png"), normalized_sobelx_industry_1)
cv2.imwrite(os.path.join(result_dir, f"sobelx_industry_{class_name}_2.png"), normalized_sobelx_industry_2)
cv2.imwrite(os.path.join(result_dir, f"sobely_{class_name}.png"), normalized_sobely)
cv2.imwrite(os.path.join(result_dir, f"sobely_industry_{class_name}_1.png"), normalized_sobely_industry_1)
cv2.imwrite(os.path.join(result_dir, f"sobely_industry_{class_name}_2.png"), normalized_sobely_industry_2)
cv2.imwrite(os.path.join(result_dir, f"sobelz_{class_name}.png"), normalized_sobelz)
cv2.imwrite(os.path.join(result_dir, f"sobelz_industry_{class_name}_1.png"), normalized_sobelz_industry_1)
cv2.imwrite(os.path.join(result_dir, f"sobelz_industry_{class_name}_2.png"), normalized_sobelz_industry_2)


# 显示结果
result = [normalized_sobelx, normalized_sobelx_industry_1, normalized_sobelx_industry_2,
          normalized_sobely, normalized_sobely_industry_1, normalized_sobely_industry_2,
          normalized_sobelz, normalized_sobelz_industry_1, normalized_sobelz_industry_2]
titles = ['Sobel X', 'Sobel X Industry 1', 'Sobel X Industry 2',
          'Sobel Y', 'Sobel Y Industry 1', 'Sobel Y Industry 2',
          'Sobel Z', 'Sobel Z Industry 1', 'Sobel Z Industry 2']
text_contents = [
    f'SSIM X Industry 1: {ssim_x_1:.4f}',
    f'SSIM X Industry 2: {ssim_x_2:.4f}',
    f'SSIM Y Industry 1: {ssim_y_1:.4f}',
    f'SSIM Y Industry 2: {ssim_y_2:.4f}',
    f'SSIM Z Industry 1: {ssim_z_1:.4f}',
    f'SSIM Z Industry 2: {ssim_z_2:.4f}'
]

# 将文本内容重新组合为3个双行文本
combined_text = [
    f'SSIM X WaiYan: {ssim_x_1:.4f}\nSSIM X FeiWaiYan: {ssim_x_2:.4f}',
    f'SSIM Y WaiYan: {ssim_y_1:.4f}\nSSIM Y FeiWaiYan: {ssim_y_2:.4f}',
    f'SSIM Z WaiYan: {ssim_z_1:.4f}\nSSIM Z FeiWaiYan: {ssim_z_2:.4f}'
]

print(text_contents)

# 设置图像显示区域大小
plt.figure(figsize=(15, 15))

# 每行的图像和文字
for i in range(0, len(result) - 1, 3):  # 每次处理三张图
    row = i // 3  # 当前行数

    # 左图
    plt.subplot((len(result) + 2) // 3, 4, row * 4 + 1)  # 每行占四格
    plt.imshow(result[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

    # 中间图
    plt.subplot((len(result) + 2) // 3, 4, row * 4 + 2)  # 中间图
    plt.imshow(result[i + 1], cmap='gray')
    plt.title(titles[i + 1])
    plt.xticks([]), plt.yticks([])

    # 右图
    plt.subplot((len(result) + 2) // 3, 4, row * 4 + 3)  # 右图
    plt.imshow(result[i + 2], cmap='gray')
    plt.title(titles[i + 2])
    plt.xticks([]), plt.yticks([])

    # 插入文字
    plt.subplot((len(result) + 2) // 3, 4, row * 4 + 4)  # 最右列放文字
    plt.axis('off')  # 不显示坐标轴
    plt.text(0.5, 0.5, combined_text[row], ha='center', va='center', fontsize=12)

# # 显示最后一张图
# plt.subplot((len(result) + 2) // 3, 4, len(result) + 1)  # 放在最后一个可用的格子
# plt.imshow(result[-1], cmap='gray')
# plt.title(titles[-1])
# plt.xticks([]), plt.yticks([])

# 调整子图间距
plt.tight_layout()
plt.savefig(os.path.join(result_dir, f"mix_{class_name}.png"), dpi=600)
# plt.show()
print('finish!')