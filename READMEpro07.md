# pro7quiz — HTML/CSS 다중 페이지 홈페이지 실습

> **학습 목표:** 여러 HTML 문서를 하나의 홈페이지로 구성하고 메뉴 이동·스타일·이미지 배치를 구현한다.

## 1. 화면 구성과 개념

```text
main.html (기준 화면)
├─ 네비게이션: 홈 / 메뉴1 / 메뉴2
└─ 본문 iframe
   ├─ home.html  → 초기 페이지
   ├─ menu1.html → 첫 번째 메뉴 내용
   └─ menu2.html → 두 번째 메뉴 내용
      (공통 스타일: test.css)
```

### ① 페이지 분리와 링크
- 메인 화면의 메뉴 클릭에 따라 다른 HTML이 본문 영역에 표시되도록 작성했다.
- `iframe`과 링크의 `target`을 이용하면 전체 페이지를 새로 여는 대신 프레임 콘텐츠를 바꿀 수 있다.
- 이 방식은 학습용으로 유용하지만 실제 서비스에서는 라우팅, 접근성, 브라우저 기록 등을 고려해 구현 방식을 선택한다.

### ② CSS 레이아웃
- `margin`: 요소 바깥 여백, `padding`: 내부 여백.
- `display: flex`는 한 축을 중심으로 요소를 정렬하며 `justify-content`와 `align-items`로 배치를 제어한다.
- `display: grid`는 행과 열을 함께 설계할 때 활용한다.
- `box-sizing: border-box`는 지정한 너비에 테두리·패딩을 포함해 레이아웃 계산을 쉽게 한다.
- `width`, `max-width`, `gap`, `object-fit` 등은 크기와 이미지 배치에 유용하다.

```css
/* 학습용 레이아웃 핵심 패턴 */
.nav { display: flex; gap: 12px; }
.content { width: 100%; min-height: 400px; }
img { max-width: 100%; height: auto; }
```

## 2. 실제 코드와 개념 연결

| 파일 | 구현 내용 |
|---|---|
| `main.html` | 메뉴·본문 프레임이 포함된 홈페이지 진입점 |
| `home.html` | 최초 보이는 메인 콘텐츠와 이미지 |
| `menu1.html` | 첫 번째 메뉴 콘텐츠 및 표 |
| `menu2.html` | 두 번째 메뉴 콘텐츠 |
| `test.css` | 전체 페이지의 배경, 간격, 메뉴, 정렬 등 스타일 정의 |

## 3. 실행 및 점검

1. `projects/pro7quiz/main.html`을 브라우저에서 연다.
2. '홈페이지', '메뉴1', '메뉴2' 이동이 예상대로 동작하는지 확인한다.
3. 이미지와 CSS가 로드되는지 개발자 도구(`F12`)의 Network/Console에서 확인한다.
4. 창의 너비를 줄여 메뉴와 본문이 겹치지 않는지 확인한다.

## 4. 다음 단계로 확장한다면

- 시맨틱 HTML(`<nav>`, `<main>`)과 키보드 접근성 보강.
- iframe 의존도를 줄이고 JavaScript 라우팅 또는 백엔드 라우팅으로 개선.
- 반응형 미디어 쿼리(`@media`)와 모바일 화면 지원.
- 공통 CSS를 유지하며 여러 페이지의 스타일 일관성 확보.

[⬅ 프로젝트 목록으로](../README.md)
