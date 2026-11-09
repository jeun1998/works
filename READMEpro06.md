# pro6web3basic — HTML·CSS와 웹 문서 구조

> **학습 목표:** HTML로 문서의 의미를 구조화하고 CSS로 표현과 레이아웃을 지정한다.

## 1. 핵심 이론

### ① HTML의 역할
- `<!DOCTYPE html>`은 HTML5 문서임을 선언한다.
- `<html>`, `<head>`, `<body>`로 문서를 구성한다.
- 제목(`<h1>`~`<h6>`), 문단(`<p>`), 목록(`<ul>`, `<ol>`, `<li>`)은 문서 의미를 표현한다.
- `<a href="...">`는 링크를, `<img src="..." alt="...">`는 이미지를 표현한다.
- `<table>`은 표 형식 데이터에 사용하고, 입력 폼에는 `<form>`, `<input>`, `<select>`, `<textarea>` 등을 쓴다.
- `id`는 문서에서 고유한 식별자, `class`는 여러 요소에 재사용할 수 있는 분류 속성이다.

### ② 상대경로·절대경로
- `./`은 현재 폴더, `../`은 상위 폴더를 가리킨다.
- 예: `kbs/sbs/aa.html`에서 상위 폴더의 파일을 연결하려면 경로 계산이 필요하다.
- GitHub Pages 또는 서버에서 파일을 표시할 때 **대소문자·파일명·경로**가 일치해야 한다.

### ③ CSS 기본 문법

```css
/* 선택자 { 속성: 값; } */
.notice {
  color: #1d4ed8;
  padding: 12px;
  border: 1px solid #ddd;
}
```

- **선택자:** 태그(`p`), 클래스(`.box`), ID(`#main`), 가상 클래스(`a:hover`, `input:focus`) 등.
- **우선순위:** 중요 선언 여부, 출처, 선택자 특이성, 선언 순서에 따라 적용 결과가 달라진다.
- **박스 모델:** `content + padding + border + margin`. `box-sizing: border-box`를 이해한다.
- CSS 적용 방법은 인라인 스타일, 내부 `<style>`, 외부 `.css` 연결이 있다. 재사용에는 외부 파일이 유리하다.

## 2. 실제 코드와 개념 연결

| 파일 | 주요 학습 내용 |
|---|---|
| `web1.html` | 텍스트 태그, 목록 등 기본 문서 구조 |
| `web2.html` | 하이퍼링크, 이미지, iframe과 경로 |
| `web3.html` | 표 작성과 HTML 폼 구성 |
| `web4.html` | CSS 내부/외부 스타일 연결 및 화면 꾸미기 |
| `css/pro6.css` | 여러 페이지에서 공통 CSS 사용 |
| `kbs/sbs/aa.html`, `mbc/bb.html` | 하위 폴더를 오가는 상대경로 실습 |

## 3. 확인하는 방법

```text
projects/pro6web3basic/web1.html
projects/pro6web3basic/web4.html
```

정적 파일이므로 브라우저에서 직접 열 수 있다. 다만 일부 링크·이미지는 폴더 구조에 의존하므로 폴더를 이동할 때 참조 경로를 확인한다.

## 4. 필수 복습

- `href`와 `src`의 역할 차이는?
- `<div>`와 의미 있는 태그(`<header>`, `<nav>`, `<main>`)의 차이는?
- `id`·`class`·CSS 선택자의 관계를 설명할 수 있는가?
- 이미지의 `alt`, 폼의 `<label>`이 접근성 측면에서 중요한 이유는?
- `iframe`은 다른 문서를 포함하지만 보안·접근성을 고려해 적절히 사용해야 한다.

[⬅ 프로젝트 목록으로](../README.md)
