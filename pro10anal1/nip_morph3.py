# 웹(donga.com)에서 특정 단어 관련 문서를 검색 후 명사만 추출


from bs4 import BeautifulSoup
from urllib.parse import quote
import urllib.request
from konlpy.tag import Okt
from collections import Counter
import pytagcloud
import matplotlib.pyplot as plt
import koreanize_matplotlib
import matplotlib.image as mpimg
import webbrowser
import pandas as pd
import numpy as np
import pygame

# searchWord = input("검색어:")
# print(searchWord)

searchWord = "대만"
target_url = "https://www.donga.com/news/search?query=" + quote(searchWord)
source_code = urllib.request.urlopen(target_url)
soup = BeautifulSoup(source_code, 'lxml',from_encoding='utf-8')
print(soup)

msg = ""

for title in soup.find_all("h4", class_="tit"):
    title_link = title.find("a")
    # print(title_link)
    article_url = title_link["href"]

    try:
        source_article = urllib.request.urlopen(article_url)
        soup2 = BeautifulSoup(source_article, 'lxml', from_encoding='utf-8')
        contents = soup2.select("div.article_txt")
        for imsi in contents:
            item = str(imsi.find_all(string=True))
            msg += item
    except Exception as e:
        pass

    okt = Okt()
    nouns = okt.nouns(msg)

    result = []
    for n in nouns:
        if len(n) > 1:
            result.append(n)

print(result[:20])

count = Counter(result)
tag = count.most_common(50)
# print(tag)

taglist = pytagcloud.make_tags(tag, maxsize=100)
print(len(taglist))
pytagcloud.create_tag_image(taglist, "nip_word.png",
                        size=(1000, 600), background=(0,0,0), fontname="H2HDRM", rectangular=False)

img = mpimg.imread("nip_word.png")
plt.imshow(img)
plt.show()

print('--------------------------')
df = pd.DataFrame(count.items(), columns=["단어","빈도수"])
print(df.head())

if not df.empty:
    print("\n빈도수 기준 내림차순 정렬 ---")
    df = df.sort_values(by="빈도수", ascending=False)
    df = df.reset_index(drop=True)
    print(df.head())
    print("\nPandas 기초 통계: \n", df["빈도수"].describe())
    print("\nNumpy 기초 통계 :")
    freq = df["빈도수"].to_numpy()
    print("전체 단어 출현 횟수 : ", np.sum(freq))
    print("평균 빈도수 : ", np.mean(freq))
    print("표준 편차 : ", np.std(freq))
    print("\n상위 단어 10개로 막대 그래프")
    top10 = df.head(10).sort_values(by="빈도수")
    plt.figure(figsize=(10, 6))
    plt.barh(top10["단어"], top10["빈도수"])
    plt.xlabel("단어")
    plt.ylabel("빈도수")
    plt.show()

    df.to_csv("nlp_freq.csv", index=False, encoding='utf-8')

else:
    print("분석할 단어가 없어요.")
