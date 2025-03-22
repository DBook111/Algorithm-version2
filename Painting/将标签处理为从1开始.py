import cv2
import numpy as np

# 读取单通道标签图像
image = cv2.imread(r'C:\Yan3\Algorithm-version2\Painting\RETOUCH\Topcon\label.png'
                   , cv2.IMREAD_GRAYSCALE)

# 获取图像中的唯一像素值
unique_values = np.unique(image)

# 创建一个映射字典，将原始像素值映射到从0开始的值
value_map = {val: idx for idx, val in enumerate(unique_values)}

# 创建一个新的图像，应用映射
new_image = np.zeros_like(image)
for original_value, new_value in value_map.items():
    new_image[image == original_value] = new_value

# 保存处理后的图像
cv2.imwrite(r"C:\Yan3\Algorithm-version2\Painting\RETOUCH\Topcon\new_label.png"
            , new_image)