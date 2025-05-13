import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim


def process_one_img(image_path, output_folder):
    class_name = image_path.split('\\')[-1].split('.')[0]
    # 读取灰度图像
    # img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_GRAYSCALE)


    # 自定义 Sobel 卷积核
    sobel_kernel_x = np.array([[1, 0, -1],
                            [1, 0, -1],
                            [1, 0, -1]], dtype=np.float32)

    sobel_kernel_y = np.array([[1, 1, 1],
                            [0, 0, 0],
                            [-1, -1, -1]], dtype=np.float32)

    # 使用自定义卷积核计算梯度
    sobelx = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_x)
    sobely = cv2.filter2D(img, cv2.CV_64F, sobel_kernel_y)

    # 分别计算 x 和 y 梯度，取加权和
    # slbelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

    # 输出统计信息
    print(f"Min value: {sobelx.min()}, Max value: {sobelx.max()}")
    print(f"Mean value: {sobelx.mean()}, Std Dev: {sobelx.std()}")

    # 手动裁剪掉边缘像素 (适配无填充输出尺寸)
    crop_size = 1  # 卷积核大小为 3x3 时，每边裁剪 (3-1)/2 = 1 像素
    sobelx_cropped = sobelx[crop_size:-crop_size, crop_size:-crop_size]
    sobely_cropped = sobely[crop_size:-crop_size, crop_size:-crop_size]


    # 将结果归一化到 0-255 范围
    normalized_sobelx = cv2.normalize(sobelx_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    normalized_sobely = cv2.normalize(sobely_cropped, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # # 将结果归一化到 0-255 范围
    # normalized_sobelx = cv2.normalize(sobelx, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    # normalized_sobely = cv2.normalize(sobely, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    # normalized_slbelz = cv2.normalize(sobelz, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # 保存到指定文件夹
    output_path_1 = os.path.join(output_folder, f"{class_name}_kernel_1.png")
    output_path_2 = os.path.join(output_folder, f"{class_name}_kernel_2.png")

    # cv2.imwrite(output_path_1, normalized_sobelx)
    # cv2.imwrite(output_path_2, normalized_sobely)
    _, buf1 = cv2.imencode('.png', normalized_sobelx)
    _, buf2 = cv2.imencode('.png', normalized_sobely)
    buf1.tofile(output_path_1)
    buf2.tofile(output_path_2)


    print(f'{class_name} finished!')

if __name__ == '__main__':
    # img_path = "D:\SoftWare\BaiduNetdisk\BaiduNetdiskDownload\cifar_png\cifar\\test\\13_horse.png"
    # img_path = "D:\SoftWare\BaiduNetdisk\BaiduNetdiskDownload\cifar_png\cifar\\test\\10_airplane.png"
    # img_path = r"C:\\Yan3\\Algorithm-version2\\CaiLiaoCode\\13_horse.png"
    input_folder = r"C:\Yan3\与材料学院合作\第二波\COCO"
    output_folder = r"C:\Yan3\与材料学院合作\第二波\Output\CoCo"
    os.makedirs(output_folder, exist_ok=True)
    imgs = os.listdir(input_folder)
    for img in imgs:
        img_path = os.path.join(input_folder, img)
        process_one_img(image_path=img_path, output_folder=output_folder)