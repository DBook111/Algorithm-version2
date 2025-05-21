import os
import tempfile
import argparse
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import io

def compress_pdf(input_file, output_file, quality=30):
    """
    压缩PDF文件
    
    参数:
        input_file: 输入PDF文件路径
        output_file: 输出PDF文件路径
        quality: 图像质量 (0-100, 默认30)
    """
    reader = PdfReader(input_file)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    
    for i, page in enumerate(reader.pages):
        print(f"正在处理页面 {i+1}/{total_pages}...")
        page_obj = page
        writer.add_page(page_obj)
        
        for j, image_file_object in enumerate(page.images):
            # 提取图片
            image = Image.open(io.BytesIO(image_file_object.data))
            
            # 转换成RGB模式（如果是RGBA）
            if image.mode == 'RGBA':
                image = image.convert('RGB')
                
            # 创建临时文件来存储压缩后的图像
            with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as temp:
                image.save(temp, format='JPEG', quality=quality, optimize=True)
            
            # 用压缩后的图像替换原图
            with open(temp.name, 'rb') as img_file:
                img_data = img_file.read()
                page_obj.replace_image(image_file_object.name, img_data)
            
            # 删除临时文件
            os.unlink(temp.name)
    
    # 保存压缩后的PDF
    with open(output_file, 'wb') as output:
        writer.write(output)
    
    original_size = os.path.getsize(input_file) / (1024 * 1024)
    compressed_size = os.path.getsize(output_file) / (1024 * 1024)
    print(f"原始文件大小: {original_size:.2f} MB")
    print(f"压缩后文件大小: {compressed_size:.2f} MB")
    print(f"压缩率: {(1 - compressed_size/original_size) * 100:.2f}%")

def main():
    parser = argparse.ArgumentParser(description='压缩PDF文件')
    parser.add_argument('input', nargs='?', default=r'C:\Yan3\Algorithm-version2\Tools\online.pdf', help='输入PDF文件路径 (默认: input.pdf)')
    parser.add_argument('-o', '--output', default='C:\Yan3\Algorithm-version2\Tools', help='输出PDF文件路径 (默认: compressed_输入文件名)')
    parser.add_argument('-q', '--quality', type=int, default=30, help='图像质量 (0-100, 默认: 30)')
    
    args = parser.parse_args()
    
    input_file = args.input
    output_file = args.output if args.output else f"compressed_{os.path.basename(input_file)}"
    
    compress_pdf(input_file, output_file, args.quality)
    print(f"PDF已压缩并保存为: {output_file}")

if __name__ == "__main__":
    main()
