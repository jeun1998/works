# 편차가 큰 데이터에 대한 로그 변환
# 큰 값을 압축해서 데이터 간 격차를 줄이는 변환이 가능

import numpy as np
np.set_printoptions(suppress=True, precision=6)

def test():
    values = np.array([345, 34.5, 3.45, 0.345, 0.01, 0.1, 10, 100])
    print(np.log2(3.45), ' ', np.log10(3.45), ' ', np.log(3.45))
    print('원본 값 : ', values)
    log_values = np.log10(values)
    print('log_values : ', log_values)
    ln_values = np.log(values)
    print('ln_values : ', ln_values)

    min_val = np.min(values)
    max_val = np.max(values)
    normalized = (values - min_val) / (max_val - min_val)
    print('정규화 결과 : ', normalized)

    mymean = np.mean(values)
    mystd = np.std(values)
    standardized = (values - mymean) / mystd
    print('표준화 결과 : ', standardized)

class LogTrans:
    def __init__(self, offset:float=1.0):
        self.offset = offset

    def transform(self, x:np.ndarray) -> np.ndarray:
        return np.log(x + self.offset)

    def inverse_transform(self, x_log:np.ndarray) -> np.ndarray:
        return np.exp(x_log) - self.offset

test()
print('---------------------------------')
data = np.array([0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000], dtype=float)
logObj = LogTrans()
data_log_scaled = logObj.transform(data)
reversed_data = logObj.inverse_transform(data_log_scaled)

print('원본 자료 : ', data)
print('로그 변환 : ', data_log_scaled)
print('역 변환 : ', reversed_data)