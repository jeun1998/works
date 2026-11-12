# pro12ml — Python 머신러닝·통계·예측 모델 학습 노트

> **학습 주제:** 상관관계 → 선형·다항 회귀 → 로지스틱 회귀 → 분류기 평가 → 결정트리/앙상블 → SVM·차원 축소 → 나이브 베이즈/KNN → 퍼셉트론·MLP → Flask 예측 서비스  
> **대상 소스:** 업로드된 `pro12ml.zip`의 실제 파일을 읽고 작성함 · `ex1.py`~`ex46.py`, **`ex.47.py`**(실제 파일명의 점 포함), `prac1.py`, `prac2.py`, `prac4.py`~`prac11.py`, `quiz1/app.py` 및 HTML  
> **작성 원칙:** 기존 원본 코드는 변경하지 않음. *실제 코드가 구현한 내용*과 *개념적으로 바람직한 개선점*을 구분해 설명함. 외부 API/DB를 이용하는 스크립트의 최종 실행 성능은 여기서 검증하지 않았음.

## 목차

1. [프로젝트 개요와 학습 지도](#1-프로젝트-개요와-학습-지도)
2. [환경 준비 및 실행](#2-환경-준비-및-실행)
3. [핵심 이론 요약](#3-핵심-이론-요약)
4. [예제 코드 해설 — ex1 ~ ex.47](#4-예제-코드-해설--ex1--ex47)
5. [실전 연습문제 해설 — prac 시리즈](#5-실전-연습문제-해설--prac-시리즈)
6. [Flask 미니 프로젝트 — quiz1](#6-flask-미니-프로젝트--quiz1)
7. [데이터 파일과 실행 의존성](#7-데이터-파일과-실행-의존성)
8. [실제 코드 점검·개선 포인트](#8-실제-코드-점검개선-포인트)
9. [복습 순서 및 포트폴리오 활용](#9-복습-순서-및-포트폴리오-활용)

---

## 1. 프로젝트 개요와 학습 지도

이 폴더는 Python의 통계 분석을 머신러닝으로 확장하는 학습 기록이다. 단순히 `fit()`을 호출하는 데서 끝나지 않고, **데이터 탐색 → 변수 관계 분석 → 전처리 → 학습/검증 분리 → 모델 생성 → 성능지표 해석 → 새 데이터 예측 → 웹 서비스 연결**까지 다양한 예제로 실습했다.

| 학습 단계 | 핵심 내용 | 연결되는 파일 |
|---|---|---|
| 상관·기초 통계 | 분산, 공분산, 피어슨 상관계수, 산점도, 상관 히트맵 | `ex1`~`ex3`, `prac1` |
| 선형회귀 | 최소제곱법, 기울기·절편, OLS, 다중회귀, 잔차 진단 | `ex4`~`ex14`, `prac2`, `prac4` |
| 비선형 회귀 | 다항 특성, 과적합, 규제의 의미 | `ex15`, `ex16`, `prac5` |
| 로지스틱 분류 | 시그모이드, 로그오즈, 이진·다중 분류, ROC/AUC | `ex17`~`ex21`, `prac6`~`prac8` |
| 트리·검증 | 지니 불순도, 엔트로피, 훈련/테스트, K-Fold, GridSearchCV | `ex22`~`ex25` |
| 앙상블 | 소프트 보팅, 랜덤포레스트, XGBoost, LightGBM | `ex26`~`ex32`, `prac9`, `prac10` |
| 마진·차원 축소 | SVM, 커널, PCA, 얼굴 이미지 분류 | `ex33`~`ex37` |
| 확률·거리 기반 분류 | 가우시안/다항 나이브 베이즈, KNN | `ex38`~`ex42`, `prac11` |
| 인공신경망 | 퍼셉트론, XOR, MLP, 다중클래스 분류 | `ex43`~`ex46`, `ex.47` |
| 웹 연동 | SQL → Pandas → 회귀모델 → Flask API → fetch 결과 표시 | `quiz1/app.py`, `quiz1/templates/index.html` |

**이 저장소의 성격:** 개별 알고리즘을 비교·연습한 교육용 예제 모음이다. 일부 코드는 실험 중 작성한 상태이므로, 실행 전에 [8장](#8-실제-코드-점검개선-포인트)의 주의사항을 반드시 확인한다.

---

## 2. 환경 준비 및 실행

### 2.1 실행 환경

- Python 3.10 이상 권장. 기존 코드에 사용된 특정 패키지/API의 호환성은 설치 버전에 따라 차이가 날 수 있다.
- VS Code 터미널 또는 Anaconda Prompt에서 `pro12ml` 폴더를 작업 디렉터리로 설정한다.
- 그래프 표시 코드는 로컬 GUI 환경에서 실행하는 것이 편하다.
- 일부 파일은 공개 GitHub 원격 CSV·`statsmodels` R 데이터·scikit-learn 다운로드 데이터에 접속하므로 인터넷 연결이 필요하다.
- `quiz1`은 별도 MariaDB/MySQL 서버와 `test.jikwon` 테이블이 있어야 실행된다.

```bash
# 압축 해제 후 폴더 이동
cd pro12ml

# 가상환경 생성 및 활성화 (Windows PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# 공통 및 선택적 실습 패키지 설치
python -m pip install -U pip
python -m pip install numpy pandas scipy matplotlib seaborn scikit-learn statsmodels koreanize-matplotlib joblib flask pymysql pillow xgboost lightgbm

# 개별 예제 실행
python ex1.py
python ex20.py
python prac9.py
python "ex.47.py"

# Flask 앱은 프로젝트 루트에서
python quiz1/app.py
```

**참고:** 위 설치 명령은 여러 예제를 실행하기 위한 통합 예시이며, 실제 실행에 필요 없는 라이브러리까지 포함한다. Windows에서 `lightgbm` 등의 설치가 실패하면 해당 예제만 별도 환경으로 분리할 수 있다. GitHub의 `vscode.dev`는 코드 열람·편집에는 적합하지만 Python 파일을 직접 실행하는 일반적인 로컬 터미널 역할은 하지 않는다.

### 2.2 데이터·파일 경로 규칙

아래 파일은 **현재 작업 디렉터리가 `pro12ml`**일 때 상대경로로 읽힌다.

```text
pro12ml/
├── ex1.py ~ ex46.py
├── ex.47.py                # 파일명이 ex47.py가 아니라 ex.47.py
├── prac1.py, prac2.py, prac4.py ~ prac11.py
├── train.csv               # ex32.py (용량이 큼)
├── winequality-red.csv     # prac9.py
├── mushrooms.csv           # prac11.py
├── bush.jpeg               # ex37.py
├── *방문객.json, *관광지입장정보*.json  # ex3.py
├── ex20model.sav           # 일부 예제의 학습모델 산출물
├── carseat.pickle          # ex11.py 학습모델 산출물
├── quiz1/
│   ├── app.py
│   └── templates/index.html
└── READMEpro12.md          # 이 설명 파일
```

- Windows에서 다른 디렉터리로 실행하면 `'train.csv'` 등을 찾지 못할 수 있다. `cd pro12ml` 이후 실행하거나 `pathlib.Path(__file__).resolve().parent`를 사용한다.
- `.sav`, `.pickle`은 프로그램에서 생성한 직렬화 모델 파일이다. **신뢰할 수 없는 출처의 pickle/joblib 파일을 열면 임의 코드가 실행될 위험**이 있으므로 외부에서 받은 파일은 불러오지 않는다.

---

## 3. 핵심 이론 요약

### 3.1 지도학습과 데이터 처리 흐름

| 개념 | 설명 | 예제에서의 역할 |
|---|---|---|
| **Feature (`X`, 독립변수)** | 예측의 근거로 넣는 입력 변수 | 아이리스 꽃잎 길이/너비, 자동차 마력, 광고비 |
| **Label/Target (`y`, 종속변수)** | 예측 대상 | 꽃 품종, 연비, 광고 클릭 여부 |
| **회귀(Regression)** | 연속형 수치 예측 | 연비·주택가격·연봉·맥주 소비량 |
| **분류(Classification)** | 이산형 범주 예측 | 생존 여부·품종·독버섯 구분 |
| **학습(Training)** | 입력과 정답의 관계를 모델이 학습 | `model.fit(X_train, y_train)` |
| **추론(Prediction)** | 학습 완료 모델로 새 값 예측 | `model.predict(X_test)` |
| **검증(Validation)** | 학습 과정의 설정 및 성능을 점검 | K-Fold, GridSearchCV |
| **테스트(Test)** | 최종 일반화 성능을 확인 | 학습에 쓰지 않은 별도 데이터 |

기본 코드 흐름:

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print(classification_report(y_test, pred))
```

- `test_size=0.2`: 전체의 20%를 테스트로 배정.
- `random_state=42`: 무작위 분할을 재현 가능하게 설정.
- `stratify=y`: 분류 문제에서 클래스 비율을 유지하는 데 유용.
- **데이터 누수 방지:** 스케일러·인코더·결측값 대체기는 훈련 데이터로만 `fit`하고 테스트에는 `transform`만 적용한다.

### 3.2 분산·공분산·피어슨 상관계수 (`ex1`~`ex3`)

분산은 **하나의 변수**가 평균 주위에 얼마나 퍼져 있는지, 공분산은 **두 변수**가 함께 증가·감소하는 경향을 나타낸다.

- 표본분산: `s² = Σ(xᵢ − x̄)² / (n − 1)`
- 표본공분산: `Cov(X,Y) = Σ(xᵢ − x̄)(yᵢ − ȳ) / (n − 1)`
- 피어슨 상관계수: `r = Cov(X,Y) / (sₓ × sᵧ)`, 범위는 `[-1, 1]`.

**해석:** `r > 0`이면 양의 선형 관계, `r < 0`이면 음의 선형 관계, `r ≈ 0`이면 *선형* 관계가 약할 수 있다. **상관관계가 인과관계를 의미하지는 않는다.** U자형처럼 비선형 관계가 강해도 피어슨 r은 0 근처일 수 있다.

```python
corr = df.corr(numeric_only=True)
print(corr['sales'].sort_values(ascending=False))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
```

`DataFrame.corr()`는 수치형 열의 상관행렬을 만들고, 히트맵은 변수가 많을 때 관계를 빠르게 파악하게 한다.

### 3.3 최소제곱법과 선형회귀 (`ex4`~`ex14`)

단순선형회귀는 `ŷ = β₀ + β₁x`, 다중회귀는 `ŷ = β₀ + β₁x₁ + ... + βₚxₚ` 형태다.

- **절편 β₀:** 모든 입력변수가 0일 때의 모형상 예측값.
- **기울기 β₁:** *다른 변수를 고정*했을 때 입력변수 한 단위 증가에 대응하는 예측값 변화.
- **잔차 eᵢ:** `yᵢ − ŷᵢ`.
- **OLS(최소제곱법):** `Σ(yᵢ − ŷᵢ)²`를 최소화하도록 계수를 구한다.
- 단순회귀의 계수는 `β₁ = Cov(X,Y)/Var(X)`, `β₀ = ȳ − β₁x̄`로 계산할 수 있다.

주요 코드 사용법:

```python
# 방법 1: 예측 중심 — scikit-learn
from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(X_train, y_train)
print(reg.coef_, reg.intercept_)
print(reg.predict(X_test))

# 방법 2: 계수 유의성·모형 해석 — statsmodels
import statsmodels.formula.api as smf
result = smf.ols('sales ~ tv + radio + newspaper', data=df).fit()
print(result.summary())
```

| 도구 | 장점 | 주의사항 |
|---|---|---|
| `scipy.stats.linregress` | 단순회귀, 기울기·p-value 빠른 계산 | 다중회귀 용도는 아님 |
| `sklearn.linear_model.LinearRegression` | 훈련·예측·모델 파이프라인에 적합 | `statsmodels` 같은 `.summary()`는 기본 미제공 |
| `statsmodels.formula.api.ols` | 회귀계수, 표준오차, t값, p값, 신뢰구간 등 통계적 해석 | 예측 성능 평가는 별도로 실시할 것 |

**중요:** 회귀계수의 p-value는 모형 가정과 자료 수집 방법이 타당할 때 통계적으로 해석하며, 낮은 p-value가 높은 예측 정확도를 보장하지 않는다.

### 3.4 회귀 성능지표 및 잔차 진단

| 지표 | 뜻 | 일반적인 방향 |
|---|---|---|
| MAE | `mean(|y − ŷ|)` | 작을수록 좋음 |
| MSE | `mean((y − ŷ)²)` | 작을수록 좋음; 큰 오차에 민감 |
| RMSE | `√MSE` | 작을수록 좋음; 타깃과 단위가 같음 |
| R² | `1 − SSE/SST` | 1에 가까울수록 좋음; 음수도 가능 |
| 수정 R² | 변수 개수와 표본 수를 고려한 설명력 | 불필요한 설명변수 증가에 대한 보정 |

회귀 가정 점검 (`ex10.py`, `ex11.py`):

1. **선형성/모형 지정:** 잔차-적합값 그래프, Ramsey RESET 검정.
2. **오차의 정규성:** Q-Q plot, Shapiro-Wilk 검정. 특히 작은 표본에서 계수에 대한 추론과 관련이 있다.
3. **등분산성:** 잔차가 예측 수준에 따라 일정한 분산인지 확인; Breusch–Pagan 검정.
4. **잔차 독립성:** 시간 순서가 있는 자료 등에서 Durbin–Watson 검정/잔차 시계열 검토.
5. **다중공선성:** VIF(`Variance Inflation Factor`)로 설명변수 사이 중복성을 점검.
6. **영향점:** Cook's distance로 일부 관측치가 계수에 강하게 영향을 주는지 확인.

단, `p >= 0.05`는 가정이 **증명되었다는 뜻은 아니며**, 해당 검정에서 기각할 만한 증거가 충분하지 않다는 의미다.

### 3.5 스케일링·다항회귀·규제 (`ex12`, `ex14`~`ex16`, `prac5`)

- **StandardScaler:** `z = (x − μ_train) / σ_train`; 평균 0, 표준편차 1로 변환.
- **MinMaxScaler:** `(x − min_train)/(max_train − min_train)`; 일반적인 훈련 범위를 0~1로 이동.
- **PolynomialFeatures(degree=2):** `(x₁,x₂)` → `x₁, x₂, x₁², x₁x₂, x₂²` 등의 비선형 항을 생성한다. **변환된 특성에 대해 선형회귀**를 수행하므로 계수 관점에서는 여전히 선형모형이다.
- **Ridge(L2):** 계수 제곱합에 페널티를 주어 큰 계수를 억제.
- **Lasso(L1):** 일부 계수를 정확히 0으로 만드는 변수 선택 특성.
- **ElasticNet:** L1과 L2를 결합.

`ex14.py`는 `Ridge`, `Lasso`, `ElasticNet`을 **import만 하고 실제 학습에는 `LinearRegression`을 사용**한다. 따라서 해당 세 알고리즘을 비교한 실험으로 소개하면 안 된다.

권장 파이프라인(훈련셋에서만 전처리 학습):

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import Ridge

model = make_pipeline(
    StandardScaler(), PolynomialFeatures(degree=2, include_bias=False), Ridge(alpha=1.0)
)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
```

### 3.6 로지스틱 회귀·시그모이드 (`ex17`~`ex21`)

로지스틱 회귀는 이름에 회귀가 붙지만 주로 **분류 모델**로 사용된다.

- 선형 점수: `z = wᵀx + b`
- 시그모이드: `σ(z) = 1 / (1 + e^(−z))`
- 이진 분류: `P(y=1|x) = σ(z)`로 해석할 수 있다.
- 로그오즈(logit): `log(p/(1−p)) = z`. 오즈는 `p/(1−p)`.
- 기본 경계값 0.5에서 `P >= 0.5`면 양성 클래스라고 판단할 수 있지만, 비용·불균형에 따라 조정한다.
- 다중클래스의 경우 로지스틱 회귀는 소프트맥스 등의 접근을 통해 여러 클래스 중 하나를 예측할 수 있다.

```python
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(max_iter=1000).fit(X_train, y_train)
labels = clf.predict(X_test)          # 분류 결과
probs = clf.predict_proba(X_test)     # 클래스별 확률
scores = clf.decision_function(X_test) # 결정 점수 (설정에 따라 모양 상이)
```

### 3.7 분류 성능지표·혼동행렬·ROC/AUC

이진 혼동행렬(행=실제, 열=예측, 클래스 0/1 순서):

| | 0으로 예측 | 1로 예측 |
|---|---:|---:|
| 실제 0 | TN(진음성) | FP(위양성) |
| 실제 1 | FN(위음성) | TP(진양성) |

- 정확도(Accuracy): `(TP+TN)/(TP+TN+FP+FN)`
- 정밀도(Precision): `TP/(TP+FP)` — **양성이라고 예측한 것** 중 실제 양성 비율
- 재현율(Recall/TPR): `TP/(TP+FN)` — **실제 양성** 중 모델이 찾아낸 비율
- 특이도(Specificity/TNR): `TN/(TN+FP)`
- F1-score: `2×Precision×Recall/(Precision+Recall)`
- FPR: `FP/(FP+TN) = 1−Specificity`
- ROC: 여러 분류 임계값에 따른 `TPR` 대 `FPR` 그래프
- AUC: ROC 아래 면적, 양성과 음성을 순위로 구별하는 능력의 지표

```python
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score
pred = clf.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
# 이진분류 예시: 양성(1) 확률로 계산
print(roc_auc_score(y_test, clf.predict_proba(X_test)[:, 1]))
```

**불균형 분류**(예: 불만족 고객이 소수)는 정확도만 높아도 소수 클래스를 못 찾을 수 있다. 관심 클래스의 재현율/정밀도, PR-AUC 및 ROC-AUC를 함께 평가한다.

### 3.8 트리·교차검증·앙상블 (`ex22`~`ex32`)

- **Decision Tree:** 데이터를 조건문 형태로 나누는 비선형 분류기/회귀기. `max_depth`, `min_samples_split`, `min_samples_leaf` 등으로 복잡도를 제어한다.
- **Gini impurity:** `1 − Σpₖ²`; 노드가 한 클래스 위주면 낮다.
- **Entropy:** `−Σpₖ log₂(pₖ)`; 정보이득이 큰 분할을 선호한다.
- **K-Fold:** 학습 데이터를 K조각으로 나누고 검증 조각을 바꿔 가며 K번 평가.
- **StratifiedKFold:** 클래스 비율을 고려한 분류용 K-Fold.
- **GridSearchCV:** 지정한 하이퍼파라미터 조합을 교차검증으로 평가해 최적의 조합을 선택.
- **VotingClassifier:** 개별 모델의 투표(하드) 또는 예측확률 평균(소프트)으로 결정.
- **Random Forest:** 여러 결정트리를 부트스트랩과 특성 무작위 선택으로 학습해 결과를 결합하는 **배깅** 방식.
- **XGBoost/LightGBM:** 앞선 모델의 오차/목적함수를 줄이는 방향으로 트리를 **순차적으로 보강하는 부스팅** 계열. 중요한 설정은 `n_estimators`, `learning_rate`, `max_depth`, `subsample` 등.
- **Feature importance:** 트리 기반 중요도는 해당 모델·학습 데이터에서의 상대적 기여를 요약한다. **인과효과나 절대적 변수 중요도를 뜻하지 않는다.**

### 3.9 SVM·PCA (`ex33`~`ex37`)

- **SVM(Support Vector Machine):** 클래스 간 분리 경계의 **마진**을 넓게 설정하는 방법. 경계에 가까운 데이터(서포트 벡터)가 중요한 역할을 한다.
- **C:** 오분류를 허용하는 규제의 강도에 반비례하는 파라미터. 값이 크면 훈련 오분류를 더 강하게 벌할 수 있다.
- **Kernel:** `linear`는 선형 경계, `rbf`는 비선형 관계를 표현하는 대표적 커널.
- **PCA(Principal Component Analysis):** 변수들의 공분산 구조를 이용해 데이터 분산을 많이 설명하는 축으로 투영하는 **비지도 차원 축소**.
- `explained_variance_ratio_`: 각 주성분이 설명하는 분산 비율.
- `inverse_transform`: 압축된 자료를 원래 특성 공간으로 대략 복원(정보 손실 가능).

차원 축소기 역시 훈련 데이터로만 `fit`해야 한다. `Pipeline(StandardScaler → PCA → SVC)`로 구성하면 데이터 누수를 줄이고 재사용이 편해진다.

### 3.10 나이브 베이즈·KNN (`ex38`~`ex42`)

- **Bayes 정리:** `P(C|X) ∝ P(X|C) P(C)`.
- **Naive Bayes:** 주어진 클래스 조건에서 특성 간 조건부 독립을 가정하는 확률 분류기.
- **GaussianNB:** 연속형 특성의 클래스별 가우스 분포를 사용.
- **MultinomialNB:** 단어 출현 횟수·비음수 카운트형 특성에 자주 적용.
- **BernoulliNB:** 0/1 출현 여부 등 이진 특징에 적합.
- **KNN:** 새 데이터 주변의 가까운 K개 이웃을 다수결로 분류. 거리를 이용하므로 특성의 단위 차이가 큰 경우 스케일링이 중요.
- `n_neighbors`가 너무 작으면 잡음에 민감하고, 너무 크면 경계가 지나치게 부드러워질 수 있다.

### 3.11 퍼셉트론·다층신경망 (`ex43`~`ex.47`)

- **Perceptron:** 입력의 가중합 `wᵀx+b`에 따른 선형 결정경계를 학습한다. 오분류된 샘플을 중심으로 가중치를 갱신한다.
- **단층 퍼셉트론의 한계:** XOR처럼 단일 직선으로 분리할 수 없는 문제를 그대로 풀기 어렵다.
- **MLP(Multi-Layer Perceptron):** 입력층과 출력층 사이에 은닉층을 두어 비선형 패턴을 학습.
- **Activation:** `relu`, `tanh`, `logistic` 등은 은닉층에 비선형성을 부여.
- **Adam:** 적응형 학습률을 사용하는 경사 기반 최적화 알고리즘.
- **Epoch/Iteration:** 데이터를 반복해 학습시키는 과정. scikit-learn MLP의 `max_iter`는 solver 설정과 데이터 형태에 따라 반복 의미를 확인해야 한다.
- **Cross-entropy:** 분류에서 자주 쓰는 손실함수.
- **과적합 완화:** 훈련/검증 분리, 표준화, 규제(`alpha`), 조기종료(`early_stopping`) 등을 고려.

**API 차이(중요):** `LogisticRegression`과 `MLPClassifier`는 `predict_proba()`를 지원하지만 **`Perceptron`은 `predict_proba()`를 제공하지 않는다**. 퍼셉트론 점수를 보려면 `decision_function()`을 사용한다.

---
## 4. 예제 코드 해설 — ex1 ~ ex.47

> 파일명을 누르면 같은 폴더의 해당 소스로 이동한다. 이 설명은 단순히 라이브러리 이름만 나열하는 대신 **무엇을 예측하는지 → 처리 흐름 → 개념 → 주의점** 순서로 기술했다.

### 4.1 기초 통계·상관관계 (ex1~ex3)

#### [`ex1.py`](./ex1.py) — 공분산과 상관계수 직접 계산·비교

- **목적:** 숫자 배열 사이의 관계를 공분산과 피어슨 상관계수로 수치화하고 산점도로 확인한다.
- **흐름:** `np.arange()`로 양의/음의 상관 및 상수 배열 생성 → `np.cov()` 공분산 행렬 출력 → 실제 `x, y` 산점도 → `np.corrcoef()`, `scipy.stats.pearsonr()` 비교 → `y=x²` 모양 자료의 상관계수 확인.
- **핵심 함수:** `np.cov(x,y)[0,1]`는 두 변수의 공분산, `np.corrcoef(x,y)[0,1]`는 상관계수를 반환한다. `pearsonr`는 통계량과 유의성 검정 p-value를 반환한다.
- **이론 핵심:** 단위가 달라지면 공분산 크기는 달라지지만 상관계수는 단위 없는 값이다. 예제 마지막의 U자형 관계는 **비선형 구조가 있어도 피어슨 r이 낮을 수 있음**을 보여준다.

#### [`ex2.py`](./ex2.py) — 음용수 만족도 데이터 상관관계 시각화

- **목적:** `drinking_water.csv`의 `친밀도`, `적절성`, `만족도` 변수가 서로 어떤 선형 관계를 갖는지 탐색한다.
- **흐름:** 원격 CSV 읽기 → 평균·표준편차·공분산 → `corr()`와 `만족도` 기준 정렬 → `scatter_matrix` → 전체/마스킹 히트맵.
- **핵심 코드:** `data.corr()['만족도'].sort_values(ascending=False)`로 목적변수와의 상관 순서를 볼 수 있다. `sns.heatmap(..., annot=True)`는 값을 표시하는 상관 히트맵이다.
- **유의:** `np.bool`은 현재 NumPy 환경에서 오류를 낼 수 있어 `dtype=bool`로 변경하는 것이 좋다. `corr()` 실행 시 문자형 열이 있으면 `numeric_only=True`를 고려한다.

#### [`ex3.py`](./ex3.py) — 서울 관광지와 국가별 방문객 상관분석

- **목적:** 2011~2016년 관광지 입장객 수(`ForNum`)와 중국·일본·미국 방문객 수의 관계를 **월 단위**로 비교한다.
- **흐름:** 관광지 JSON과 국가별 방문객 JSON 4개 로드 → `yyyymm`을 인덱스로 변환 → `pd.merge(..., left_index=True, right_index=True)`로 같은 월 결합 → 관광지별 3개 산점도 및 상관계수 → 주요 5개 관광지 결과를 막대그래프로 요약.
- **핵심 함수:** `processFunc()`는 전체 로드·병합·반복을 담당하고, `setScatterGraph()`는 특정 관광지의 3개 상관계수와 그래프를 생성한다.
- **해석 유의:** 전국 국가별 방문객 수와 특정 관광지 입장객 사이의 상관성일 뿐, 한 국가 방문객이 해당 관광지를 방문한 인과적 증거는 아니다. 계절·연도 추세에 의해 상관이 부풀려질 수도 있다.

### 4.2 선형회귀·OLS·예측 성능 (ex4~ex14)

#### [`ex4.py`](./ex4.py) — 선형회귀 공식 직접 구현

- **목적:** 선형회귀의 가중치와 편향이 어떻게 계산되는지 라이브러리 호출 없이 이해한다.
- **흐름 ①:** `np.vstack([x, ones]).T`로 설계행렬 구성 → `numpy.linalg.lstsq`로 최소제곱 계수 계산 → 회귀 직선과 새로운 입력 예측.
- **흐름 ②:** `MySimpleLinearRegression` 클래스의 `fit()`에서 평균·편차·분산으로 기울기와 절편을 산출하고, `predict()`에서 `w*x+b` 계산.
- **핵심 공식:** `w = Σ(x−x̄)(y−ȳ)/Σ(x−x̄)²`, `b = ȳ−wx̄`. `fit`은 학습, `predict`는 추론이라는 머신러닝 API 형태를 직접 만든다.
- **해석 유의:** 뒤쪽 키·몸무게 자료는 독립적으로 난수 생성된 인공 샘플이므로 실제 인간의 관계를 대표하지 않는다.

#### [`ex5.py`](./ex5.py) — 선형회귀 API 비교 시도 (미완성·오류 포함)

- **목적:** `LinearRegression`과 `statsmodels` OLS의 사용 방식을 비교하려는 예제다.
- **의도된 흐름:** 가상의 `x, y` 생성 → 모델 학습 → 기울기·절편·새 입력 예측 → DataFrame을 만들고 `smf.ols` 결과 요약.
- **실제 코드 상태:** `y = 5*x.ravel() + ... + np.random.normal(0,3,5)`에서 배열 길이가 맞지 않으며, `LinearRegression(n_samples=...)`는 올바른 데이터 생성 방식이 아니다. `np.array([2.34], [6.21], [8.123])`, `smf.ols(formula='y')` 부분도 수정이 필요하다.
- **학습 포인트:** 데이터 생성은 `sklearn.datasets.make_regression(...)`, 학습기는 `LinearRegression().fit(X,y)`, 통계 해석은 `smf.ols('y ~ x', data=df).fit()`을 구분해 사용한다. 원본은 **그대로 실행 가능한 완성 예제로 간주하지 않음**.

#### [`ex6.py`](./ex6.py) — IQ와 점수의 단순회귀 (`linregress`)

- **목적:** `score_iq.csv`의 IQ와 시험점수 사이 관계를 단순선형회귀로 살핀다.
- **흐름:** CSV 로드 → `np.corrcoef`, `df[['iq','score']].corr()` 확인 → `scipy.stats.linregress()` 실행 → `slope`, `intercept`, `pvalue` 표시 → 산점도에 회귀 직선 중첩.
- **이론:** `linregress`는 피어슨 상관과 회귀 기울기가 어떻게 연결되는지 이해하기 좋은 경량 함수다. p-value는 기본적으로 기울기가 0이라는 귀무가설을 검정한다.
- **주의:** 데이터 사이의 통계적 연관성을 분석하는 것이며 개인의 점수를 단정하는 용도로 적합하지 않다.

#### [`ex7.py`](./ex7.py) — 만족도 예측 및 잔차·RSS·MSE 계산

- **목적:** 음용수 `적절성`으로 `만족도`를 예측하는 OLS 회귀모델을 만든다.
- **흐름:** `smf.ols('만족도 ~ 적절성', data=df).fit()` → `summary()`, `params`, `rsquared`, `pvalues` 확인 → 산점도·추세선 → 실제값/예측값/잔차 표 작성 → RSS, MSE, RMSE 계산 → 새 적절성 값 예측.
- **핵심:** `model.resid`는 잔차, `model.ssr`은 잔차제곱합(RSS)이다. `predict(pd.DataFrame({'적절성': [...]}))`는 원래 공식에서 사용하는 변수명과 일치해야 한다.
- **주의:** 같은 데이터로 구한 잔차 기반 점수는 **학습 데이터의 적합도**이며 미지 데이터에 대한 일반화 성능은 별도 테스트가 필요하다.

#### [`ex8.py`](./ex8.py) — 약한·강한 상관과 회귀 설명력 비교

- **목적:** 아이리스에서 `sepal_width → sepal_length`와 `petal_length → sepal_length`를 비교하고, 이어 다중회귀를 만든다.
- **흐름:** `sns.load_dataset('iris')` → 두 단순회귀 결과의 `R²`, p-value 확인 → 산점도와 예측선 → 새 꽃잎 길이 예측 → 다중회귀 공식 자동 구성.
- **핵심:** 독립변수와 타깃의 선형 상관이 높은 경우 같은 데이터에서의 단순회귀 설명력이 높아질 수 있음을 보여준다.
- **주의:** 설명력과 인과성은 다르다. 산점도에 회귀선을 그릴 때 `x`를 정렬해야 선이 뒤엉키지 않는다.

#### [`ex9.py`](./ex9.py) — 자동차 연비의 단순·다중회귀

- **목적:** `mtcars` 데이터에서 마력(`hp`)과 무게(`wt`)가 연비(`mpg`)와 어떻게 관련되는지 비교한다.
- **흐름:** `get_rdataset('mtcars')` 로드 → `mpg ~ hp` OLS → 마력 100~250에 대한 예측 → `mpg ~ hp + wt` 다중 OLS → 계수·수정 R² 확인 → 실제값 대 예측값 그래프.
- **핵심:** 다중회귀의 각 계수는 **다른 독립변수가 일정하다는 조건**에서 해석한다. 새 입력을 `pd.DataFrame({'hp':..., 'wt':...})`로 만드는 방식도 학습한다.
- **주의:** 예측 입력이 실제 훈련 분포에서 많이 벗어나면 외삽 문제가 커질 수 있다.

#### [`ex10.py`](./ex10.py) — 광고비·매출 다중회귀와 회귀 가정 진단

- **목적:** TV·라디오·신문 광고비(`tv`, `radio`, `newspaper`)를 이용해 `sales`를 설명하고 적합성을 검토한다.
- **흐름:** CSV → `sales ~ tv + radio + newspaper` 회귀 → 새 광고비 시나리오 예측 → 잔차 계산 → Shapiro-Wilk, Q-Q plot → Ramsey RESET → Breusch–Pagan → Cook's distance 및 영향점 그래프.
- **핵심 코드:** `smf.ols(...).fit()`, `linear_reset`, `het_breuschpagan`, `OLSInfluence(lm).cooks_distance`.
- **실제 코드 주의:** RESET 결과를 `reset_result`에 담고도 조건문은 앞서 계산한 **Shapiro p-value(`pv`)**를 재사용한다. 선형성 판정에는 반드시 `reset_result.pvalue`를 써야 한다. 다변량 잔차 분석에서 일부 검정·그래프는 `tv` 단독이 아닌 전체 설명변수로 구성하는 편이 타당하다.

#### [`ex11.py`](./ex11.py) — Carseats 매출 예측과 다중공선성 점검

- **목적:** `Carseats.csv`에서 `Sales`를 타깃으로 `Income`, `Advertising`, `Price`, `Age`를 설명변수로 선택해 회귀한다.
- **흐름:** 불필요한 열 삭제 → `Sales ~ Income + Advertising + Price + Age` → 실제/예측/잔차 비교 → Shapiro, RESET, Breusch–Pagan, Durbin–Watson, VIF → 모델을 `carseat.pickle`로 저장·불러오기 → 신규 조건의 Sales 예측.
- **이론:** VIF는 각 설명변수가 나머지 설명변수로 얼마나 잘 설명되는지를 나타내며, 다중공선성이 클수록 계수 추정의 안정성이 저하될 수 있다. Durbin–Watson은 잔차의 1차 자기상관을 가늠한다.
- **코드 주의:** 열을 `df.columns[6]` 같은 **위치 번호로 삭제**하면 파일 열 순서가 바뀔 때 다른 변수를 지울 수 있으므로 열 이름 기준으로 선택하는 편이 안전하다. `pickle` 파일은 신뢰할 수 있는 로컬에서만 읽는다.

#### [`ex12.py`](./ex12.py) — MinMax 스케일링과 회귀 성능지표 구현

- **목적:** 난수 기반 연속형 데이터를 만들어 `LinearRegression` 결과와 회귀 점수들을 비교한다.
- **흐름:** `x`, `y` 생성 → `MinMaxScaler.fit_transform(x.reshape(-1,1))` → 선형회귀 → `r2_score`, `explained_variance_score`, `mean_squared_error`, `sqrt(MSE)` 출력 → 분포를 달리한 두 번째 실험.
- **핵심:** 1차원 벡터 `x`를 `reshape(-1,1)`로 2차원 특성 행렬로 바꾸는 이유, R²와 RMSE가 나타내는 정보를 익힌다.
- **실제 코드 주의:** 두 번째 모형의 `score` 호출에서 `x_scaled`와 `x_scaled2`가 혼용되므로 데이터 짝을 맞춰야 한다. 스케일러 재학습도 이전 데이터의 변환 기준을 덮어쓴다는 점에 유의한다.

#### [`ex13.py`](./ex13.py) — scikit-learn을 이용한 mtcars 마력→연비 예측

- **목적:** `ex9`와 유사한 문제를 이번에는 `LinearRegression` 중심으로 구현한다.
- **흐름:** `mtcars` 로드 → `X=hp`, `y=mpg` 분리 → `fit`, `coef_`, `intercept_` → `predict` → MSE/RMSE/R² → `hp=100,110,120`일 때 예측.
- **핵심:** scikit-learn에서 입력 `X`는 `(샘플 수, 특성 수)`의 2차원 배열이어야 하며 `[[100],[110],[120]]`처럼 넣는다.
- **주의:** 현재 학습 데이터에 대해 바로 평가하므로 실제 성능 비교에는 별도 테스트 분할이 필요하다.

#### [`ex14.py`](./ex14.py) — Iris를 이용한 선형회귀와 Train/Test 분리

- **목적:** 아이리스 **꽃잎 길이(petal length)**로 **꽃잎 너비(petal width)**를 예측하는 연속값 회귀 실습이다.
- **흐름:** `load_iris()` → DataFrame 구성 → `train_test_split(test_size=0.3)` → `LinearRegression.fit` → 테스트 예측과 `r2_score`.
- **핵심:** 아이리스 데이터가 보통 분류에 쓰이지만, 특정 연속형 특성을 타깃으로 잡으면 회귀 문제로도 설계할 수 있음을 확인한다.
- **주의:** `Ridge`, `Lasso`, `ElasticNet`을 import했지만 실제 학습/평가는 선형회귀 하나만 수행한다. 그래프 선 연결은 `x` 정렬 후 그리는 것이 적절하다.

### 4.3 다항회귀·로지스틱 회귀 (ex15~ex21)

#### [`ex15.py`](./ex15.py) — 직선과 2차 다항회귀 비교

- **목적:** 직선으로 설명하기 어려운 5개 점을 `degree=2` 다항 특성으로 더 유연하게 표현한다.
- **흐름:** `x=[1,2,3,4,5]` → 일반 `LinearRegression` → `PolynomialFeatures(degree=2, include_bias=False)` → 확장 특성(`x`, `x²`)으로 재학습 → 두 예측 결과 시각화.
- **핵심:** 원래 입력을 `x[:, np.newaxis]`로 2차원 변환하는 방법과 다항회귀가 `x²` 항을 추가한다는 사실.
- **실제 코드 주의:** 두 번째 모델의 결정계수 출력이 `r2_score(y, ypred)`로 되어 있다. **다항회귀 점수는 `r2_score(y, ypred2)`**로 계산해야 한다. 표본이 5개뿐이므로 과적합 판단에는 주의한다.

#### [`ex16.py`](./ex16.py) — 주택가격에 대한 1·2·3차 회귀

- **목적:** 주택가격(`MEDV`)과 `LSTAT`의 관계를 선형·2차·3차 다항회귀로 적합하여 형태 차이를 본다.
- **흐름:** 원격 `housing.data` → `LSTAT`, `MEDV` 선택 → `PolynomialFeatures(degree=2/3)` → 각 모델 훈련 → R² 계산 → 예측곡선 그래프.
- **이론:** 다항 차수가 커질수록 훈련 데이터 적합도는 높아질 수 있지만 일반화 성능이 좋아진다고 보장할 수 없다.
- **실제 코드 주의:** 2·3차 그래프 라벨에서도 1차 `model_r2`를 사용하고 있어 각각 `q_r2`, `c_r2`로 수정해야 한다. 데이터셋에는 사회적으로 민감하거나 시대에 뒤떨어진 특성이 있으므로 **모델 학습용 역사적 자료**로만 다룬다.

#### [`ex17.py`](./ex17.py) — 시그모이드 함수 구현과 확률 시각화

- **목적:** 분류에서 연속적인 점수를 0~1 범위의 값으로 바꾸는 시그모이드 함수의 동작을 이해한다.
- **흐름:** `math.exp`를 이용해 한 값에 적용하는 `MySigmoidFunc` 구현 → `np.exp` 배열 버전 `OurSigmoidFunc` 구현 → `z = w*x + b` → `sigmoid(z)` 곡선을 그려 0.5 임계값 확인.
- **핵심:** z가 0이면 확률은 0.5, 큰 양수면 1에, 큰 음수면 0에 가까워진다.
- **주의:** 실습에서 직접 정한 `w`, `b`는 학습 데이터로 추정된 회귀계수가 아니다. 시그모이드 출력이 확률로 해석되려면 적절히 학습되고 보정된 모델이 전제된다.

#### [`ex18.py`](./ex18.py) — 수동변속기 여부에 대한 statsmodels Logit/GLM

- **목적:** `mtcars`의 `mpg`, `hp`로 자동/수동변속기 변수 `am`을 이진분류한다.
- **흐름:** `smf.logit` 이항분류 → `summary()`, 예측확률 및 0.5 임계값 → 혼동행렬/정확도 → `smf.glm(..., family=Binomial())` 비교 → 새로운 연비·마력 입력을 예측.
- **핵심:** `statsmodels`의 `Logit`과 Binomial GLM을 비교하고 확률을 분류 클래스로 바꾸는 원리를 학습한다.
- **주의:** 전체 자료에서 학습·평가하고 있어 정확도가 낙관적으로 보일 수 있다. 학습 자료 바깥의 비현실적 입력(`mpg=120`, `130`)은 외삽에 해당한다.

#### [`ex19.py`](./ex19.py) — 날씨 데이터로 내일 비 여부 예측

- **목적:** `weather.csv`의 기상 변수를 사용하여 `RainTomorrow`를 0/1로 분류한다.
- **흐름:** `Date`, `RainToday` 삭제 → `RainTomorrow`를 Yes=1/No=0 매핑 → 훈련/테스트 분리 → 열 이름을 합쳐 `RainTomorrow ~ ...` 공식 생성 → `smf.logit(...).fit()` → `pred_table`, 혼동행렬, 정확도 계산.
- **핵심:** 범주형 정답을 수치형 타깃으로 변환하고 훈련/테스트에서 평가를 분리한다.
- **주의:** 결측값·데이터 타입에 따라 Logit이 실패할 수 있으므로 `isna()`, `dtypes` 확인이 우선이다. 실제 시계열 예측에서는 단순 무작위 분할 대신 시간순 분리를 고려한다.

#### [`ex20.py`](./ex20.py) — Iris 다중클래스 로지스틱 회귀·모델 저장

- **목적:** 꽃잎 길이·너비(`iris.data[:, [2,3]]`)로 아이리스 품종 3개를 예측한다.
- **흐름:** `train_test_split` → `LogisticRegression(solver='lbfgs')` → 정확도·혼동행렬·train/test 점수 → `joblib.dump/load` → 새 입력의 클래스와 `predict_proba()` → 2차원 분류 경계 시각화.
- **핵심:** 분류기에서 `predict()`는 클래스 번호, `predict_proba()`는 클래스별 예측확률을 반환한다. `np.trace(conf_mat) / np.sum(conf_mat)`는 혼동행렬 기반 정확도다.
- **실제 코드 주의:** 경계 그래프에 쓸 `x2_min/max`가 `X[:,0]`을 참조하고 있으며 테스트 포인트 표시용 `c=[]`도 오류를 유발할 수 있다. 여러 예제가 모두 `ex20model.sav`를 사용하므로 저장파일이 덮어써질 수 있다.

#### [`ex21.py`](./ex21.py) — 분류 정확도·정밀도·재현율·ROC/AUC

- **목적:** 합성 이진분류 자료(`make_classification`)와 로지스틱 회귀로 성능지표를 익힌다.
- **흐름:** 합성 2특성 생성 → `LogisticRegression.fit()` → 예측·결정점수 출력 → `confusion_matrix`, 수동 성능지표 계산 → `classification_report` → `roc_curve`, `auc` 시각화.
- **핵심:** `decision_function`은 결정 임계값 분석에 쓸 점수이며, ROC는 임계값을 달리하면서 민감도와 위양성률 간 균형을 그린다.
- **실제 코드 주의:** `(44+44)/100` 같은 **수동 계산 값은 특정 결과를 가정한 상수**이므로 혼동행렬에서 동적으로 계산하는 것이 안전하다. 그림의 y축은 `plt.xlabel('tpr...')`가 아니라 `plt.ylabel('tpr...')`여야 한다. 별도 테스트 분할이 없어 학습 성능만 나타낸다.

### 4.4 결정트리·앙상블·부스팅 (ex22~ex32)

#### [`ex22.py`](./ex22.py) — 합성 데이터 결정트리 분할 시각화

- **목적:** 2개 입력변수의 합성 분류 데이터에서 트리가 공간을 어떤 규칙으로 나누는지 확인한다.
- **흐름:** `make_classification` → `DecisionTreeClassifier(criterion='gini', max_depth=3)` → 모델 학습 → `plot_tree`로 분할 규칙과 노드 시각화 → 격자점 예측으로 결정경계 그리기.
- **핵심:** 분할 기준이 지니 불순도를 낮추고 `max_depth`가 트리의 복잡도를 제한한다.
- **실제 코드 주의:** `np.linspace(x[:,0].min(), x[:,0].min(), 100)`처럼 시작값·끝값이 동일해 격자가 한 점으로 고정된다. 끝값은 각각 `.max()`로 고쳐야 2차원 결정경계가 나온다.

#### [`ex23.py`](./ex23.py) — 키·머리 길이 2특성으로 트리 규칙 학습

- **목적:** 아주 작은 인공 예제에서 엔트로피 기준 결정트리를 시각적으로 익힌다.
- **흐름:** 수작업으로 만든 `height`, `hair_length` 특성 10개 → 문자열 분류 레이블 → `DecisionTreeClassifier(criterion='entropy', max_depth=3)` → 학습·새 입력 예측 → `plot_tree`.
- **핵심:** 트리가 `feature <= threshold` 질문을 누적해 분류하는 과정을 그림에서 확인한다.
- **주의:** 키·머리 길이만으로 실제 사람의 성별을 추정하는 것은 타당하지 않다. **교육용 인공 데이터와 트리 작동 원리 설명으로만** 해석해야 한다.

#### [`ex24.py`](./ex24.py) — Iris 결정트리 학습·평가·직렬화

- **목적:** Iris 품종 3개를 `DecisionTreeClassifier(criterion='entropy', max_depth=5)`로 분류한다.
- **흐름:** 데이터 분할 → 트리 학습 → 정확도·혼동행렬 → `joblib.dump`·`load` → 새 꽃잎 데이터 예측확률 → 결정경계 표시.
- **핵심:** `max_depth`를 조절해 훈련 데이터 암기 가능성을 제한하며 로지스틱 회귀(`ex20`)와 다른 비선형 결정경계를 비교한다.
- **주의:** `ex20model.sav`를 다른 예제와 공유하여 덮어쓰며 결정경계 그리기 함수도 `ex20`의 축 참조 오류를 그대로 포함한다.

#### [`ex25.py`](./ex25.py) — 과적합과 K-Fold·GridSearchCV

- **목적:** 같은 데이터를 학습과 평가에 사용한 경우, 홀드아웃 분할, K-Fold 검증을 각각 비교한다.
- **흐름:** 전체 Iris에 트리 학습·동일 자료 평가 → `train_test_split` → `KFold(n_splits=5)`로 직접 5회 반복 → `cross_val_score` 단축 사용 → `GridSearchCV`로 `max_depth`, `min_samples_split` 조합 탐색.
- **핵심:** 학습 점수가 높다고 새로운 데이터에서 잘 작동한다는 보장은 없다. 그리드 서치는 검증 점수로 **하이퍼파라미터**를 고른 뒤 미사용 테스트에서 평가한다.
- **실제 코드 오류:** `cross_val_score(..., scoring='scoring', cv=5)`는 유효하지 않은 점수 문자열이다. `scoring='accuracy'`로 수정해야 한다. Iris 분류에서는 클래스 비율을 보존하는 `StratifiedKFold`도 적합하다.

#### [`ex26.py`](./ex26.py) — 유방암 데이터 소프트 보팅 앙상블

- **목적:** `load_breast_cancer()`에 대해 로지스틱 회귀, KNN, 결정트리를 함께 사용하는 `VotingClassifier`를 만든다.
- **흐름:** 레이블별 개수 계산 → `stratify=y`로 분할 → LR·KNN에는 `make_pipeline(StandardScaler(), ...)`, 트리에는 단독 모델 사용 → 각 모델 정확도 비교 → `VotingClassifier(voting='soft')` → `StratifiedKFold` 5겹 평가 → `classification_report`, ROC-AUC.
- **핵심:** 소프트 보팅은 개별 모델의 확률 예측을 결합한다. LR·KNN에만 표준화가 필요하다는 모델별 차이, `Pipeline`을 이용한 전처리 누수 방지 방식을 보여준다.
- **해석:** 이 데이터의 타깃 0은 악성, 1은 양성으로 정의돼 있다. 코드의 `roc_auc_score(y_test, predict_proba[:,1])`는 **클래스 1(양성)을 양성 클래스**로 본 점수다. 실제 악성 탐지 실무 지표와 혼동하지 않는다.

#### [`ex27.py`](./ex27.py) — Titanic 생존 예측·랜덤포레스트 중요도

- **목적:** `Pclass`, `Age`, `Sex`로 승객 생존 여부(`Survived`)를 분류한다.
- **흐름:** 원격 Titanic CSV → 필수 변수 결측 행 제거 → `Sex`를 `LabelEncoder`로 숫자 변환 → `RandomForestClassifier(n_estimators=500)` → 테스트 정확도·5겹 교차검증·특성 중요도 → 추가 6개 변수 사용 시도.
- **핵심:** 랜덤포레스트는 다수의 결정트리를 조합해 단일 트리보다 안정적인 예측을 추구한다. `feature_importances_`는 학습된 트리 분할에서 계산한 상대적 중요도다.
- **실제 코드 오류:** 후반부의 `df.imsi['Sex']`는 DataFrame의 존재하지 않는 속성을 참조한다. `df_imsi['Sex']`로 수정해야 한다. `df_x` 슬라이스에 바로 값을 대입하는 부분도 `.copy()` 사용을 권장한다.

#### [`ex28.py`](./ex28.py) — Iris 랜덤포레스트 분류·경계 비교

- **목적:** 동일한 Iris 2특성/3클래스 문제에 `RandomForestClassifier(criterion='entropy', n_estimators=500)` 적용.
- **흐름:** Train/Test 분리 → 500개 트리 앙상블 학습 → 정확도·혼동행렬 → 모델 저장 및 재로딩 → 새 표본 분류확률 → 결정경계 시각화.
- **핵심:** `ex20`(LogisticRegression), `ex24`(DecisionTree), `ex28`(RandomForest)를 같은 데이터 설정에서 비교하기 좋다.
- **주의:** 모델 저장 파일명이 다른 예제와 중복되며 결정경계 시각화 함수에는 동일한 격자·테스트 표시 문제가 남아 있다.

#### [`ex29.py`](./ex29.py) — California 주택가격 랜덤포레스트 회귀

- **목적:** `fetch_california_housing`의 여러 지역 특성으로 `MedHouseVal`을 예측한다.
- **흐름:** `as_frame=True`로 DataFrame 로드 → 타깃/특성 분리 → 70/30 분할 → `RandomForestRegressor(n_estimators=200)` 학습 → 테스트 MSE·R² → 중요도 순위표 및 막대그래프.
- **핵심:** 랜덤포레스트는 `Regressor`로 연속형 가격도 예측한다. 트리 앙상블에서 스케일링이 상대적으로 덜 중요하다는 점을 이해할 수 있다.
- **주의:** 지역 평균값을 다루는 과거 자료이므로 실제 개별 부동산 감정가의 근거로 사용하면 안 된다. 처음 실행 시 데이터 다운로드가 필요할 수 있다.

#### [`ex30.py`](./ex30.py) — XGBoost vs LightGBM 성능·중요도 비교

- **목적:** `load_breast_cancer()`의 이진 분류에 두 가지 그래디언트 부스팅 모델을 학습하여 비교한다.
- **흐름:** 80/20 층화 분리 → `xgb.XGBClassifier`와 `LGBMClassifier` 학습 → 테스트 정확도 비교 → `gain` 기준 중요도를 백분율로 정규화 → 상위 5개 변수 그래프.
- **핵심:** XGBoost/LightGBM은 모두 순차적 트리 보강 계열이지만 구현·분할 전략과 하이퍼파라미터가 다르다. `gain` 중요도는 해당 모델에서 손실 감소에 대한 기여도로 해석한다.
- **실제 코드 주의:** XGBoost 생성자의 `n_estimator=200`은 **`n_estimators`의 오타**다. 잘못된 설정이 무시되거나 경고될 수 있으므로 수정해야 한다. 성능은 실제 실행 결과를 확인해야 한다.

#### [`ex31.py`](./ex31.py) — Iris XGBoost 다중클래스 분류

- **목적:** `ex20`과 동일한 Iris 꽃잎 2특성 분류를 `XGBClassifier`로 수행한다.
- **흐름:** Train/Test → XGBoost 트리 앙상블 → 정확도·혼동행렬 → joblib 저장·재사용 → 새 데이터 확률 → 결정경계.
- **핵심:** 기존 알고리즘과 같은 입력/분할에서 모델만 바꾸어 결과를 비교하는 학습 패턴이다.
- **주의:** 이 파일에도 `n_estimator` 오타가 있으며 `ex20model.sav` 덮어쓰기와 시각화 함수의 격자 오류가 있다.

#### [`ex32.py`](./ex32.py) — Santander 고객 불만족 분류·AUC·튜닝

- **목적:** 대용량 `train.csv`의 `TARGET`으로 고객 불만족 여부를 예측하는 이진 분류다.
- **흐름:** `latin-1` CSV 로드 → `TARGET` 분포 분석 → `var3`의 `-999999` 센티널값을 대체 → `ID` 제거 → 특징·타깃 분리 → XGBoost 학습 → 확률 기반 ROC-AUC·정확도 → `GridSearchCV`로 `max_depth`, `min_child_weight`, `colsample_bytree` 탐색 → 재학습 및 Recall 계산.
- **핵심:** 소수 클래스가 존재할 때 `accuracy`보다 **ROC-AUC, Recall**을 함께 보아야 한다. 센티널값 처리는 결측값/특이값을 구분하는 데이터 이해 단계다.
- **실제 코드 주의:** `train.csv`는 약 59MB로 웹 업로드 시 제한에 걸릴 수 있다. 또한 GridSearchCV 중 평가용 `x_test, y_test`를 `eval_set`으로 전달하면 독립 테스트셋의 지위가 약해진다. 튜닝에는 학습 내부의 검증/교차검증만 쓰고 최종 테스트는 마지막 한 번 수행한다. `var3.replace(..., inplace=True)`는 pandas 버전에 따른 경고 가능성이 있다.

### 4.5 SVM·PCA·이미지 분류 (ex33~ex37)

#### [`ex33.py`](./ex33.py) — 선형 SVM 마진·서포트벡터 시각화

- **목적:** 두 개의 군집으로 구성된 인공 분류 문제에서 SVM의 **결정경계와 양쪽 마진**을 직접 확인한다.
- **흐름:** `make_blobs` → 레이블을 -1/+1로 변환 → `SVC(kernel='linear', C=1.0)` → 2차원 그리드의 `decision_function` 계산 → 등고선 `-1,0,+1` 표시 → `support_vectors_` 강조.
- **핵심:** 경계 `0`과 마진 `±1`의 기하학적 의미, 모델이 분류를 결정하는 핵심 표본(서포트벡터)을 배운다.
- **주의:** `x_new` 위치는 그림에 찍지만 이 코드에서는 해당 입력의 실제 `predict` 결과를 출력하지 않는다.

#### [`ex34.py`](./ex34.py) — XOR로 선형모델의 한계 확인

- **목적:** XOR 진리표(`00→0`, `01→1`, `10→1`, `11→0`)를 로지스틱 회귀와 **선형 커널** SVM으로 각각 학습한다.
- **흐름:** XOR 데이터를 DataFrame으로 변환 → `LogisticRegression`, `SVC(kernel='linear')` 훈련 → 동일 자료 예측 정확도 계산.
- **핵심:** XOR은 한 개의 직선으로 완전 분리할 수 없어서 두 선형 분류기에는 본질적인 제약이 있다. 비선형 커널(`rbf`) 또는 다층신경망(`ex45`)과 비교할 수 있다.
- **주의:** 이 4개 샘플은 알고리즘 원리 교육용 자료로, 실전 검증 데이터가 아니다.

#### [`ex35.py`](./ex35.py) — Iris SVM 분류·모델 저장

- **목적:** 꽃잎 길이·너비로 Iris 품종을 `SVC(C=100, kernel='linear')`로 분류한다. 코드에는 RBF 커널 비교용 주석도 있다.
- **흐름:** 분할 → SVM 학습 → 테스트 정확도·혼동행렬 → joblib 저장/불러오기 → 새 입력 예측 → 경계 시각화.
- **핵심:** `C`는 잘못 분류한 훈련 샘플에 대한 벌점과 경계의 유연성에 영향을 준다. RBF 커널은 비선형 경계를 만들 수 있다.
- **주의:** SVM은 스케일링에 민감할 수 있지만 원본 코드의 스케일러 부분은 주석 처리되어 있다. `SVC`는 기본적으로 `predict_proba`가 비활성화돼 있으며, 확률을 사용하려면 설계 단계에서 `probability=True` 등 추가 고려가 필요하다.

#### [`ex36.py`](./ex36.py) — PCA 주성분 분석·압축·복원·SVM 비교

- **목적:** Iris 원본 특성을 2차원으로 투영하여 분산이 큰 방향의 의미를 이해하고 차원 축소 전후 SVM을 비교한다.
- **흐름:** 벡터 `flatten()` 예시 → Iris 일부 2특성의 주성분 시각화 → `PCA.fit_transform`, `components_`, `inverse_transform` → 전체 4특성을 2특성으로 축소 → `explained_variance_ratio_` → 원본/축소 자료 각각에 `SVC` 적용.
- **핵심:** PCA는 정답 레이블 없이 데이터를 축소하며, 원복은 근사 복원일 수 있다. 2차원 분산 방향과 원래 변수의 물리적 의미가 항상 일치하지는 않는다.
- **주의:** 마지막 정확도는 각 모델이 **학습한 동일 데이터**에서 계산됐으므로 일반화 비교가 아니다. 비교하려면 분할 후 훈련 전용 PCA를 사용한다.

#### [`ex37.py`](./ex37.py) — LFW 얼굴 이미지 PCA + SVM 분류

- **목적:** 얼굴 이미지의 높은 픽셀 차원을 PCA로 줄이고 SVM으로 여러 사람의 클래스를 분류하는 예제다.
- **흐름:** `fetch_lfw_people(min_faces_per_person=60, resize=0.5)` 다운로드 → 이미지 표시 → `PCA(n_components=0.95)` 및 `PCA(n_components=150, whiten=True)`로 특성 축소·고유얼굴(eigenfaces) 시각화 → `make_pipeline(PCA, SVC)` → 분할·분류 → 혼동행렬·보고서 → 제공된 `bush.jpeg` 전처리 후 예측.
- **핵심:** 고차원 이미지의 차원 축소, `whiten=True`의 역할, 훈련/검증을 파이프라인으로 묶는 장점을 이해한다.
- **주의:** 시각화용 PCA를 전체 자료에 먼저 fit하는 구간이 있지만, **최종 학습에 사용한 Pipeline은 분할 후 재학습**한다. 별도 얼굴 JPEG는 픽셀 크기뿐 아니라 학습 데이터와 조명·정렬·정규화 조건도 맞춰야 하며, 예측은 신뢰할 수 있는 인물 식별 수단이 아니다. 최초 실행 시 네트워크가 필요하다.

### 4.6 나이브 베이즈·최근접이웃 (ex38~ex42)

#### [`ex38.py`](./ex38.py) — GaussianNB로 내일 비 예측

- **목적:** `weather.csv`의 날씨 변수로 다음 날 강수 여부를 예측한다.
- **흐름:** `Date` 삭제 → Sunshine 결측값 평균 대체, RainToday/RainTomorrow 숫자화 → `GaussianNB` → 층화 분할 → 정확도·혼동행렬·교차검증 → 클래스 평균 차이(`theta_`)로 변수 순위 표시 → 새 기상 조건 예측.
- **핵심:** GaussianNB의 조건부 독립성 가정, 연속형 특성의 클래스별 평균·분산 기반 확률 계산.
- **주의:** `abs(theta_[1]−theta_[0])`는 **변수 단위 차이를 고려하지 않은 평균차이**이며 표준적인 중요도 지표가 아니다. 결측값 대체를 전체 데이터에서 수행하면 누수가 될 수 있어 훈련셋 안의 `SimpleImputer`가 적절하다.

#### [`ex39.py`](./ex39.py) — 단어 빈도 기반 스팸메일 분류

- **목적:** 간단한 한국어 문장 6개를 스팸(`spam`)·일반(`ham`)으로 분류한다.
- **흐름:** 문장 리스트와 레이블 생성 → `CountVectorizer.fit_transform`으로 단어별 카운트 행렬 → `MultinomialNB.fit` → 정확도 → 새 메시지 2개에 `transform`만 적용 → 예측 클래스 및 확률 출력.
- **핵심:** Bag-of-Words(BoW), 문장-단어 행렬의 희소성, 나이브베이즈의 확률적 분류를 익힌다.
- **주의:** 6문장에 대한 훈련 정확도는 일반화 지표가 아니다. 한국어는 형태소 분석·토큰화 방식에 따라 성능 차이가 크다.

#### [`ex40.py`](./ex40.py) — 3특성 KNN과 거리 가중치

- **목적:** 작은 3차원 수치 자료 3개로 `KNeighborsClassifier(n_neighbors=3, weights='distance')`를 직접 익힌다.
- **흐름:** `train` 3×3 배열·정답 → 일부 특성 산점도 → KNN 학습·동일 데이터 예측 → 새로운 3특성 데이터 2개 분류.
- **핵심:** 거리 가중치(`weights='distance'`)에서는 가까운 이웃의 투표가 더 큰 영향을 준다. `n_neighbors`는 학습 샘플 수를 초과하면 안 된다.
- **주의:** 학습 자료 3개를 다시 예측한 `score`는 독립 테스트 정확도가 아니다. 시각화는 2개 특성만 보이지만 실제 분류에는 3개가 사용된다.

#### [`ex41.py`](./ex41.py) — Iris KNN 분류·경계·모델 저장

- **목적:** Iris 꽃잎 2특성을 이용해 `KNeighborsClassifier(n_neighbors=5)`로 3개 품종 분류.
- **흐름:** 70/30 분할 → KNN 학습 → 정확도·혼동행렬 → joblib 저장 → 새 꽃잎 데이터의 클래스 및 확률 → 결정경계 표시.
- **핵심:** KNN은 별도의 복잡한 선형 결정계수를 학습하지 않고, 예측 시 저장된 훈련 샘플과의 거리를 사용한다.
- **주의:** 코드의 스케일러가 주석 처리되어 있다. 거리 기반 모델에는 `StandardScaler` 파이프라인이 효과적일 수 있다. 결정경계/저장파일 관련 주의점은 `ex20`과 동일하다.

#### [`ex42.py`](./ex42.py) — 유방암 데이터에서 최적 K 탐색

- **목적:** 유방암 30개 수치 특성으로 KNN을 학습하면서 `n_neighbors`에 따른 Train/Test 정확도를 비교한다.
- **흐름:** 데이터 분할 → `StandardScaler` → K 후보별 KNN 반복 학습 → 훈련·테스트 정확도 리스트 → 최고 점수의 K 산출 → K-정확도 그래프.
- **핵심:** `k`가 작을수록 복잡도가 커지는 경향이 있고, 큰 k는 과소적합으로 이어질 수 있다.
- **주의:** **테스트셋을 이용해 최적 K를 직접 선택한 뒤 동일 테스트 성능을 최종 성능이라고 보고하면 선택 편향**이 생긴다. K는 학습셋 내부 교차검증으로 정하고 별도 테스트에서 최종 평가하는 방식이 바람직하다.

### 4.7 퍼셉트론·MLP (ex43~ex.47)

#### [`ex43.py`](./ex43.py) — AND 논리회로·직선 결정경계 퍼셉트론

- **목적:** 단층 퍼셉트론의 가중치 갱신 방식과 선형 결정경계를 이해한다.
- **흐름:** AND 진리표(`00,01,10,11`) 학습 → `Perceptron(max_iter=100)` 예측 → 별도의 2특성 5표본 학습(`eta0=0.1`) → `coef_`, `intercept_` → `w₁x₁+w₂x₂+b=0` 직선 시각화.
- **핵심:** 오분류 시 가중치를 갱신하는 학습 원리와 결정경계 계산 `x₂=−(w₁x₁+b)/w₂`.
- **주의:** `w₂ == 0`인 경우 직선 계산에서 0으로 나누지 않도록 분기해야 한다. 논리회로 훈련 점수는 모델 평가 목적의 별도 테스트가 아니다.

#### [`ex44.py`](./ex44.py) — Iris 다중클래스 퍼셉트론과 결정 점수

- **목적:** Iris 꽃잎 길이·너비로 `Perceptron(max_iter=1000, eta0=0.1)` 분류를 수행한다.
- **흐름:** Train/Test → 퍼셉트론 학습 → 정확도·혼동행렬 → 저장/불러오기 → 새 입력 예측 → `decision_function`으로 결정점수 확인 → 경계 시각화.
- **핵심:** 선형 분류기의 기본 구조와 `LogisticRegression` 대비 **확률 예측 API의 차이**를 배운다.
- **중요:** `Perceptron`에는 `predict_proba()`가 없으므로 이 예제처럼 `decision_function()`을 써야 한다. 출력 점수는 보정된 확률이 아니다.

#### [`ex45.py`](./ex45.py) — XOR·초승달 데이터 MLP 분류

- **목적:** 은닉층을 둔 신경망으로 선형 분리가 어려운 자료를 예측한다.
- **흐름 ①:** AND/OR/XOR 레이블 중 XOR 선택 → `MLPClassifier(hidden_layer_sizes=10, solver='adam', learning_rate_init=0.01)` 학습 → `n_layers_`, `coefs_`, `intercepts_`로 네트워크 크기·가중치 확인 → 예측 정확도.
- **흐름 ②:** `make_moons(n_samples=300, noise=0.2)` 비선형 데이터 → 80/20 분할 → 은닉층 `(10,10)`·ReLU·Adam MLP 학습 → 테스트 정확도.
- **핵심:** 단층 퍼셉트론으로 불가능한 XOR를 비선형 은닉층을 통해 표현할 수 있다. `coefs_`는 계층 간 가중치 행렬 목록이다.
- **주의:** 작은 XOR 자료는 난수 초기화와 학습 반복에 따라 완전한 학습이 보장되지 않는다.

#### [`ex46.py`](./ex46.py) — Iris 3클래스 MLP, 모델 저장, 경계

- **목적:** Iris 꽃잎 2특성을 이용해 두 은닉층 `(20,10)`의 MLP 분류기를 실습한다.
- **흐름:** Train/Test 분할 → `MLPClassifier(activation='relu', solver='adam', learning_rate_init=0.001, max_iter=1000)` 학습 → 정확도/혼동행렬 → joblib 저장 → 새 입력 예측 → 분류경계.
- **핵심:** 출력층은 클래스 3개에 대응하며 `predict()`는 클래스를, `predict_proba()`는 클래스별 확률을 반환할 수 있다. 훈련 정확도와 검증 정확도를 비교해 일반화 상태를 점검한다.
- **실제 코드 주의:** 표준화 코드가 주석 처리되어 있고, 스케일러 예시에는 테스트 데이터에 `fit`하는 잘못된 흐름이 남아 있다. MLP는 표준화 후 훈련하는 편이 일반적으로 유리하다. 또 예측확률을 설명하는 주석과 달리 출력 코드는 `predict()`를 두 번 호출한다.

#### [`ex.47.py`](./ex.47.py) — Wine 13특성 3클래스 MLP 평가

- **목적:** `load_wine()`의 178개 표본, 13개 특성, 3개 클래스에 MLP를 적용한다.
- **흐름:** `train_test_split(test_size=0.2, stratify=y)` → `StandardScaler` → `MLPClassifier(hidden_layer_sizes=(20,10), activation='relu', max_iter=150)` → 정확도·`classification_report` → 혼동행렬 히트맵.
- **핵심:** 다중클래스 분류에서 각 클래스의 정밀도·재현율·F1과 전체 혼동행렬을 해석한다. 13개 특성의 단위가 다르므로 표준화가 특히 유용하다.
- **실제 코드 오류:** `x_test_scaled = scaler.fit_transform(x_test)`는 **테스트셋에서 평균과 표준편차를 다시 학습**한다. 올바른 코드는 `x_test_scaled = scaler.transform(x_test)`이다. `max_iter=150`은 수렴에 충분하지 않을 수 있다. 파일명은 `ex47.py`가 아닌 정확히 `ex.47.py`이다.

---
## 5. 실전 연습문제 해설 — prac 시리즈

`prac` 파일은 예제(`ex`)에서 다룬 알고리즘을 새로운 데이터에 적용하는 문제 풀이이다. 업로드된 폴더에는 **`prac3.py`는 없고**, `prac1`, `prac2`, `prac4`~`prac11`의 **10개** 파일이 있다.

#### [`prac1.py`](./prac1.py) — Advertising 상관관계 분석·Heatmap

- **문제:** `Advertising.csv`에서 TV/라디오/신문 광고비의 상호관계 및 매출(`sales`)과의 관련성을 파악한다.
- **실제 처리:** 파일 로드 → `tv`, `radio`, `newspaper`, `sales` 선택 → 공분산·상관행렬 출력 → `sales` 기준 상관순위 → 관계를 시각화하는 코드.
- **공부할 개념:** EDA(탐색적 자료 분석), 숫자형 변수의 상관계수, 목적변수와 설명변수의 구분, Heatmap 색깔과 값의 의미.
- **해석:** 광고비와 매출의 상관성이 높아도 광고가 반드시 매출을 인과적으로 증가시킨다는 결론은 아니다. 자료의 변수 단위·숨은 공변량을 살펴봐야 한다.

#### [`prac2.py`](./prac2.py) — TV 시청시간으로 운동시간·종편 시청시간 회귀

- **문제:** 지상파 시청시간을 입력하면 ① 운동시간 ② 종편 시청시간을 예측한다.
- **실제 처리:** 직접 만든 15행 DataFrame → `운동 > 10` 이상치 제거 → 지상파 결측값 평균 대체 → `stats.linregress`로 두 가지 회귀 → 사용자 `input()` → `LinearRegression`과 `smf.ols` 방식도 비교.
- **공부할 개념:** 결측 처리, 이상치 규칙, 동일 데이터에 대한 서로 다른 회귀 API 구현, 모델 기울기·절편·p-value·R² 해석.
- **실행 주의:** 콘솔에서 지상파 시청시간을 직접 입력해야 다음 단계로 진행한다. 이상치 기준(`운동 10시간 초과`)은 문제에서 정의한 규칙이며, 실제 분석에서는 근거를 명시해야 한다.
- **실무 개선:** 평균 대체값은 전체 데이터로 결정하기보다 훈련 데이터에서만 추정하고, 표본이 매우 작을 때는 외삽과 과적합에 주의한다.

#### [`prac4.py`](./prac4.py) — 기온·강수량으로 맥주 소비량 예측

- **문제:** 상파울루 맥주 소비 자료에서 평균기온(`Temperatura Media (C)`)과 강수량(`Precipitacao (mm)`)으로 소비량(`Consumo de cerveja (litros)`) 예측.
- **실제 처리:** 원격 CSV → 필요한 열 선택 → 결측 행 제거·숫자 형식 처리 → 특성/타깃 분리 → Train/Test → `LinearRegression` → 계수·절편·R²/MSE → 새 기온·강수량 조합 예측.
- **공부할 개념:** 다중선형회귀, 문자형 숫자의 변환, 결측값 처리, 회귀계수의 단위와 테스트 평가.
- **주의:** 관측된 소비량에는 날씨 외에도 요일·행사 등 숨은 요인이 작용할 수 있어 해석 시 인과성을 단정하지 않는다.

#### [`prac5.py`](./prac5.py) — UCI Servo 데이터 다항회귀 비교

- **문제:** 서보 제어기 데이터에서 `pgain`, `vgain`으로 응답시간(`class`) 예측.
- **실제 처리:** UCI `servo.data` → 연속값 특성 선택 → Train/Test → `StandardScaler` → `PolynomialFeatures(degree=2)` → 일반 선형회귀와 2차 다항회귀의 R² 비교 → 다항회귀 MSE/RMSE → 새 증폭 설정 예측.
- **공부할 개념:** 수치형 전처리, 2차 상호작용항 생성, 과적합 위험, 회귀 평가, 새로운 입력에도 **같은 scaler/poly 적용**.
- **주의:** 새 표본에 `scaler.fit_transform()`을 새로 적용하면 안 된다. 원본은 `scaler.transform(new_df)`, `quad.transform(new_scaled)`의 순서를 올바르게 사용한다.

#### [`prac6.py`](./prac6.py) — 소득수준으로 외식 여부 로지스틱 회귀

- **문제:** 소득수준이 주말 외식 여부(0/1)와 유의하게 관련되는지 검정하고 새 입력으로 분류한다.
- **실제 처리:** 요일·소득수준·외식여부 데이터 생성 → `smf.logit(...)` → 소득 계수 p-value 판정 → `w`, `b`로 시그모이드 확률 직접 계산 → 혼동행렬/정확도 → 소득·외식 확률 곡선 → 사용자 소득 입력 예측.
- **공부할 개념:** 로그오즈와 시그모이드, 회귀계수 부호, 오즈비(`exp(coef)`), 유의성 검정, 확률→라벨 변환.
- **주의:** 입력은 양의 정수를 기대하므로 `input()`에 문자가 들어오면 `ValueError`가 발생할 수 있다. `p-value < 0.05`는 연관성에 대한 증거이며 원인·결과를 확정하지 않는다.

#### [`prac7.py`](./prac7.py) — 게임·TV 시청시간으로 안경 착용 여부 분류

- **문제:** `bodycheck.csv`에서 `게임`, `TV시청`을 입력으로 `안경유무`를 분류하고 새 입력을 받아 예측한다.
- **실제 처리:** 원격 CSV → `train_test_split` → `LogisticRegression` → 확률·혼동행렬·정확도·`classification_report` → 게임/TV 입력 → DataFrame으로 예측 및 클래스별 확률 출력.
- **공부할 개념:** 이진 분류, 혼동행렬, API 입력 특성 순서 유지, `predict_proba`와 `predict` 차이.
- **주의:** 두 사용시간만으로 실제 안경 필요 여부를 판단할 수 없으며, 교육용 분류 데이터 실습이다. 정확도를 평가할 때 클래스 비율도 확인한다.

#### [`prac8.py`](./prac8.py) — 광고 클릭률 예측과 ROC-AUC

- **문제:** 웹사이트 이용시간, 나이, 지역소득, 인터넷 사용량으로 `Clicked on Ad`(광고 클릭 여부) 예측.
- **실제 처리:** `advertisement.csv` → 4개 특성과 타깃 선택 → Train/Test → `StandardScaler` → 로지스틱 회귀 → 정밀도·재현율·정확도·분류 보고서 → ROC curve 및 AUC → 새 고객 입력 예측.
- **공부할 개념:** 입력값 단위 차이로 인한 표준화, 이진 확률, 불균형 분류 지표, ROC-AUC의 해석.
- **핵심 코드:** 새 자료는 `sc.transform(newdf)`를 거쳐 **훈련할 때와 같은 특성 공간**으로 들어가야 한다.
- **주의:** ROC-AUC는 확률(또는 순위 점수)로 계산해야 하며, 단순 0/1 예측값만 전달하면 정보가 줄어든다.

#### [`prac9.py`](./prac9.py) — 와인 품질 점수 랜덤포레스트 다중분류

- **문제:** `winequality-red.csv`의 11개 물리·화학 특성으로 관능 품질 점수(`quality`) 분류.
- **실제 처리:** 로컬 CSV → 품질별 분포 확인 → `quality` 제외 11개 변수 분리 → Train/Test → `RandomForestClassifier` → 테스트 정확도·혼동행렬·classification_report → 5겹 교차검증 → 변수 중요도 정렬/시각화 → 샘플 1건 예측.
- **공부할 개념:** 다중클래스 분류, 품질 레이블의 불균형, 교차검증, 포레스트 특성 중요도.
- **주의:** `quality`는 순서가 있는 점수지만 이 코드는 **각 점수를 서로 다른 분류 클래스**로 취급한다. 정확한 점수 오차 자체를 평가하려면 별도 회귀·순서형 모델과 비교해 볼 수 있다.

#### [`prac10.py`](./prac10.py) — 유리 종류 식별 XGBoost

- **문제:** `glass.csv`의 굴절률(`RI`)과 `Na`, `Mg`, `Al`, `Si`, `K`, `Ca`, `Ba`, `Fe` 등으로 유리 종류 `Type` 예측.
- **실제 처리:** 외부 CSV → `Type` 분포 → `LabelEncoder`로 불연속 타입 번호를 연속 인덱스로 변환 → 층화 Train/Test → `XGBClassifier(objective='multi:softprob', eval_metric='mlogloss')` → 분류 보고서·혼동행렬 → 중요도 → 새 유리 데이터 분류 후 원래 Type으로 역변환.
- **공부할 개념:** 다중클래스 부스팅 분류, `LabelEncoder.fit_transform(y)`, `inverse_transform`의 역할, 모델 하이퍼파라미터.
- **주의:** 문제 설명의 '7종'과 실제 데이터에 나타나는 클래스 개수는 다를 수 있으므로 `unique()`로 확인한다. `LabelEncoder`는 **타깃 클래스**에 쓰며 일반적인 명목형 입력에는 `OneHotEncoder` 등의 전처리가 더 적합할 수 있다.

#### [`prac11.py`](./prac11.py) — 독버섯/식용버섯 GaussianNB 분류

- **문제:** `mushrooms.csv`에서 `class`(`p`: poisonous, `e`: edible) 분류.
- **실제 처리:** 로컬 CSV → 클래스를 제외한 22개 범주형 변수 → `pd.get_dummies(..., dtype=int)`로 원-핫 인코딩 → 냄새(`odor_`), 포자문양색(`spore-print-color_`) 등 접두어 기반 변수 선택 → Train/Test → `GaussianNB` → 정확도 → 테스트 2건 예측확률과 실제값 비교.
- **공부할 개념:** 범주형 변수를 수치 행렬로 바꾸는 원-핫 인코딩, 입력 특성 선택, 이진 분류, 나이브 베이즈.
- **방법론 한계:** **GaussianNB는 연속형 가우시안 특성을 가정**하므로 원-핫 이진 특성에는 `BernoulliNB` 또는 다른 모델 비교가 자연스럽다. `get_dummies`를 분할 전에 처리하는 예제지만 실제 운영에서는 훈련 시 범주 목록을 학습·유지해야 한다.
- **안전:** 이 예측 결과를 실제 야생 버섯의 식용 여부를 판단하는 데 사용해서는 안 된다.

---

## 6. Flask 미니 프로젝트 — quiz1

### 6.1 구성

```text
quiz1/
├── app.py                 # DB 조회 + 선형회귀 + Flask 라우팅/API
└── templates/
    └── index.html         # 근무년수 입력/표/예측 결과 표시
```

**목표:** MariaDB/MySQL 직원 데이터에서 근무년수(`근무년수`)와 연봉(`연봉`)의 관계를 학습해 웹에서 예상 연봉을 조회한다. 또한 직급별 평균 연봉을 HTML 표로 보여준다.

#### [`quiz1/app.py`](./quiz1/app.py) — DB → DataFrame → LinearRegression → JSON API

1. `pymysql.connect(**config)`로 로컬 DB `test`에 접속한다.
2. `jikwon` 테이블의 `jikwonname`, `jikwonjik`, 입사일·급여를 조회하여 컬럼명을 `이름`, `직급`, `근무년수`, `연봉`으로 지정한 DataFrame을 만든다.
3. `x = df[['근무년수']].values`, `y = df['연봉'].values`에 `LinearRegression().fit(x,y)`를 적용한다.
4. `r2_score(y, model.predict(x))`를 계산하고, `df.groupby('직급')['연봉'].mean()`으로 직급별 평균 연봉을 만든다.
5. `GET /`에서 템플릿 렌더링에 `jik_list`를 전달한다.
6. `GET /api/predict?year=5`가 입력값을 검증하고 예측 연봉, R², 회귀식을 JSON으로 반환한다.

**핵심 메서드·API:**

| 코드 | 역할 |
|---|---|
| `pymysql.connect` | MariaDB/MySQL 연결 |
| `cursor.execute(sql)` + `fetchall()` | SQL 조회 결과 수집 |
| `pd.DataFrame(..., columns=...)` | DB 튜플을 분석하기 좋은 표로 변환 |
| `df.groupby('직급')['연봉'].mean()` | 직급별 평균 연봉 산출 |
| `@app.get('/')` | 웹 첫 페이지 라우팅 |
| `render_template('index.html', jik_list=...)` | Jinja 템플릿 전달 |
| `@app.get('/api/predict')` | GET 기반 JSON 예측 API |
| `request.args.get('year')` | URL 쿼리 인자 읽기 |
| `jsonify({...})` | Python 딕셔너리를 JSON 응답으로 변환 |

**응답 형태 예시(수치는 실제 실행 결과에 따라 달라짐):**

```json
{
  "ok": true,
  "year": 5,
  "pay": 0,
  "r2": "0.00%",
  "formula": "pay = (학습된 계수) * years + (학습된 절편)"
}
```

위의 `pay`, `r2`는 **API 구조를 설명하기 위한 자리표시 예시**이지 실제로 계산된 결과가 아니다.

#### [`quiz1/templates/index.html`](./quiz1/templates/index.html) — 사용자 입력·표·비동기 요청

- `<input id="year">`에 근무년수를 입력하고 버튼을 클릭한다.
- JavaScript의 `addEventListener('click', async () => {...})`로 버튼 이벤트를 등록한다.
- `URLSearchParams({year})`로 쿼리스트링을 안전하게 구성하고, `fetch('/api/predict?...')`로 서버에 비동기 GET 요청을 보낸다.
- `await res.json()`으로 JSON을 파싱하고 `res.ok` 및 `data.ok`를 확인해 성공/오류 메시지를 표시한다.
- 템플릿의 `{% for row in jik_list %}` 반복문이 직원 직급별 평균 연봉 테이블을 구성한다.

**요청 → 응답 흐름:**

```text
사용자 근무년수 입력
       ↓
브라우저 JavaScript (fetch)
       ↓ GET /api/predict?year=5
Flask 라우트 (입력 검증)
       ↓
LinearRegression.predict([[5]])
       ↓
jsonify()로 예측값/회귀식 반환
       ↓
브라우저 DOM 업데이트
```

### 6.2 이 프로젝트에서 확인해야 할 사항

- **[보안 중요] `app.py`에 DB 계정과 비밀번호가 하드코딩되어 있다.** GitHub 공개 전에 원본 파일의 자격증명을 제거하고, 해당 비밀번호를 실제 사용했다면 교체해야 한다. README에서는 해당 값을 재기재하지 않는다.
- 현재 코드는 **모듈 import 시 DB에 즉시 접속**한다. DB가 꺼져 있거나 `test.jikwon`이 없으면 Flask 서버가 뜨지 않는다. 앱 시작 시 예외처리·연결 상태 확인이 필요하다.
- `year(now()) - year(jikwonibsail)`은 대략적인 연도 차이로, **정확한 만 근속연수** 계산과 차이가 날 수 있다. 필요한 경우 `TIMESTAMPDIFF(YEAR, jikwonibsail, CURDATE())` 같은 방식을 고려한다.
- `r2`는 학습에 사용한 자료로 계산된 **학습 R²**다. 별도 테스트 데이터의 검증 점수로 오해하면 안 된다.
- 선형회귀로 계산한 예측 연봉은 통계적 추정이며 실제 지급액, 직급, 연령, 직무 등 다양한 요인을 반영하지 못한다.
- `app.run(debug=True)`는 개발용 옵션으로, 외부에 공개 운영할 때는 비활성화해야 한다.
- `index.html`은 `innerHTML`로 메시지를 구성한다. 모델/API 응답에 사용자 제어 문자열이 들어가는 구조로 확장할 경우 XSS를 방지하기 위해 문자열 검증과 `textContent` 사용 등을 고려한다.

### 6.3 DB 비밀번호를 코드에서 분리하는 예시

```python
# app.py 예시: python-dotenv를 선택적으로 설치해 사용할 수 있음
import os
from dotenv import load_dotenv
load_dotenv()

config = {
    'host': os.getenv('DB_HOST', '127.0.0.1'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME', 'test'),
    'port': int(os.getenv('DB_PORT', '3306')),
    'charset': 'utf8mb4'
}
```

```dotenv
# .env.example — 값은 예시 이름만 두고 실제 비밀번호는 넣지 않기
DB_HOST=127.0.0.1
DB_USER=your_db_user
DB_PASSWORD=replace_me
DB_NAME=test
DB_PORT=3306
```

```gitignore
# 공개 저장소에서 실제 자격증명 보호
.env
.venv/
__pycache__/
*.pyc
```

**주의:** `.gitignore`는 *이후 추적되지 않는 파일*을 막는 용도다. 과거 커밋에 비밀번호가 포함됐던 경우 기록에 남아 있을 수 있으므로, 저장소 공개 전에 Git 히스토리도 확인하고 사용 중인 비밀번호는 변경한다.

---

## 7. 데이터 파일과 실행 의존성

| 파일 / 데이터 | 연결된 코드 | 성격 및 주의점 |
|---|---|---|
| `서울특별시_관광지입장정보_2011_2016.json` | `ex3` | 관광지별 월별 외국인 입장객 자료 |
| `중국인방문객.json` / `일본인방문객.json` / `미국인방문객.json` | `ex3` | 국가별 월 방문객 수; 모두 같은 월 키로 병합 |
| `bush.jpeg` | `ex37` | 얼굴 이미지 분류 입력; 이미지 크기·전처리 일관성 중요 |
| `winequality-red.csv` | `prac9` | 레드와인 물리·화학 성분/품질 분류 자료 |
| `mushrooms.csv` | `prac11` | 범주형 버섯 특성·독성 레이블 자료 |
| `train.csv` (약 **59.4MB**, 10진 MB 기준) | `ex32` | Santander 고객 예측 훈련 데이터; 대용량이라 별도 관리 검토 |
| `ex20model.sav` | `ex20` 등 여러 코드 | 실행할 때 덮어쓸 수 있는 직렬화 모델 |
| `carseat.pickle` | `ex11` | Statsmodels 모델 저장/불러오기 파일 |
| GitHub `raw.githubusercontent.com/pykwon/...`의 CSV | 여러 파일 | 인터넷 필요, 원격 경로 변경 시 실행 실패 가능 |
| `statsmodels`의 `mtcars`, scikit-learn의 Iris/Wine/Cancer/LFW/California housing | `ex9`, `ex13` 등 | 내장 또는 다운로드되는 실습용 자료 |
| `test.jikwon` 테이블 | `quiz1` | 개인 PC의 MariaDB/MySQL 실습 DB. ZIP에는 DB 스키마·테이블 데이터가 포함돼 있지 않음 |

**라이브러리별 대표 활용:**

- **NumPy:** 배열, 선형대수, 표준편차·공분산, 수치연산.
- **Pandas:** CSV/JSON/SQL 결과 처리, 결측값, 병합, 집계, 데이터프레임.
- **SciPy:** 상관검정, `linregress`, Shapiro-Wilk.
- **Statsmodels:** OLS/Logit/GLM, 회귀계수 추론과 진단.
- **scikit-learn:** 데이터 분할, 전처리, 모델, 교차검증, 성능평가.
- **XGBoost / LightGBM:** 경사 부스팅 기반 분류.
- **Matplotlib / Seaborn:** 산점도, 회귀선, 혼동행렬·중요도 시각화.
- **Flask / PyMySQL:** 데이터 분석 모델의 웹 API 및 DB 연동.

---
## 8. 실제 코드 점검·개선 포인트

아래는 업로드된 소스에서 확인되는 **수정 권장 사항**이다. 원본을 삭제하거나 변경했다는 뜻이 아니며, GitHub에서 코드를 실행하려는 사람에게 현재 상태를 투명하게 알리기 위한 안내다.

### 8.1 우선 수정할 오류·호환성 이슈

| 관련 파일 | 실제 확인한 사항 | 권장 수정 |
|---|---|---|
| `ex2.py` | `np.zeros_like(..., dtype=np.bool)` | `dtype=bool` 또는 `np.bool_` 사용 |
| `ex5.py` | 길이가 다른 배열 연산, 존재하지 않는 `LinearRegression(n_samples=...)`, 잘못된 `np.array`, 누락된 OLS 공식 등 | 데이터 생성·모델 학습 구문부터 재작성 필요 |
| `ex10.py` | RESET 진단 후 조건문에서 Shapiro의 `pv`를 사용 | `reset_result.pvalue`를 참조 |
| `ex12.py` | 두 번째 모델 평가에 앞선 실험의 `x_scaled` 사용 | `x_scaled2`와 같은 데이터 세트로 평가 |
| `ex15.py` | 2차 모델 출력에서 첫 번째 `ypred`로 R² 계산 | `r2_score(y, ypred2)` |
| `ex16.py` | 2·3차 그래프 라벨에 모두 `model_r2` 사용 | `q_r2`, `c_r2` 각각 사용 |
| `ex20.py`, `ex24.py`, `ex28.py`, `ex31.py`, `ex35.py`, `ex41.py`, `ex44.py`, `ex46.py` | 같은 분류경계 함수에 `x2` 축 최소/최대가 `X[:,0]`로 지정됨; 테스트 강조 색상 `c=[]` | `X[:,1]` 축 참조, `facecolors='none'` 활용 |
| `ex22.py` | `linspace(min, min, 100)`으로 격자 생성 | `linspace(min, max, 100)`으로 수정 |
| `ex25.py` | `scoring='scoring'` | `scoring='accuracy'` |
| `ex27.py` | `df.imsi['Sex']` 오타 | `df_imsi['Sex']`로 수정 |
| `ex30.py`, `ex31.py` | `n_estimator=200` 오타 | `n_estimators=200` |
| `ex.47.py` | 테스트 집합에 `scaler.fit_transform()` | 테스트는 `scaler.transform()` |
| `ex20.py`, `ex24.py`, `ex28.py`, `ex31.py`, `ex35.py`, `ex41.py`, `ex44.py`, `ex46.py` | 모델 직렬화 파일 이름을 모두 `ex20model.sav`로 사용 | `logistic_iris.sav`, `tree_iris.sav` 등 구분 |
| `quiz1/app.py` | DB 자격증명 문자열이 코드에 들어 있음 | `.env` 환경변수 분리, 실제 비밀번호 교체, 커밋 이력 점검 |

**공통 코드 수정 예시 1 — 올바른 표준화**

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # 훈련 데이터만 fit
X_test_scaled = scaler.transform(X_test)        # 테스트는 transform만
```

**공통 코드 수정 예시 2 — 2차원 결정경계**

```python
import numpy as np
import matplotlib.pyplot as plt

x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(
    np.arange(x1_min, x1_max, 0.02),
    np.arange(x2_min, x2_max, 0.02)
)
grid = np.c_[xx.ravel(), yy.ravel()]
Z = model.predict(grid).reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.35)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k')
plt.show()
```

> 위 `X`는 모델에 실제로 학습시킨 것과 **동일한 전처리/좌표계의 입력**이어야 한다. 표준화한 모델에 원본 좌표를 보내면 잘못된 그림이 나온다.

**공통 코드 수정 예시 3 — 검증으로 튜닝하고 테스트는 마지막에 사용**

```python
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
search = GridSearchCV(
    estimator=pipe,
    param_grid={'logisticregression__C': [0.1, 1.0, 10.0]},
    cv=cv,
    scoring='accuracy'
)
search.fit(X_train, y_train)
print('검증 최고 설정:', search.best_params_)
print('최종 테스트 정확도:', accuracy_score(y_test, search.predict(X_test)))
```

### 8.2 머신러닝 해석에서 자주 헷갈리는 점

1. **훈련 정확도 ≠ 테스트 정확도.** `ex21`, `ex36`, `ex40` 등에는 학습한 자료에서 성능을 구하는 구간이 있다. 연습 목적으로는 가능하지만 포트폴리오 성과 지표로 쓰려면 분리된 평가가 필요하다.
2. **전처리는 테스트로 학습하지 않는다.** 표준화뿐 아니라 결측치 평균·PCA·변수 선택 등 `fit`이 필요한 단계는 훈련 전용이다.
3. **정확도만으로 모델을 비교하지 않는다.** 클래스 비율과 오분류 비용에 따라 Recall·Precision·F1·AUC를 함께 본다.
4. **회귀 R²와 분류 정확도는 다른 지표다.** `LinearRegression.score()`는 R²지만 `Classifier.score()`는 보통 정확도다.
5. **다중클래스 확률과 0/1 임계값을 혼동하지 않는다.** `predict_proba`는 클래스별 확률행렬로, 열 순서는 `model.classes_`에 따른다.
6. **트리 중요도는 인과 설명이 아니다.** 상관된 변수들의 중요도가 서로 분산되는 등의 한계가 있다.
7. **높은 p-value는 가정 충족의 증명이 아니다.** 표본 수·검정력과 함께 그래프·도메인 지식을 확인한다.
8. **README의 성과 수치는 실제 실행 후 기록한다.** 본 문서에는 정확도·R²를 실행으로 검증하지 않은 채 '합격률 99%' 등으로 쓰지 않았다.

### 8.3 GitHub 공개 전 체크리스트

- [ ] `quiz1/app.py`에서 DB 사용자명·비밀번호 제거, 유출된 적 있는 실제 비밀번호 변경.
- [ ] `.env`, API Key, 로컬 경로, 개인정보가 다른 코드에 없는지 확인.
- [ ] 소스 코드의 과거 커밋에도 자격증명이 남지 않았는지 확인.
- [ ] `train.csv`처럼 큰 자료는 업로드 제한·라이선스·저작권 확인 후 저장 여부 결정. 필요하면 다운로드 경로 설명 또는 Git LFS 사용.
- [ ] `.sav`·`.pickle` 산출물의 공개 필요성을 점검하고 불필요한 모델 파일은 버전관리에서 제외.
- [ ] 실행 순서가 중요한 파일은 의존 라이브러리, 원격 자료, DB 준비 방법을 명시.
- [ ] 공통 파일명을 사용한 모델 산출물 덮어쓰기 문제를 정리.
- [ ] `pro12ml` 폴더에 파일 설명 README를 넣고, 저장소 상위 README에서 링크.

---

## 9. 복습 순서 및 포트폴리오 활용

### 9.1 추천 복습 순서

| 순서 | 파일 | 확인 질문 |
|---|---|---|
| 1 | `ex1`, `ex2`, `prac1` | 공분산과 상관계수의 차이? 상관관계와 인과관계가 다른 이유? |
| 2 | `ex4`, `ex7`, `ex9`, `ex10`, `ex11` | OLS 계수·잔차·R²는 무엇인가? 회귀 가정을 왜 점검하나? |
| 3 | `ex12`, `ex15`, `prac5` | 스케일링, 다항 특성, 과적합이 예측에 미치는 영향? |
| 4 | `ex17`, `ex20`, `ex21`, `prac8` | 시그모이드, 혼동행렬, ROC-AUC를 언제 사용하는가? |
| 5 | `ex22`, `ex25`, `ex26`, `ex28`, `ex30` | 트리·앙상블, 교차검증, 튜닝은 무엇이 다른가? |
| 6 | `ex33`, `ex34`, `ex36`, `ex37` | SVM 마진·커널·PCA의 목적은? |
| 7 | `ex38`, `ex39`, `ex41`, `ex42` | 확률 기반 분류와 거리 기반 분류의 차이? |
| 8 | `ex43`, `ex44`, `ex45`, `ex46`, `ex.47` | 퍼셉트론과 MLP의 차이? 왜 XOR에 은닉층이 필요한가? |
| 9 | `quiz1/app.py`, `quiz1/templates/index.html` | 모델을 API로 서비스할 때 DB, 추론, 입력 검증을 어떻게 분리하나? |

### 9.2 취업 포트폴리오용으로 강조할 수 있는 학습 역량

- **통계적 문제해결:** 데이터 시각화와 상관관계 분석, 회귀계수의 해석, 잔차 진단.
- **모델 설계·비교:** 분류·회귀 문제 구분, 트리·앙상블·신경망 등 다양한 모델의 장단점 비교.
- **평가 신뢰성:** Train/Test, 교차검증, GridSearchCV, Precision/Recall/ROC-AUC.
- **데이터 처리:** 결측값 처리, 범주형 인코딩, 표준화, 중요도 분석.
- **활용·서비스화:** SQL 데이터 읽기 → Pandas 분석 → scikit-learn 학습 → Flask API 제공 → 웹 클라이언트 표시.

**포트폴리오 설명 문구 예시**

> Python 기반 통계·머신러닝 학습 프로젝트로, 회귀·분류 모델의 원리와 성능평가를 다양한 공개 데이터셋에 적용했습니다. scikit-learn의 데이터 분할·전처리·교차검증과 Statsmodels의 회귀 분석을 실습하고, Flask·MariaDB를 연결한 연봉 예측 웹페이지를 구현했습니다. 일부 교육용 코드에 대해서는 오류·데이터 누수·보안 개선점을 별도로 문서화했습니다.

### 9.3 상위 GitHub 저장소에 연결하는 방법

이 파일은 다음 위치에 넣는 것을 권장한다.

```text
works/
├── README.md
└── projects/
    ├── pro1/
    ├── ...
    ├── pro11anal2/
    ├── pro12ml/
    │   ├── READMEpro12.md
    │   ├── ex1.py
    │   └── ...
    └── pro13/  # 추가 예정
```

상위 README에 아래처럼 한 줄 링크를 추가하면 된다.

```markdown
| pro12 | [머신러닝·통계·예측모델 학습](./projects/pro12ml/READMEpro12.md) | 회귀/분류, 평가, 앙상블, MLP, Flask |
```

> GitHub는 각 폴더 안에 `README.md` 파일이 있을 때 자동으로 내용을 표시한다. 이번 파일명은 이전 pro1~11과의 규칙을 맞춰 `READMEpro12.md`로 작성했으므로 **사용자가 클릭해야 열리는 설명 파일**이다. 폴더 첫 화면에 자동 표시하려면 동일 내용을 `README.md`로 저장하면 된다.

---

**정리:** 이 README는 현재 ZIP에 포함된 58개의 Python 소스와 1개 HTML 템플릿의 역할 및 핵심 개념을 코드와 연결한 자료다. 모델 성능 수치는 별도 실행검증을 거치지 않았으며, 안전하게 공개하려면 특히 `quiz1/app.py`의 DB 자격증명과 직렬화 모델·대용량 데이터 관리를 우선 점검해야 한다.
