# [로지스틱 분류분석 문제1]

# 문1] 소득 수준에 따른 외식 성향을 나타내고 있다. 주말 저녁에 외식을 하면 1, 외식을 하지 않으면 0으로 처리되었다. 

# 다음 데이터에 대하여 소득 수준이 외식에 영향을 미치는지 로지스틱 회귀분석을 실시하라.

# 키보드로 소득 수준(양의 정수)을 입력하면 외식 여부 분류 결과 출력하라.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import koreanize_matplotlib
import statsmodels.formula.api as smf
from sklearn.metrics import accuracy_score
data = {
    '요일': [
        '토','토','토','화','토','월','토','토','토','토',
        '토','토','토','토','일','월','화','수','목','금',
        '토','토','토','토','일','토','일','토'
    ],
    '외식유무': [
        0,0,0,1,0,1,1,1,0,0,
        1,1,0,1,1,1,0,0,1,1,
        1,1,0,0,1,1,0,0
    ],
    '소득수준': [
        57,39,28,60,31,42,54,65,45,37,
        98,60,41,52,75,45,46,39,70,44,
        74,65,46,39,60,44,30,34
    ]
}

df = pd.DataFrame(data)

print(df.head(3))
print(df.info())
print(df.shape)
print(df['외식유무'].unique())


formula = '외식유무 ~ 소득수준'

result = smf.logit(formula=formula, data=df).fit()

print('\n로지스틱 회귀분석 결과')
print(result.summary())

# 소득수준의 유의성 확인
pv = result.pvalues['소득수준']
print('소득수준 p-value : ', pv)

if pv < 0.05:
    print('소득수준은 외식 여부와 유의한 관련이 있다.')
else:
    print('소득수준과 외식 여부의 유의한 관련성을 확인하지 못했다.')

# 3. 회귀계수와 절편
w = result.params['소득수준']
b = result.params['Intercept']

print('\n가중치(w) : ', w)
print('편향(b) : ', b)

# 4. Sigmoid 함수 정의
def OurSigmoidFunc(z):
    return 1 / (1 + np.exp(-z))

# 소득수준으로 logit 계산
x = df['소득수준'].values
z = w * x + b

# Sigmoid 함수 적용
p = OurSigmoidFunc(z)

print('\nSigmoid 적용 결과')
print('x[:3] : ', x[:3])
print('z[:3](logit) : ', np.round(z[:3], 3))
print('p[:3](확률) : ', np.round(p[:3], 3))

# 5. statsmodels 예측값과 비교
pred = result.predict(df[:10])

print('\n모델 예측 확률 : ', pred.values)
print('모델 예측 결과 : ', np.rint(pred.values))
print('실제값 : ', df['외식유무'][:10].values)

print('\nSigmoid 직접 계산 확률 : ', p[:10])

# 6. 혼동 행렬
print('\n혼동 행렬')
conf_tab = result.pred_table()
print(conf_tab)

print('혼동 행렬을 이용한 분류 정확도 : ',
    (conf_tab[0][0] + conf_tab[1][1]) / len(df))

# accuracy_score 이용
pred2 = result.predict(df)

print('accuracy_score 분류 정확도 : ',
    accuracy_score(df['외식유무'], np.rint(pred2.values)))

# 7. Sigmoid 함수 시각화
print('\nSigmoid 함수 시각화')

x_fit = np.linspace(
    df['소득수준'].min(),
    df['소득수준'].max(),
    100
)

z_fit = w * x_fit + b
p_fit = OurSigmoidFunc(z_fit)

plt.figure(figsize=(8, 5))

# 실제 외식 여부
plt.scatter(
    df['소득수준'],
    df['외식유무'],
    color='black',
    label='실제 외식 여부'
)

# Sigmoid 곡선
plt.plot(
    x_fit,
    p_fit,
    color='blue',
    label='Sigmoid(외식 확률)'
)

# 분류 기준선
plt.axhline(
    0.5,
    color='red',
    linestyle='--',
    label='분류 기준 0.5'
)

plt.title('소득수준에 따른 외식 확률')
plt.xlabel('소득수준')
plt.ylabel('외식 확률')
plt.grid(True)
plt.legend()
plt.show()

# 8. 키보드로 소득수준 입력 후 예측
print('\n새로운 값으로 예측하기 ----')

income = int(input('소득수준 입력(양의 정수) : '))

if income > 0:

    # Sigmoid 직접 계산
    new_z = w * income + b
    new_p = OurSigmoidFunc(new_z)

    print('\n입력한 소득수준 : ', income)
    print('logit 값 : ', new_z)
    print('Sigmoid 외식 확률 : ', new_p)

    # statsmodels 모델로 예측
    newdf = pd.DataFrame()
    newdf['소득수준'] = [income]

    new_pred = result.predict(newdf)

    print('모델 예측 확률 : ', new_pred.values)
    print('모델 예측 결과 : ', np.rint(new_pred.values))

    if new_p >= 0.5:
        print('외식할 것으로 예측됩니다. (1)')
    else:
        print('외식하지 않을 것으로 예측됩니다. (0)')

else:
    print('양의 정수를 입력하세요.')
