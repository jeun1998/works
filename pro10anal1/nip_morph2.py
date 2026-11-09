# 웹 문서를 읽어 형태소 분석 : 위키 백과에서 단어 검색 결과
# 단어 출현 횟수를 DataFrame에 저장

import requests
from bs4 import BeautifulSoup
import pandas as pd
from konlpy.tag import Okt
from urllib import parse

okt = Okt()

url = "https://ko.wikipedia.org/wiki/%EA%B0%80%EC%98%A4%EC%8A%9D%EC%8B%9C"
para = parse.quote("가오슝")
url = "https://ko.wikipedia.org/wiki/" + para

headers = {"User-Agent":"Mozilla/5.0"}
response = requests.get(url=url, headers=headers)

if response.status_code == 200:
    page = response.text
    soup = BeautifulSoup(page, 'html.parser')

    wordlist = []

    for item in soup.select("#mw-content-text p"):
        # print(item.string)
        if item.string != None:
            wordlist += okt.nouns(item.string)

    print('wordlist : ', wordlist)
    print('단어 수 : ', len(wordlist))
    print()
    word_dict = {} # 단어의 발생횟수를 dict로 저장
    for i in wordlist:
        if i in word_dict:
            word_dict[i] += 1
        else: 
            word_dict[i] = 1
    print('word_dict : ', word_dict)

    print('Series로 출력 ---')
    seri_list = pd.Series(wordlist)
    print(seri_list[:3])
    print(seri_list.value_counts()[:5])
    print()
    seri_dict = pd.Series(word_dict)
    print(seri_dict[:3])
    print(seri_dict.value_counts()[:5])

    print('\nDataFrame으로 출력 -------')
    df1 = pd.DataFrame(wordlist, columns=['단어'])
    print(df1.head(3))
    df2 = pd.DataFrame([word_dict.keys(), word_dict.values()])
    df2 = df2.T
    df2.columns = ['단어', '빈도수']
    print(df2.head())

    result = df2[df2['빈도수'] >= 5]
    print('5회 이상 등장 단어 : ', result)
    print('전체 단어 빈도수 : ', df2['빈도수'].sum())
    print('평균 출현 빈도수 : ', df2['빈도수'].mean())