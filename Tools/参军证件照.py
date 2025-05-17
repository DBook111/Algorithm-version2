import os
import sys
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def process_photo(input_path, output_path=None):
    """
    处理证件照片，使其符合规定要求
    - 规格358像素（宽）×441像素（高）
    - 分辨率350dpi
    - 颜色模式24位RGB真彩色
    - 格式JPG或JPEG
    - 大小20K－100K
    """
    try:
        # 打开图像
        img = Image.open(input_path)
        
        # 转换为RGB模式（如果不是）
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # 调整大小为358×441像素
        img = img.resize((358, 441), Image.LANCZOS)
        
        # 设置DPI为350
        img.info['dpi'] = (350, 350)
        
        if output_path is None:
            # 如果未指定输出路径，在原文件名基础上添加"_processed"
            filename, ext = os.path.splitext(input_path)
            output_path = f"{filename}_processed.jpg"
        
        # 初始质量设置
        quality = 90
        img.save(output_path, format='JPEG', quality=quality, dpi=(350, 350))
        
        # 检查文件大小并调整，直到文件大小在20K-100K之间
        file_size = os.path.getsize(output_path)
        
        # 如果文件过大，逐步降低质量
        while file_size > 100 * 1024 and quality > 10:
            quality -= 5
            img.save(output_path, format='JPEG', quality=quality, dpi=(350, 350))
            file_size = os.path.getsize(output_path)
        
        # 如果文件过小，尝试增加质量
        while file_size < 20 * 1024 and quality < 95:
            quality += 5
            img.save(output_path, format='JPEG', quality=quality, dpi=(350, 350))
            file_size = os.path.getsize(output_path)
        
        # 最终检查
        file_size_kb = file_size / 1024
        if 20 <= file_size_kb <= 100:
            return True, output_path, file_size_kb
        else:
            return False, output_path, file_size_kb
    
    except Exception as e:
        return False, None, str(e)

def create_gui():
    """创建简单的GUI界面"""
    root = tk.Tk()
    root.title("证件照处理工具")
    root.geometry("600x400")
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill='both')
    
    # 介绍标签
    intro_label = tk.Label(
        frame, 
        text="证件照处理工具\n\n将照片调整为358×441像素，350dpi，RGB模式，文件大小20K-100K",
        justify=tk.LEFT
    )
    intro_label.pack(pady=10, anchor='w')
    
    # 输入路径框
    input_frame = tk.Frame(frame)
    input_frame.pack(fill='x', pady=5)
    
    input_label = tk.Label(input_frame, text="输入图像路径:", width=12, anchor='w')
    input_label.pack(side='left')
    
    input_var = tk.StringVar()
    input_entry = tk.Entry(input_frame, textvariable=input_var, width=40)
    input_entry.pack(side='left', fill='x', expand=True, padx=5)
    
    browse_input_btn = tk.Button(input_frame, text="浏览...", command=lambda: input_var.set(filedialog.askopenfilename(
        title="选择证件照",
        filetypes=[("图片文件", "*.jpg *.jpeg *.png *.bmp")]
    )))
    browse_input_btn.pack(side='right')
    
    # 输出路径框
    output_frame = tk.Frame(frame)
    output_frame.pack(fill='x', pady=5)
    
    output_label = tk.Label(output_frame, text="保存图像路径:", width=12, anchor='w')
    output_label.pack(side='left')
    
    output_var = tk.StringVar()
    output_entry = tk.Entry(output_frame, textvariable=output_var, width=40)
    output_entry.pack(side='left', fill='x', expand=True, padx=5)
    
    browse_output_btn = tk.Button(output_frame, text="浏览...", command=lambda: output_var.set(filedialog.asksaveasfilename(
        title="保存证件照",
        defaultextension=".jpg",
        filetypes=[("JPEG图像", "*.jpg")]
    )))
    browse_output_btn.pack(side='right')
    
    # 状态标签
    status_var = tk.StringVar()
    status_var.set("请输入图像路径...")
    status_label = tk.Label(frame, textvariable=status_var)
    status_label.pack(pady=10)
    
    def process_images():
        input_path = input_var.get().strip()
        output_path = output_var.get().strip()
        
        if not input_path:
            messagebox.showerror("错误", "请输入图像路径")
            return
        
        if not os.path.exists(input_path):
            messagebox.showerror("错误", f"找不到图像: {input_path}")
            return
        
        if not output_path:
            # 使用默认输出路径
            filename, ext = os.path.splitext(input_path)
            output_path = f"{filename}_processed.jpg"
            output_var.set(output_path)
        
        status_var.set(f"正在处理：{os.path.basename(input_path)}...")
        root.update()
        
        success, path, info = process_photo(input_path, output_path)
        
        if success:
            status_var.set(f"处理成功！文件大小: {info:.1f}KB")
            messagebox.showinfo("处理成功", f"照片已处理并保存至:\n{path}\n文件大小: {info:.1f}KB")
        else:
            if isinstance(info, str):
                status_var.set(f"处理失败: {info}")
                messagebox.showerror("处理失败", f"错误: {info}")
            else:
                status_var.set(f"处理完成，但文件大小 ({info:.1f}KB) 不在要求范围内")
                messagebox.showwarning("处理警告", f"照片已处理并保存至:\n{path}\n但文件大小 ({info:.1f}KB) 不在20K-100K范围内")
    
    # 处理按钮
    process_button = tk.Button(frame, text="处理图片", command=process_images)
    process_button.pack(pady=10)
    
    # 退出按钮
    exit_button = tk.Button(frame, text="退出", command=root.destroy)
    exit_button.pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 命令行模式
        input_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        
        success, path, info = process_photo(input_path, output_path)
        if success:
            print(f"处理成功！文件已保存至 {path}，大小: {info:.1f}KB")
        else:
            if isinstance(info, str):
                print(f"处理失败: {info}")
            else:
                print(f"处理完成，但文件大小 ({info:.1f}KB) 不在要求范围内")
    else:
        # GUI模式
        create_gui()
