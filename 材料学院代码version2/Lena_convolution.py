import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

# img_path = "D:\SoftWare\BaiduNetdisk\BaiduNetdiskDownload\cifar_png\cifar\\test\\13_horse.png"
# img_path = "D:\SoftWare\BaiduNetdisk\BaiduNetdiskDownload\cifar_png\cifar\\test\\10_airplane.png"
img_path = r"C:\Yan3\Algorithm-version2\材料学院代码version2\13_horse.png"
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
# 1
sobel_kernel_x_industry = np.array([[1.108e-10, 2.3731e-11, -1.108e-10],
                           [1.108e-10, 2.3731e-11, -1.108e-10],
                           [1.108e-10, 2.3731e-11, -1.108e-10]], dtype=np.float32)

sobel_kernel_y_industry = np.array([[1.108e-10, 1.108e-10, 1.108e-10],
                           [2.3731e-11, 2.3731e-11, 2.3731e-11],
                           [-1.108e-10, -1.108e-10, -1.108e-10]], dtype=np.float32)

sobel_kernel_z_industry =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
                           [2.3731e-11, 1.108e-10, 2.3731e-11],
                           [2.3731e-11, 2.3731e-11, -1.108e-10]], dtype=np.float32)

# 2
# sobel_kernel_x_industry = np.array([[2.738e-10, 2.3731e-11, -2.738e-10],
#                            [2.738e-10, 2.3731e-11, -2.738e-10],
#                            [2.738e-10, 2.3731e-11, -2.738e-10]], dtype=np.float32)
#
# sobel_kernel_y_industry = np.array([[2.738e-10, 2.738e-10, 2.738e-10],
#                            [2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [-2.738e-10, -2.738e-10, -2.738e-10]], dtype=np.float32)
#
# sobel_kernel_z_industry =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [2.3731e-11, 2.738e-10, 2.3731e-11],
#                            [2.3731e-11, 2.3731e-11, -2.738e-10]], dtype=np.float32)

# 3
# sobel_kernel_x_industry = np.array([[1.125e-9, 2.3731e-11, -1.125e-9],
#                            [1.125e-9, 2.3731e-11, -1.125e-9],
#                            [1.125e-9, 2.3731e-11, -1.125e-9]], dtype=np.float32)
#
# sobel_kernel_y_industry = np.array([[1.125e-9, 1.125e-9, 1.125e-9],
#                            [2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [-1.125e-9, -1.125e-9, -1.125e-9]], dtype=np.float32)
#
# sobel_kernel_z_industry =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [2.3731e-11, 1.125e-9, 2.3731e-11],
#                            [2.3731e-11, 2.3731e-11, -1.125e-9]], dtype=np.float32)

# 4
# sobel_kernel_x_industry = np.array([[1.771e-9, 2.3731e-11, -1.771e-9],
#                            [1.771e-9, 2.3731e-11, -1.771e-9],
#                            [1.771e-9, 2.3731e-11, -1.771e-9]], dtype=np.float32)
#
# sobel_kernel_y_industry = np.array([[1.771e-9, 1.771e-9, 1.771e-9],
#                            [2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [-1.771e-9, -1.771e-9, -1.771e-9]], dtype=np.float32)
#
# sobel_kernel_z_industry =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [2.3731e-11, 1.771e-9, 2.3731e-11],
#                            [2.3731e-11, 2.3731e-11, -1.771e-9]], dtype=np.float32)

# 5
# sobel_kernel_x_industry = np.array([[2.161e-9, 2.3731e-11, -2.161e-9],
#                            [2.161e-9, 2.3731e-11, -2.161e-9],
#                            [2.161e-9, 2.3731e-11, -2.161e-9]], dtype=np.float32)
#
# sobel_kernel_y_industry = np.array([[2.161e-9, 2.161e-9, 2.161e-9],
#                            [2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [-2.161e-9, -2.161e-9, -2.161e-9]], dtype=np.float32)
#
# sobel_kernel_z_industry =  np.array([[2.3731e-11, 2.3731e-11, 2.3731e-11],
#                            [2.3731e-11, 2.161e-9, 2.3731e-11],
#                            [2.3731e-11, 2.3731e-11, -2.161e-9]], dtype=np.float32)


# 使用自定义卷积核计算梯度
sobelx = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_x)
sobely = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_y)
sobelz = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_z)

sobelx_industry = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_x_industry)
sobely_industry = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_y_industry)
sobelz_industry = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_z_industry)


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
sobelx_industry_cropped = sobelx_industry[crop_size:-crop_size, crop_size:-crop_size]
sobely_industry_cropped = sobely_industry[crop_size:-crop_size, crop_size:-crop_size]
sobelz_industry_cropped = sobelz_industry[crop_size:-crop_size, crop_size:-crop_size]


# 将结果归一化到 0-255 范围
normalized_sobelx = cv2.normalize(sobelx_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobely = cv2.normalize(sobely_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobelz = cv2.normalize(sobelz_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

normalized_sobelx_industry = cv2.normalize(sobelx_industry_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobely_industry = cv2.normalize(sobely_industry_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobelz_industry = cv2.normalize(sobelz_industry_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 计算 结构相似性指数ssim
ssim_x = ssim(normalized_sobelx, normalized_sobelx_industry, data_range=normalized_sobelx.max() - normalized_sobelx.min())
ssim_y = ssim(normalized_sobely, normalized_sobely_industry, data_range=normalized_sobely.max() - normalized_sobely.min())
ssim_z = ssim(normalized_sobelz, normalized_sobelz_industry, data_range=normalized_sobelz.max() - normalized_sobelz.min())

# # 将结果归一化到 0-255 范围
# normalized_sobelx = cv2.normalize(sobelx, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# normalized_sobely = cv2.normalize(sobely, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# normalized_slbelz = cv2.normalize(sobelz, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 保存到指定文件夹
cv2.imwrite(f"D:\\sobelx_{class_name}.png", normalized_sobelx)
cv2.imwrite(f"D:\\sobelx_industry_{class_name}.png", normalized_sobelx_industry)
cv2.imwrite(f"D:\\sobely_{class_name}.png", normalized_sobely)
cv2.imwrite(f"D:\\sobely_industry_{class_name}.png", normalized_sobely_industry)
cv2.imwrite(f"D:\\slbelxy_{class_name}.png", normalized_sobelz)
cv2.imwrite(f"D:\\slbelxy_industry_{class_name}.png", normalized_sobelz_industry)


# 显示结果
result = [normalized_sobelx, normalized_sobelx_industry, normalized_sobely, normalized_sobely_industry, normalized_sobelz,  normalized_sobelz_industry, img]
titles = ['left kernel theory', 'left kernel actual', 'middle kernel theory',  'middle kernel actual', 'right kernel theory', 'right kernel actual', 'origin img']
text_contents = [
    f'ssim:{ssim_x}',
    f'ssim:{ssim_y}',
    f'ssim:{ssim_z}'
]
# 设置图像显示区域大小
plt.figure(figsize=(12, 12))

# 每行的图像和文字
for i in range(0, len(result) - 1, 2):  # 每次处理两张图
    row = i // 2  # 当前行数

    # 左图
    plt.subplot((len(result) + 1) // 2, 3, row * 3 + 1)  # 每行占三格
    plt.imshow(result[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

    # 插入文字
    plt.subplot((len(result) + 1) // 2, 3, row * 3 + 2)  # 中间列放文字
    plt.axis('off')  # 不显示坐标轴
    plt.text(0.5, 0.5, text_contents[row], ha='center', va='center', fontsize=12)

    # 右图
    plt.subplot((len(result) + 1) // 2, 3, row * 3 + 3)  # 右图
    plt.imshow(result[i + 1], cmap='gray')
    plt.title(titles[i + 1])
    plt.xticks([]), plt.yticks([])

# 显示最后一张图
plt.subplot((len(result) + 1) // 2, 3, len(result) + 3)  # 放在最后一个可用的格子
plt.imshow(result[-1], cmap='gray')
plt.title(titles[-1])
plt.xticks([]), plt.yticks([])


# 调整子图间距
plt.tight_layout()
plt.savefig(f"D:\\mix_{class_name}.png", dpi=600)
plt.show()
