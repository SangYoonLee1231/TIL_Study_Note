# 웹 사이트의 구성과 HTML의 기본

<br/>

> 참고 자료 : 「<a href="https://nomadcoders.co/kokoa-clone" target="_blank">노마드 코더 - 코코아톡 클론코딩 강의</a>」, 「<a href="https://youtube.com/playlist?list=PLuHgQVnccGMAE4Sn_SYvMw5-qEADJcU-X">생활코딩 - 웹 애플리케이션 만들기</a>」, 학부 수업 자료

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md#%EC%9B%B9-%EC%82%AC%EC%9D%B4%ED%8A%B8%EC%9D%98-%EA%B5%AC%EC%84%B1">웹 사이트의 구성</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md#-html-%EC%86%8C%EA%B0%9C">HTML 소개</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md#html-%EA%B8%B0%EB%B3%B8-%EB%AC%B8%EB%B2%95">HTML 기본 문법</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md#html%EC%9D%98-%EA%B8%B0%EB%B3%B8-%EA%B5%AC%EC%A1%B0">HTML의 기본 구조</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md#html-%EC%86%8D%EC%84%B1attribute">HTML 속성(attribute)</a>
- <a href=""></a>

<br/><br/>

## 웹 사이트의 구성

- interactive한 웹 사이트든, 단순한 웹 사이트든, 웹의 내부 구조는 같다.

- <strong>웹 사이트는 그저 text 파일이다.</strong>

<br/>

- 웹 사이트는 우리가 만드는 것이 아니라, 브라우저가 코드(text 파일)를 보고 이해해서 만들어주는 것이다.

- 즉, 개발자인 우리의 역할은 브라우저가 이해하는 text(코드)를 쓰는 일이다.

  - 어디에 어떤 종류의 text를 써야하는 지

<br/>

- 웹 사이트는 보통 3개의 언어(text)로 구성되어 있다.

  - <strong>HTML, CSS, JavaScript</strong>

  - 이 셋 중 프로그래밍 언어는 Javascript 뿐이다.

<br/><br/>

## 🗨 HTML 소개

- ✨ <strong>HTML (Hypertext Markup Language) 은 브라우저에게 content의 구조를 설명하는 언어이다.</strong>

- HTML은 웹 사이트의 뼈대를 담당한다.

<br/>

- HTML은 <strong>인간의 언어를 이해하지 못하는</strong> 브라우저에게,

  웹 사이트의 content (이미지, 제목, 사진, 사이드 바 등등..) 가 어떻게 구성되어 있는지 설명한다.

  - "브라우저야 이건 <code>title</code>이고, 이건 날짜야. 이것은 <code>img</code>(이미지)이고 이 <code>img</code>는 따로 설명이 되어 있어."

<br/>

- HTML의 모든 태그는 검색으로 찾아 쓸 수 있으니 

  태그를 일일이 외우는 것보단 <strong>코드가 어떻게 작동하는 지를 이해하는 것</strong>이 중요하다.

<br/><br/>

## HTML 기본 문법

- HTML은 <strong>태그</strong>로 구성되어 있다.

- HTML 태그엔 두 종류가 있다. - <strong>『일반 태그』</strong> vs <strong>『Self-Closing 태그』</strong>

  ```html
  /* 일반 태그 작성법 */
  <tag> content </tag>

  /* Self-Closing 태그 작성법 */
  <tag ... />
  ```

<br/>

- 일반 HTML 태그는 <strong>열고 반드시 닫아주어야</strong> 한다.

- 그리고 여는 태그(Start Tag)와 닫는 태그(End Tag)의 <strong>이름은 반드시 동일</strong>해야 한다.

- ✨ <strong>여는 태그(Start Tag)</strong>와 <strong>닫는 태그(End Tag)</strong> 사이에 <strong>내용(Content)</strong>을 작성하고, 태그와 내용은 함께 HTML의 한 <strong>요소(Element)</strong>를 이룬다.

- Self-Closing 태그로 구성된 요소를 Void 요소라고 한다.

<br/>

- 만일 HTML 코드를 잘못 입력하더라도 브라우저는 <strong>에러를 표시하지 않는다.</strong>

  따라서 올바른 위치에 올바른 태그를 사용하는 것이 정말 중요하다.

<br/><br/>

## HTML의 기본 구조

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Document</title>
  </head>
  <body>
    <h1>hello world!</h1>
  </body>
</html>
```

- <strong>\<!DOCTYPE html></strong> : 이 파일은 html임을 브라우저에게 알리는 코드

<br/>

- \<html>은 <strong>\<head></strong> 부분과 <strong>\<body></strong>부분으로 나뉜다.

  - <strong>\<head></strong> : 사용자의 눈에 보이지 않는 웹사이트 환경을 설정하는 부분

    (데이터를 설명하는 메타 데이터를 삽입하는 영역)

  - <strong>\<body></strong> : 사용자가 볼 수 있는 content를 작성하는 부분

<br/><br/>

## HTML 속성(attribute)

- <strong>속성(attribute)</strong> : HTML 태그에 추가하여 태그의 동작을 제어하도록 사용자가 지정하는 값

- HTML 태그의 속성은 태그 이름과 <strong>반드시 띄어쓴다</strong>.
- attribute에 값을 넣을 때, <strong>큰 따옴표("")</strong>를 사용하는 것이 좋다. (작은 따옴표(''), 백틱(``) 사용 자제)

<br/>

```html
/* 작성법 */
<tagname attrName="">좋은 개발자가 되고 싶다</tagname>

/* 실제 사용 예시 */
<div id="title">
  <a href="http://google.com" target="_blank">구글로 이동</a>
  <input disabled />
</div>
```

<br/>

- 태그와 속성은 대소문자를 구분하지 않는다.

- 일부 attribute는 모든 태그에 사용 가능하다. (예: id, class, style)

- 반대로 일부 attribute는 특정 태그만 사용 가능하다. (예: \<a href="">, \<img src="">, \<input type="">)

<br/>

- 다양한 태그의 attribute(속성)이 존재하나 역시 무작정 암기 X. <strong>사용법을 이해하고 필요할 때 검색해서 찾아 쓰자.</strong>

- HTML은 attribute와 결합할 때 강력해진다.