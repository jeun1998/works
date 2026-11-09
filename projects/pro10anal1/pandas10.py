# css 셀렉터를 이용
from bs4 import BeautifulSoup

html_page4 = """
<html><body>
<div id="hello">
    <a href="https://www.naver.com">naver</a><br/>
    <span>
        <a href="https://www.daum.net">daum</a>
    </span>
</div>
</body></html>
"""
soup = BeautifulSoup(html_page4, 'html.parser')
# aa = soup.select_one("div")
aa = soup.select_one("div#hello > a")
print("aa : ", aa, " ", aa.string)

print()
bb = soup.select("div")
print("bb : \n", bb)
for i in bb:
    print(i, " ", i.text)

print("위키백과 사이트에서 대만으로 검색된 자료 읽기 ---")
import requests
url = "https://ko.wikipedia.org/wiki/대만"
headers = {"User-Agent":"Mozila/5.0"}
wiki = requests.get(url=url, headers=headers)
# print(wiki.text[:1000])
soup = BeautifulSoup(wiki.text, 'html.parser')
result = soup.select("p#mwIA")
# print(result)
for s in result:
    for sup in s.find_all("sup"):
        sup.decompose()  # sup 태그 제거

    print(s.get_text(strip=True, separator=" "))  # 문자열만 출력

print("\n\n교촌 치킨 사이트에서 메뉴, 가격 자료 읽기 ---")
import pandas as pd
url = "https://www.kyochon.com/menu/chicken.asp"
headers = {"User-Agent":"Mozila/5.0"}
kyochon = requests.get(url=url, headers=headers)
# print(kyochon.text)
soup2 = BeautifulSoup(kyochon.text, 'html.parser')

names = soup2.select("dl.txt > dt")
prices = [int(tag.text.strip().replace(",",""))
            for tag in soup2.select("p.money strong")]

df = pd.DataFrame({"상품명":names, "가격":prices})
print(df.head(3))
print(f"가격 평균 : {df["가격"].mean():.2f}")
print(f"가격 표준편차 : {df["가격"].std():.2f}")
cv = df["가격"].std() / df["가격"].mean() * 100
print(f"가격 변동계수 : {cv:.2f}%")