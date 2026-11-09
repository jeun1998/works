# BeautifulSoup 객체를 이용한 문서 처리
import requests
from bs4 import BeautifulSoup

baseur1 = "https://www.naver.com"
headers = {"User-Agent":"Mozila/5.0"}
source = requests.get(baseur1, headers=headers)
print(source, type(source))  
print(source.status_code)
# print(source.text, type(source.text))
# print(source.content)

conv_data = BeautifulSoup(source.text, 'lxml')
# print(conv_data, type(conv_data))
for atag in conv_data.find_all("a"):
    href = atag.get("href")
    title = atag.get_text(strip=True)
    if title:
        print(href)
        print(title)
        print('---')