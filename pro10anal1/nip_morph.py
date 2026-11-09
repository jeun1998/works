# 형태소 분석
# 말뭉치 (코퍼스)는 자연어 연구, 언어분석, 인공지능 분야에 ................................................................................
# 형태소는 의미를 가지는 가장 작은 단위를 말함

# 영어 토큰화

import nltk
from nltk.tokenize import word_tokenize
# 최초 실행 시 필요한 데이터 다운로드
nltk.download("punkt")
nltk.download("punkt_tab")

text = "I am studying Python with my friends at room."
# 1. 토큰화
tokens = word_tokenize(text)
print(tokens)
print()

pos_tags = nltk.pos_tag(tokens)
print(pos_tags)

print('\n\n----------------------')
from konlpy.tag import Okt, Kkma, Komoran
text = "하이닉스 꼭 가고 싶다 ㄹㅇ"
print('Okt ----------------------')
okt = Okt()
print('형태소 : ', okt.morphs(text))
print('품사 태깅 : ', okt.pos(text))
print('품사 태깅 (어간 포함) : ', okt.pos(text, stem=True))
print('명사 추출 : ', okt.nouns(text))