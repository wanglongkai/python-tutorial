import os
import re
import time
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from hashlib import md5

class ImageDownloader:
    def __init__(self, save_dir="./downloaded_images", headers=None, retry_times=3, delay=0.5):
        """
        初始化图片下载器
        :param save_dir: 图片保存目录，默认当前目录下的downloaded_images
        :param headers: 请求头，默认自带浏览器UA避免反爬
        :param retry_times: 下载失败重试次数，默认3次
        :param delay: 下载间隔秒数，避免请求过快被封IP
        """
        self.save_dir = save_dir
        self.retry_times = retry_times
        self.delay = delay
        self.downloaded = set() # 已下载图片哈希，避免重复下载
        
        # 默认请求头，模拟浏览器访问
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Referer": ""
        }
        
        # 创建保存目录
        os.makedirs(save_dir, exist_ok=True)

    def _get_file_ext(self, url):
        """提取图片扩展名"""
        ext = os.path.splitext(urlparse(url).path)[1].lower()
        # 常见图片扩展名，没有的话默认用jpg
        return ext if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'] else '.jpg'

    def _download_single_image(self, img_url):
        """下载单张图片"""
        # 跳过base64编码的内嵌图片
        if img_url.startswith('data:image'):
            return None
        
        # 生成图片唯一哈希，避免重复下载
        img_hash = md5(img_url.encode('utf-8')).hexdigest()
        if img_hash in self.downloaded:
            print(f"[跳过] 已下载: {img_url}")
            return None
        self.downloaded.add(img_hash)

        ext = self._get_file_ext(img_url)
        save_path = os.path.join(self.save_dir, f"{img_hash}{ext}")

        for attempt in range(self.retry_times):
            try:
                response = requests.get(
                    img_url, 
                    headers=self.headers, 
                    timeout=10,
                    stream=True
                )
                response.raise_for_status()

                # 校验是否为图片文件
                if 'image' not in response.headers.get('content-type', ''):
                    print(f"[跳过] 非图片资源: {img_url}")
                    return None

                # 保存图片
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=1024):
                        f.write(chunk)
                
                print(f"[成功] 已保存: {save_path}")
                time.sleep(self.delay)
                return save_path

            except Exception as e:
                print(f"[重试 {attempt+1}/{self.retry_times}] 下载失败 {img_url}: {str(e)}")
                time.sleep(1)
        
        print(f"[失败] 多次重试仍无法下载: {img_url}")
        return None

    def get_page_images(self, page_url):
        """获取目标页面所有图片链接"""
        try:
            self.headers['Referer'] = page_url
            response = requests.get(page_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')

            img_urls = set()
            for img in soup.find_all('img'):
                # 优先取data-src（懒加载图片），没有的话取src
                src = img.get('data-src') or img.get('src') or img.get('data-original')
                if not src:
                    continue
                # 相对路径转绝对路径
                absolute_url = urljoin(page_url, src)
                img_urls.add(absolute_url)
            
            print(f"[发现] 页面共找到 {len(img_urls)} 张图片")
            return list(img_urls)

        except Exception as e:
            print(f"[错误] 无法获取页面内容: {str(e)}")
            return []

    def download_page_images(self, page_url):
        """下载页面所有图片"""
        img_urls = self.get_page_images(page_url)
        if not img_urls:
            return
        
        success = 0
        for url in img_urls:
            if self._download_single_image(url):
                success +=1
        
        print(f"\n[完成] 共下载成功 {success}/{len(img_urls)} 张图片，保存路径：{os.path.abspath(self.save_dir)}")

if __name__ == "__main__":
    # 配置参数
    TARGET_URL = "https://616pic.com/tupian/meinvxingganmeinv_3.html" # 替换为你要爬取的网站地址
    SAVE_DIR = "./my_images" # 替换为你的保存路径
    
    # 如果你需要爬取需要登录的网站，可以在这里加Cookie
    custom_headers = {
        # "Cookie": "你的登录Cookie"
    }
    
    downloader = ImageDownloader(save_dir=SAVE_DIR, headers=custom_headers)
    downloader.download_page_images(TARGET_URL)