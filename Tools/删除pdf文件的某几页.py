import os
from PyPDF2 import PdfReader, PdfWriter

def delete_pages_from_pdf(input_path, output_path, pages_to_delete):
    """
    从PDF文件中删除指定页面，并保存到新的位置
    
    参数:
        input_path: 输入PDF文件的路径
        output_path: 输出PDF文件的路径
        pages_to_delete: 要删除的页面列表（页码从1开始）
    """
    # 确保输出目录存在
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 转换为从0开始的索引
    zero_based_pages = [page - 1 for page in pages_to_delete]
    
    # 读取PDF文件
    pdf_reader = PdfReader(input_path)
    pdf_writer = PdfWriter()
    
    # 添加除了要删除的页面外的所有页面
    for page_num in range(len(pdf_reader.pages)):
        if page_num not in zero_based_pages:
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
    
    # 写入新的PDF文件
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)
    
    print(f"已成功从PDF中删除指定页面，新文件已保存至: {output_path}")

# 使用示例
if __name__ == "__main__":
    # 示例：删除第2, 4, 6页
    input_pdf = ""
    output_pdf = ""
    delete_pages_from_pdf(input_pdf, output_pdf, [11])
