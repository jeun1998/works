import pandas as pd
import scipy.stats as stats

data = pd.read_csv("https://raw.githubusercontent.com/pykwon/python/refs/heads/master/testdata_utf8/drinkdata.csv")
print(data)
print(stats.chisquare(data['관측도수']))

exp = [data['관측도수'].sum() / 5] * 5
print("기대 도수(exp) : ", exp)
stat, pv = stats.chisquare(f_obs=data["관측도수"], f_exp=exp)
print(f"검정 통계량(chi2) : {stat:.7f}")
print(f"유의 확률(p) : {pv:.7f}")