import requests
from bs4 import BeautifulSoup
import re
import time
import random
import argparse
import sys
import os
import ssl
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib3.exceptions import InsecureRequestWarning

# 禁用不安全请求的警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_paper_info(url, verify_ssl=True, max_retries=3):
    """
    从Google学术链接中提取论文信息
    
    参数:
        url (str): Google学术论文链接
        verify_ssl (bool): 是否验证SSL证书
        max_retries (int): 最大重试次数
        
    返回:
        dict: 包含论文题目、作者列表、期刊名称等信息的字典
    """
    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }
    
    # 设置重试策略
    session = requests.Session()
    retry_strategy = Retry(
        total=max_retries,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    try:
        # 发送HTTP请求
        response = session.get(url, headers=headers, timeout=10, verify=verify_ssl)
        response.raise_for_status()  # 检查请求是否成功
        
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取论文信息
        paper_info = {}
        
        # 提取标题
        title_tag = soup.find('h1', class_='title')
        if title_tag:
            paper_info['title'] = title_tag.get_text().strip()
        else:
            # 尝试其他可能的标题标签
            title_tag = soup.find('div', class_='gs_ri')
            if title_tag and title_tag.h3:
                paper_info['title'] = title_tag.h3.get_text().strip()
        
        # 提取作者列表
        authors_tag = soup.find('div', class_='gs_a')
        if authors_tag:
            authors_text = authors_tag.get_text().strip()
            # 通常作者在第一个 '-' 之前
            if '-' in authors_text:
                authors = authors_text.split('-')[0].strip()
                paper_info['authors'] = [author.strip() for author in authors.split(',')]
        
        # 提取期刊/会议名称
        venue_tag = soup.find('div', class_='gs_a')
        if venue_tag:
            venue_text = venue_tag.get_text().strip()
            # 期刊/会议名称通常在第一个和第二个 '-' 之间
            if venue_text.count('-') >= 2:
                venue = venue_text.split('-')[1].strip()
                paper_info['venue'] = venue
        
        # 提取发表年份
        venue_text = venue_tag.get_text().strip() if venue_tag else ""
        year_match = re.search(r'\b(19|20)\d{2}\b', venue_text)
        if year_match:
            paper_info['year'] = year_match.group(0)
        
        # 提取引用次数
        citations_tag = soup.find('div', class_='gs_fl')
        if citations_tag and citations_tag.find('a'):
            citations_text = citations_tag.find('a').get_text()
            citations_match = re.search(r'被引用次数：(\d+)', citations_text)
            if citations_match:
                paper_info['citations'] = int(citations_match.group(1))
        
        return paper_info
    
    except requests.exceptions.SSLError as e:
        print(f"SSL错误: {e}")
        # 如果启用了SSL验证但失败，尝试禁用SSL验证重试
        if verify_ssl:
            print("尝试禁用SSL验证重试...")
            return get_paper_info(url, verify_ssl=False, max_retries=max_retries)
        return None
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
        return None
    except Exception as e:
        print(f"处理错误: {e}")
        return None

def generate_markdown(paper_info):
    """
    将论文信息生成markdown格式
    
    参数:
        paper_info (dict): 包含论文信息的字典
        
    返回:
        str: markdown格式的论文信息
    """
    if not paper_info:
        return "无法获取论文信息"
    
    markdown = []
    
    # 添加标题
    if 'title' in paper_info:
        markdown.append(f"# {paper_info['title']}")
        markdown.append("")
    
    # 添加作者
    if 'authors' in paper_info:
        markdown.append(f"**作者**: {', '.join(paper_info['authors'])}")

    
    # 添加发表信息
    pub_info = []
    if 'venue' in paper_info:
        pub_info.append(f"**期刊/会议**: {paper_info['venue']}")
    if 'year' in paper_info:
        pub_info.append(f"**年份**: {paper_info['year']}")
    if pub_info:        
        markdown.append("\n".join(pub_info))
        markdown.append("")
    
    # 添加引用信息
    if 'citations' in paper_info:
        markdown.append("**引用次数**")
        markdown.append(f"{paper_info['citations']}")
        markdown.append("")
    
    return "\n".join(markdown)

def save_markdown_to_file(markdown_content, filename):
    """
    将markdown内容保存到文件
    
    参数:
        markdown_content (str): markdown格式的内容
        filename (str): 文件名
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    print(f"已保存到文件: {filename}")

def main():
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='从Google学术链接中提取论文信息')
    parser.add_argument('--urls', nargs='+', help='Google学术论文链接列表')
    parser.add_argument('--file', help='包含Google学术论文链接的文件，每行一个链接')
    parser.add_argument('--output', help='输出的Markdown文件名（默认使用论文标题）')
    parser.add_argument('--quiet', action='store_true', help='安静模式，不打印详细信息到控制台')
    args = parser.parse_args()
    
    urls = []
    
    # 从命令行参数获取URLs
    if args.urls:
        urls.extend(args.urls)
    
    # 从文件读取URLs
    if args.file:
        try:
            with open(args.file, 'r') as f:
                file_urls = [line.strip() for line in f if line.strip()]
                urls.extend(file_urls)
        except Exception as e:
            print(f"读取文件出错: {e}")
            sys.exit(1)
    
    # 如果没有提供URLs，显示帮助信息
    if not urls:
        # 默认使用一个示例URL
        if not args.quiet:
            print("未提供URLs，使用默认示例链接...")
        urls = [
            "https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Joint+Modeling+of+Image+and+Label+Statistics+for+Enhancing+Model+Generalizability+of+Medical+Image+Segmentation&btnG="
        ]
    
    for url in urls:
        paper_info = get_paper_info(url)
        if paper_info:
            # 生成markdown格式
            markdown_content = generate_markdown(paper_info)
            
            if not args.quiet:
                print("\nMarkdown格式:")
                print("-" * 40)
                print(markdown_content)
            
            # 确定输出文件名
            # if args.output:
            #     filename = args.output
            # elif 'title' in paper_info:
            #     # 使用论文标题的前20个字符作为文件名
            #     safe_title = "".join(c for c in paper_info['title'][:20] if c.isalnum() or c.isspace()).strip()
            #     safe_title = safe_title.replace(" ", "_")
            #     filename = f"{safe_title}.md"
            # else:
            #     filename = "paper_info.md"
            
            # # 如果处理多个URL并使用自定义输出名称，添加序号
            # if args.output and len(urls) > 1:
            #     name, ext = os.path.splitext(filename)
            #     filename = f"{name}_{urls.index(url) + 1}{ext}"
            
            # save_markdown_to_file(markdown_content, filename)
            # if not args.quiet:
            #     print(f"已保存到文件: {filename}")
        else:
            if not args.quiet:
                print("无法获取论文信息，请检查链接是否正确。")
        
        # 多个链接之间添加随机延迟
        if urls.index(url) < len(urls) - 1:
            time.sleep(random.uniform(2, 5))

if __name__ == "__main__":
    main()
