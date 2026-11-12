# 스팸메일 분류기

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts= [ 
    "무료 쿠폰 지금 클릭하면 무료 선물",
    "한번만 클릭해도 무료 대박",
    "오늘 회의는 2시 제 3회의실입니다.",
    "지금 할인 행사 중",
    "회의 자료는 메일로 보내주세요",
    "지금 바로 쿠폰 확인"
]
labels = ["spam", "spam", "ham", "spam", "ham", "spam"]

vect = CountVectorizer()
x = vect.fit_transform(texts)
print(vect.get_feature_names_out())
print(x.toarray())
print(vect.vocabulary_)
print(x)

from sklearn.metrics import accuracy_score
model = MultinomialNB()
model.fit(x, labels)
pred = model.predict(x)
print('정확도 : ', accuracy_score(labels, pred))

print()
text_test = ['무료 쿠폰 지금 발급', '간부 회의는 언제 시작하나요?']
x_test = vect.transform(text_test)
print(x_test)

preds = model.predict(x_test)
probs = model.predict_proba(x_test)
class_names = model.classes_

for text, pred, prob in zip(text_test, preds, probs):
    prob_str = ", ".join([f'{cls}:{p:.4f}' for cls, p in zip(class_names, prob)])
    print(f"'{text}' --> 예측:{pred} // 확률:[{prob_str}]")