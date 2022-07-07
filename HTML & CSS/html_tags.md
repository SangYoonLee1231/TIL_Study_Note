# HTML의 다양한 태그

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

- HTML에서 자주 쓰이는 태그를 최대한 많이 정리하였다. <strong>단순 암기하지 말고 계속 쓰면서 익숙해지자.</strong>

- ✨ 모르는 태그는 구글에 검색하거나 <a href="https://developer.mozilla.org/ko/docs/Web/HTML/Element">MDN Web Docs</a>에 가서 찾아 쓰자. <br/>
  <br/>

## \<head> 내부 태그 (메타 데이터 삽입 태그)

- <code>\<title></code> : 웹페이지에 타이틀 달기

- <code>\<meta></code> : 다양한 종류의 메타 데이터 나타냄

  - <code>\<meta charset="UTF-8"></code> : 브라우저에서 text를 어떻게 render할 지 말해주는 역할 (미작성시 글자가 깨질 수 있으니 항상 넣어줄 것)

  - <code>\<meta content="..." name="description" /></code> : Google이 검색할 때 찾는 태그. Google 검색 시 링크 창의 설명란에 표시.

- <code>\<link></code>

  - <code>\<link rel="shortcut icon" sizes="16x16 32x32 64x64" href="(img 주소)" /></code> : 웹 브라우저 탭의 이미지 설정

  - <code>\<link rel="stylesheet" href="style.css" /></code> : style이름의 css파일과 연결

- <code>\<style></code> : 웹 페이지 전체에 적용할 css(스타일 시트) 코드 작성

<br/>

## \<body> 내부 태그

### 블록, 인라인 태그

- 블록(<code>block</code>) 태그 : 양 옆에 다른 content 배치 X, 한 라인 독점 사용
  - <code>\<div></code>, <code>\<p></code>, <code>\<h1></code>, <code>\<ul></code>
- 인라인(<code>inline</code>) 태그 : 블록 속에 삽입되어 블록의 일부로 출력
  - <code>\<strong></code>, <code>\<a></code>, <code>\<img></code>, <code>\<span></code>

<br/>

### 줄바꿈

- <code>\<br></code> OR <code>\<br/></code> : 강제 줄바꿈 태그 (Self-Closing 태그)

- <code>\<p></code> : 단락 표시  
  (의미를 담고 있는 태그이므로 <code>\<br></code>보다 좋은 태그이다.)

<br/>

### 목록 (리스트)

- <code>\<ol></code> : ordered list - 순서가 있는 목록 (부모 태그)

- <code>\<ul></code> : unordered list - 순서가 없는 목록 (부모 태그)

- <code>\<li></code> : 목록의 각 항목을 나열하는 태그 (자식 태그)

```html
<ol>
  <li>사과</li>
  <li>김치</li>
  <li>고기</li>
</ol>
```

- ol 태그의 type 속성(attribute)

  - <code>\<ol type="A"></code> : 1,2,3 숫자 순이 아닌 A,B,C 알파벳 순으로 리스트 항목 표시

<br/>

### 미디어 content 태그

- <code>\<img></code> : 이미지 삽입 태그 (Self-Closing Tag)

  - <code>\<img src="... .jpg" width="150" height="200" alt="사진 없음 아무튼 없음"></code>

- <code>\<video></code> : 비디오 삽입 태그

<br/>

### 표 (테이블) 태그

- <code>\<table></code> : 표 전체를 담는 컨테이너

- <code>\<caption></code> : 표 제목

- <code>\<tr></code>,<code>\<th></code>,<code>\<td></code> : 행(가로줄), 열(세로줄), 데이터 셀

- 셀 합치기

  - <code>\<td></code> 요소의 <code>rowspan</code> 속성(attribute) : 위 아래 줄(rows)의 셀 병합

  - <code>\<td></code> 요소의 <code>colspan</code> 속성(attribute) : 옆 칸(column)의 셀 병합

- 자세한 건 검색을 활용하자.

<br/>

### Form 태그

- 정보를 제출하기 위한 대화형 컨트롤을 포함하는 문서 구획을 나타낸다.

- <code>form</code> 내부에서, <code>input</code> 안에 있는 버튼을 누르거나, <code>type="submit"</code>인 input을 클릭하거나, 엔터를 누르면 (<code>input</code>이 더 이상 존재X)  
  작성된 form이 자동으로 submit되고, 웹페이지는 새로고침 된다.

- form 속성

  - <code>action</code> : form 제출 시, 어떤 html 파일로 데이터를 보낼 지를 지정하는 것
  - <code>method</code> : form의 데이터를 보내는 방식. GET 방식 또는 POST 방식이 있음.  
    (GET 방식은 URL, POST 방식은 서버에 전송하는 방식)

<br/>

### 기타 태그

- <code>\<hr></code> : 수평선 긋기

- <code>\<a></code> : 하이퍼링크 태그

<br/>

## Semantic HTML

<img src="img/html_semantic.jpeg">
