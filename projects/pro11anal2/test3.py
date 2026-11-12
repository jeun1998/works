import pandas as pd
import scipy.stats as stats

data = [4, 6, 17, 16, 8, 9]
print(stats.chisquare(data))

alpha = 0.05
results = stats.chisquare(data)
print(f"카이제곱 검정 통계량 : {results.statistic:.4f}")
print(f"유의확률(p-value) : {results.pvalue:.4f}")
if p < alpha :
    print("판정 : 귀무가설 기각(통계적으로 유의함)")
else:
    print("판정 : 귀무가설 채택(통계적으로 유의하지 않음)")