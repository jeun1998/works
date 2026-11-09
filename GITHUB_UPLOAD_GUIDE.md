# pro1–pro11 GitHub 업로드 가이드 (Windows + VS Code)

## 0. 준비: 올릴 파일만 모으기

`projects.zip`을 압축 해제하고, 새 작업 폴더(예: `python-web-data-study`)에 **`pro1`, `pro2`, `pro3db`, `pro4web`, `pro5web2`, `pro6web3basic`, `pro7quiz`, `pro8js`, `pro9flask`, `pro10anal1`, `pro11anal2`** 11개 폴더를 복사합니다.

이 문서와 함께 제공된 `README.md`, `CODE_SUMMARY.md`, `.gitignore`, `.env.example`도 같은 최상위 폴더에 복사합니다. 원본 압축에 존재하는 **빈 `.gitignore` 폴더**는 삭제하세요. Git이 사용하는 것은 같은 이름의 **텍스트 파일 `.gitignore`**입니다.

기존 `team`, `team1`, `pro12ml` 등은 이번 저장소에 넣지 않는 것을 추천합니다.

## 1. 보안 점검 (매우 중요)

- `pro3db/.env`와 `pro5web2/cgi-bin/.env`는 **업로드하지 않습니다.**
- `pro3db/dbconnect.json`은 접속정보 파일이므로 업로드하지 않습니다. 학습용 예시가 필요하면 비밀값을 제거한 `.example` 파일을 별도로 만듭니다.
- `pro3db/db2maria.py`, `pro9flask/fpro17/app.py`, `pro10anal1/pandas14.py`, `pro10anal1/pandas17.py` 등에는 소스 내부의 DB 접속 설정이 있습니다. 또한 일부 Flask `app.py`, `db.py`도 환경변수의 기본값·고정 secret key를 사용합니다. **하드코딩된 비밀번호가 실제 접속 가능한 값이라면 코드를 수정한 뒤에 커밋하세요.**
- `.gitignore`는 비밀값이 **코드 내부에 직접 작성된 경우** 보호하지 못합니다. 비밀값은 환경변수(`os.getenv(...)`)로 이전하고 `.env.example`에 키 이름만 남기는 방법을 권장합니다.
- `__pycache__`, `*.pyc`, `.git`, 로컬 DB 파일을 제외합니다.
- 공개 범위를 정하기 전에는 GitHub 저장소를 **Private**으로 생성할 수도 있습니다. 단, Private 저장소라도 민감한 비밀번호를 올리지 않는 것이 원칙입니다.

## 2. GitHub 웹에서 빈 저장소 생성

1. GitHub 로그인 → 우측 상단 `+` → `New repository`.
2. 저장소 이름 예: `python-web-data-study`.
3. `Public` 또는 `Private` 선택.
4. **Add a README file / Add .gitignore / Choose a license를 선택하지 않고** 빈 저장소 생성. 로컬에서 파일을 넣을 것이므로 중복 초기화를 피합니다.
5. GitHub에 나오는 HTTPS 저장소 주소(`https://github.com/YOUR_ID/python-web-data-study.git`)를 복사합니다.

## 3. VS Code 터미널에서 업로드

새 폴더를 VS Code에서 연 다음 Terminal → New Terminal. 다음 명령을 **프로젝트 최상위 폴더**에서 차례로 실행합니다.

```bash
git --version
git init -b main
git status
# .gitignore 적용 후 추적 대상 검사
git add .
git status
# 민감한 파일이 표시되면 절대 다음 단계로 넘어가지 말 것!
git commit -m "Add Python, web and data analysis exercises"
git remote add origin https://github.com/YOUR_ID/python-web-data-study.git
git push -u origin main
```

`YOUR_ID`를 본인의 GitHub 사용자 이름으로 교체합니다. 처음 푸시할 때 브라우저 인증이 뜰 수 있습니다. Git에 작성자 설정이 없어서 commit이 실패할 경우:

```bash
git config --global user.name "Your GitHub Name"
git config --global user.email "you@example.com"
```

`git init -b main`을 지원하지 않는 구버전 Git에서는 `git init` 다음 `git branch -M main`을 사용합니다.

### 업로드 여부 확인

```bash
git status
```

`nothing to commit, working tree clean`으로 출력되고 GitHub 저장소의 파일 목록에서 `README.md`와 `pro1`~`pro11` 폴더가 확인되면 완료입니다.

## 4. 다음에 코드를 수정했다면

```bash
git add .
git status
git commit -m "Update Flask and Pandas exercises"
git push
```

## 5. GitHub Desktop을 사용한다면

GitHub Desktop 설치 → `File` → `Add local repository` (새 폴더가 Git 저장소가 아니라면 `Create a Repository`) → 로컬 폴더 선택 → 커밋 → `Publish repository`. 공개/비공개를 확인한 뒤 업로드합니다. 터미널 명령이 익숙하지 않을 때 적합합니다.

## 6. 자주 하는 실수

- **압축파일 자체만 올리기:** GitHub에서 개별 소스 탐색이 어려워집니다. 압축을 풀고 코드 파일을 폴더별로 올리세요.
- **`.gitignore`가 폴더로 존재:** 실제 이름이 `.gitignore/`인 디렉터리는 설정 파일이 아닙니다. 디렉터리를 삭제하고 `.gitignore` 파일을 두세요.
- **민감정보 커밋:** 나중에 파일만 삭제해도 Git 기록에 남을 수 있습니다. 커밋 전 확인하고 실제 비밀번호가 노출됐다면 비밀번호 교체가 필요합니다.
- **DB 프로그램을 그대로 실행하려고 하기:** 실습 DB/테이블이 없다면 오류가 날 수 있습니다. 학습 코드인 점을 README에 명확히 적는 편이 좋습니다.
- **모든 코드가 하나의 앱이라고 소개:** 실제로는 독립적인 파일별 학습 예제입니다.

[GitHub 공식 문서: 로컬 코드 업로드](https://docs.github.com/ko/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
