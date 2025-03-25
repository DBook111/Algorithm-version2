import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取灰度图像
img = cv2.imread("D:\\35931_cat.png", cv2.IMREAD_GRAYSCALE)

# Sobel 运算
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# 分别计算 x 和 y 梯度，取加权和
slbelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# 输出统计信息
print(f"Min value: {slbelxy.min()}, Max value: {slbelxy.max()}")
print(f"Mean value: {slbelxy.mean()}, Std Dev: {slbelxy.std()}")

# 将结果归一化到 0-255 范围
normalized_sobelx = cv2.normalize(sobelx, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_sobely = cv2.normalize(sobely, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
normalized_slbelxy = cv2.normalize(slbelxy, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 保存到指定文件夹
cv2.imwrite("D:\\sobelx_normalized.png", normalized_sobelx)
cv2.imwrite("D:\\sobely_normalized.png", normalized_sobely)
cv2.imwrite("D:\\slbelxy_normalized.png", normalized_slbelxy)
print('yes')
# 显示结果
# result = [img, normalized_sobelx, normalized_sobely, normalized_slbelxy]
# titles = ['origin img', 'sobel x img', 'sobel y img', 'sobel x-y img']
# for i in range(4):
#     plt.subplot(2, 2, i + 1)
#     plt.imshow(result[i], cmap='gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
# plt.show()
