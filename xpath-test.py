from lxml import etree
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
}
response = requests.get("https://www.bilibili.com/", headers=headers)

tree = etree.HTML(response.text)

print(
    tree.xpath(
        "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/div/div/div/a/@href"
    )
)
