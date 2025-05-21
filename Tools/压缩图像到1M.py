import os
import sys
from PIL import Image
import io

def compress_image_to_1mb(input_path, output_path=None):
    """
    将图像压缩到接近1M大小
    
    Args:
        input_path: 输入图像路径
        output_path: 输出图像路径，如不指定则在原文件名后添加_compressed
    """
    # 1MB = 1048576 bytes
    target_size = 1048576
    
    # 如果没有指定输出路径，生成默认输出路径
    if output_path is None:
        filename, ext = os.path.splitext(input_path)
        output_path = f"{filename}_compressed{ext}"
    
    # 打开原始图像
    img = Image.open(input_path)
    
    # 保存图像格式，如果是PNG等无损格式，转换为JPEG
    img_format = img.format
    if img_format not in ['JPEG', 'JPG']:
        img = img.convert('RGB')
        img_format = 'JPEG'
        # 如果输出路径没有.jpg或.jpeg后缀，修改它
        if not output_path.lower().endswith(('.jpg', '.jpeg')):
            output_path = os.path.splitext(output_path)[0] + '.jpg'
    
    # 检查原始图像大小
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format=img_format)
    original_size = img_byte_arr.tell()
    
    # 如果原始图像已经小于1MB，无需压缩
    if original_size <= target_size:
        print(f"原始图像已经小于1MB ({original_size / 1024:.2f}KB)，无需压缩")
        img.save(output_path)
        return output_path
    
    # 二分查找法找到合适的质量值
    quality_low = 1
    quality_high = 95  # 最高质量
    best_quality = 0
    best_size = 0
    
    while quality_low <= quality_high:
        quality_mid = (quality_low + quality_high) // 2
        
        # 尝试当前质量值
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format=img_format, quality=quality_mid)
        current_size = img_byte_arr.tell()
        
        print(f"尝试质量: {quality_mid}, 大小: {current_size / 1024:.2f}KB")
        
        # 如果当前大小更接近目标大小，更新最佳值
        if abs(current_size - target_size) < abs(best_size - target_size) or best_size == 0:
            best_quality = quality_mid
            best_size = current_size
        
        # 调整质量范围
        if current_size > target_size:
            quality_high = quality_mid - 1
        else:
            quality_low = quality_mid + 1
    
    # 如果最佳大小还是与目标相差太多，尝试调整图像尺寸
    if abs(best_size - target_size) > target_size * 0.05:  # 允许5%的误差
        print(f"质量调整后仍未达到目标大小，尝试调整图像尺寸")
        
        # 初始缩放因子
        scale_factor = 1.0
        # 根据与目标的差距估计初始缩放因子
        if best_size > target_size:
            scale_factor = 0.9  # 缩小10%
        
        while True:
            # 调整图像尺寸
            new_width = int(img.width * scale_factor)
            new_height = int(img.height * scale_factor)
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            
            # 尝试当前尺寸和最佳质量
            img_byte_arr = io.BytesIO()
            resized_img.save(img_byte_arr, format=img_format, quality=best_quality)
            current_size = img_byte_arr.tell()
            
            print(f"尝试缩放: {scale_factor:.2f}, 尺寸: {new_width}x{new_height}, 大小: {current_size / 1024:.2f}KB")
            
            # 检查是否达到目标大小
            if abs(current_size - target_size) <= target_size * 0.01:  # 允许1%的误差
                img = resized_img
                best_size = current_size
                break
            
            # 更新最佳值
            if abs(current_size - target_size) < abs(best_size - target_size):
                img = resized_img
                best_size = current_size
            
            # 根据当前大小调整缩放因子
            if current_size > target_size:
                scale_factor *= 0.99  # 每次缩小1%
            else:
                scale_factor *= 1.01  # 每次放大1%
            
            # 防止无限循环
            if scale_factor < 0.5 or scale_factor > 2.0:
                break
    
    # 保存最终图像
    img.save(output_path, format=img_format, quality=best_quality)
    
    # 获取最终文件大小
    final_size = os.path.getsize(output_path)
    print(f"压缩完成！最终质量: {best_quality}, 最终大小: {final_size / 1024:.2f}KB")
    
    return output_path

if __name__ == "__main__":
    # 直接指定输入和输出路径
    input_path = r"C:\Yan3\大论文\盲审后要提交的\论文+专利材料\用于oa提交\专利.jpg"
    output_path = None  # 默认使用原文件名+_compressed，或指定为"output.jpg"
    
    if not os.path.exists(input_path):
        print(f"错误: 文件 '{input_path}' 不存在")
    else:
        try:
            result_path = compress_image_to_1mb(input_path, output_path)
            print(f"已保存到: {result_path}")
        except Exception as e:
            print(f"处理时出错: {e}")
