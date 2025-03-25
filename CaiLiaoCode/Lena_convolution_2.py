import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

# img_path = "D:\SoftWare\BaiduNetdisk\BaiduNetdiskDownload\cifar_png\cifar\\test\\13_horse.png"
# img_path = "D:\SoftWare\BaiduNetdisk\BaiduNetdiskDownload\cifar_png\cifar\\test\\10_airplane.png"
img_path = "C:\\Yan3\\Algorithm-version2\\CaiLiaoCode\\13_horse.png"
class_name = img_path.split('\\')[-1].split('_')[1].split('.')[0]
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
                           [1.75e-11, 1.75e-11, 1.75e-11],
                           [-1.80e-10, -1.80e-10, -1.80e-10]], dtype=np.float32)

sobel_kernel_z_industry_2 = np.array([[1.75e-10, 1.75e-10, 1.75e-10],
                           [1.75e-10, 1.80e-10, 1.75e-10],
                           [1.75e-10, 1.75e-10, -1.80e-10]], dtype=np.float32)


# # 3
# sobel_kernel_x_industry = np.array([[1.125e-9, 2.3731e-11, -1.125e-9],
#                            [1.125e-9, 2.3731e-11, -1.125e-9],
#                            [1.125e-9, 2.3731e-11, -1.125e-9]], dtype=np.float32)

# sobel_kernel_y_industry = np.array([[1.125e-9, 1.125e-9, 1.125e-9],
#                            [2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [-1.125e-9, -1.125e-9, -1.125e-9]], dtype=np.float32)

# sobel_kernel_z_industry =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [2.3731e-11, 1.125e-9, 2.3731e-11],
#                            [2.3731e-11, 2.3731e-11, -1.125e-9]], dtype=np.float32)

# # 4
# sobel_kernel_x_industry = np.array([[1.771e-9, 2.3731e-11, -1.771e-9],
#                            [1.771e-9, 2.3731e-11, -1.771e-9],
#                            [1.771e-9, 2.3731e-11, -1.771e-9]], dtype=np.float32)

# sobel_kernel_y_industry = np.array([[1.771e-9, 1.771e-9, 1.771e-9],
#                            [2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [-1.771e-9, -1.771e-9, -1.771e-9]], dtype=np.float32)

# sobel_kernel_z_industry =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [2.3731e-11, 1.771e-9, 2.3731e-11],
#                            [2.3731e-11, 2.3731e-11, -1.771e-9]], dtype=np.float32)

# # 5
# sobel_kernel_x_industry = np.array([[2.161e-9, 2.3731e-11, -2.161e-9],
#                            [2.161e-9, 2.3731e-11, -2.161e-9],
#                            [2.161e-9, 2.3731e-11, -2.161e-9]], dtype=np.float32)

# sobel_kernel_y_industry = np.array([[2.161e-9, 2.161e-9, 2.161e-9],
#                            [2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [-2.161e-9, -2.161e-9, -2.161e-9]], dtype=np.float32)

# sobel_kernel_z_industry =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [2.3731e-11, 2.161e-9, 2.3731e-11],
#                            [2.3731e-11, 2.3731e-11, -2.161e-9]], dtype=np.float32)

# # 6
# sobel_kernel_x_industry = np.array([[2.161e-9, 2.3731e-11, -2.161e-9],
#                            [2.161e-9, 2.3731e-11, -2.161e-9],
#                            [2.161e-9, 2.3731e-11, -2.161e-9]], dtype=np.float32)

# sobel_kernel_y_industry = np.array([[2.161e-9, 2.161e-9, 2.161e-9],
#                            [2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [-2.161e-9, -2.161e-9, -2.161e-9]], dtype=np.float32)

# sobel_kernel_z_industry =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [2.3731e-11, 2.161e-9, 2.3731e-11],
#                            [2.3731e-11, 2.3731e-11, -2.161e-9]], dtype=np.float32)


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
# combined_sobel = np.stack((sobelx_industry_cropped_1, 
#                            sobely_industry_cropped_1,
#                            sobelz_industry_cropped_1,
#                            sobelx_industry_cropped_2,
#                            sobely_industry_cropped_2,
#                            sobelz_industry_cropped_2), axis=-1)

# 将结果归一化到 0-255 范围
normalized_sobelx = cv2.normalize(sobelx_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobely = cv2.normalize(sobely_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobelz = cv2.normalize(sobelz_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

normalized_sobelx_industry_1 = cv2.normalize(sobelx_industry_cropped_1, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobely_industry_1 = cv2.normalize(sobely_industry_cropped_1, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobelz_industry_1 = cv2.normalize(sobelz_industry_cropped_1, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobelx_industry_2 = cv2.normalize(sobelx_industry_cropped_2, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobely_industry_2 = cv2.normalize(sobely_industry_cropped_2, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobelz_industry_2 = cv2.normalize(sobelz_industry_cropped_2, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# normalized_combined_sobel = cv2.normalize(combined_sobel, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# normalized_sobelx_industry_1 = normalized_combined_sobel[..., 0]
# normalized_sobely_industry_1 = normalized_combined_sobel[..., 1]
# normalized_sobelz_industry_1 = normalized_combined_sobel[..., 2]
# normalized_sobelx_industry_2 = normalized_combined_sobel[..., 3]
# normalized_sobely_industry_2 = normalized_combined_sobel[..., 4]
# normalized_sobelz_industry_2 = normalized_combined_sobel[..., 5]

# # 计算 结构相似性指数ssim
# ssim_x_1 = ssim(normalized_sobelx, normalized_sobelx_industry_1, data_range=normalized_sobelx.max() - normalized_sobelx.min())
# ssim_y_1 = ssim(normalized_sobely, normalized_sobely_industry_1, data_range=normalized_sobely.max() - normalized_sobely.min())
# ssim_z_1 = ssim(normalized_sobelz, normalized_sobelz_industry_1, data_range=normalized_sobelz.max() - normalized_sobelz.min())
# ssim_x_2 = ssim(normalized_sobelx, normalized_sobelx_industry_2, data_range=normalized_sobelx.max() - normalized_sobelx.min() )
# ssim_y_2 = ssim(normalized_sobely, normalized_sobely_industry_2, data_range=normalized_sobely.max() - normalized_sobely.min())
# ssim_z_2 = ssim(normalized_sobelz, normalized_sobelz_industry_2, data_range=normalized_sobelz.max() - normalized_sobelz.min())

ssim_x_1 = ssim(normalized_sobelx, normalized_sobelx_industry_1, data_range=normalized_sobelx_industry_1.max() - normalized_sobelx_industry_1.min())
ssim_y_1 = ssim(normalized_sobely, normalized_sobely_industry_1, data_range=normalized_sobely_industry_1.max() - normalized_sobely_industry_1.min())
ssim_z_1 = ssim(normalized_sobelz, normalized_sobelz_industry_1, data_range=normalized_sobelz_industry_1.max() - normalized_sobelz_industry_1.min())
ssim_x_2 = ssim(normalized_sobelx, normalized_sobelx_industry_2, data_range=normalized_sobelx_industry_2.max() - normalized_sobelx_industry_2.min())
ssim_y_2 = ssim(normalized_sobely, normalized_sobely_industry_2, data_range=normalized_sobely_industry_2.max() - normalized_sobely_industry_2.min())
ssim_z_2 = ssim(normalized_sobelz, normalized_sobelz_industry_2, data_range=normalized_sobelz_industry_2.max() - normalized_sobelz_industry_2.min())


# # 将结果归一化到 0-255 范围
# normalized_sobelx = cv2.normalize(sobelx, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# normalized_sobely = cv2.normalize(sobely, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# normalized_slbelz = cv2.normalize(sobelz, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 保存到指定文件夹
cv2.imwrite(f"C:\\Yan3\\Algorithm-version2\\CaiLiaoCode\\sobelx_{class_name}.png", normalized_sobelx)
cv2.imwrite(f"C:\\Yan3\\Algorithm-version2\\CaiLiaoCode\\sobelx_industry_{class_name}_1.png", normalized_sobelx_industry_1)
cv2.imwrite(f"C:\\Yan3\\Algorithm-version2\\CaiLiaoCode\\sobelx_industry_{class_name}_2.png", normalized_sobelx_industry_2)
cv2.imwrite(f"C:\\Yan3\\Algorithm-version2\\CaiLiaoCode\\sobely_{class_name}.png", normalized_sobely)
cv2.imwrite(f"C:\\Yan3\\Algorithm-version2\\CaiLiaoCode\\sobely_industry_{class_name}_1.png", normalized_sobely_industry_1)
cv2.imwrite(f"C:\\Yan3\\Algorithm-version2\\CaiLiaoCode\\sobely_industry_{class_name}_2.png", normalized_sobely_industry_2)
cv2.imwrite(f"C:\\Yan3\\Algorithm-version2\\CaiLiaoCode\\slbelz_{class_name}.png", normalized_sobelz)
cv2.imwrite(f"C:\\Yan3\\Algorithm-version2\\CaiLiaoCode\\slbelz_industry_{class_name}_1.png", normalized_sobelz_industry_1)
cv2.imwrite(f"C:\\Yan3\\Algorithm-version2\\CaiLiaoCode\\slbelz_industry_{class_name}_2.png", normalized_sobelz_industry_2)


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
    plt.text(0.5, 0.5, text_contents[row], ha='center', va='center', fontsize=12)

# # 显示最后一张图
# plt.subplot((len(result) + 2) // 3, 4, len(result) + 1)  # 放在最后一个可用的格子
# plt.imshow(result[-1], cmap='gray')
# plt.title(titles[-1])
# plt.xticks([]), plt.yticks([])

# 调整子图间距
plt.tight_layout()
plt.savefig(f"C:\\Yan3\\Algorithm-version2\\CaiLiaoCode\\mix_{class_name}.png", dpi=600)
plt.show()