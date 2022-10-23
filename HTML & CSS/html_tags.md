# HTML의 다양한 태그

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

- HTML에서 자주 쓰이는 태그를 최대한 많이 정리하였다. <strong>단순 암기하지 말고 계속 쓰면서 익숙해지자.</strong>

- ✨ 모르는 태그는 구글에 검색하거나 <strong><a href="https://developer.mozilla.org/ko/docs/Web/HTML/Element">MDN Web Docs</a></strong>에 가서 찾아 쓰자.

<br/>

### 목차

- <a href="">\<!DOCTYPE html></a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_tags.md#head-%EB%82%B4%EB%B6%80-%ED%83%9C%EA%B7%B8-%EB%A9%94%ED%83%80-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%82%BD%EC%9E%85-%ED%83%9C%EA%B7%B8">\<head> 내부 태그 (메타 데이터 삽입 태그)</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_tags.md#body-%EB%82%B4%EB%B6%80-%ED%83%9C%EA%B7%B8">\<body> 내부 태그</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_tags.md#%ED%83%9C%EA%B7%B8%EC%9D%98-%EB%B6%84%EB%A5%98---%EB%B8%94%EB%A1%9D-%EC%9D%B8%EB%9D%BC%EC%9D%B8-%ED%83%9C%EA%B7%B8">태그 분류 - 블록, 인라인 태그</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_tags.md#%EC%A4%84%EB%B0%94%EA%BF%88">줄바꿈 - <code>\<br></code>, <code>\<p></code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_tags.md#%EB%AA%A9%EB%A1%9D-%EB%A6%AC%EC%8A%A4%ED%8A%B8">목록 (리스트) - <code>\<ol></code>, <code>\<ul></code>, <code>\<li></code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_tags.md#%EB%AF%B8%EB%94%94%EC%96%B4-content-%ED%83%9C%EA%B7%B8">미디어 content 태그 - <code>\<img></code>, <code>\<video></code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_tags.md#%ED%91%9C-%ED%85%8C%EC%9D%B4%EB%B8%94-%ED%83%9C%EA%B7%B8">표 (테이블) 태그</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_tags.md#form-%ED%83%9C%EA%B7%B8">Form 태그</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_tags.md#%EA%B8%B0%ED%83%80-%ED%83%9C%EA%B7%B8">기타 태그 - <code>\<a></code>, <code>\<hr></code></a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_tags.md#semantic-html">Semantic HTML</a>

<br/><br/>

### <code>\<!DOCTYPE html></code>

- HTML 파일의 최상단에 위치하는 선언문으로, HTML 태그는 아니다.

- <strong>이 html 파일이 무슨 버전의 html을 사용했는지</strong> 브라우저에 알려주는 역할을 한다.

- <code>\<!DOCTYPE html></code>은 이 문서가 HTML5 버전으로 작성되었다는 것을 의미한다.

<br/>

## <code>\<head></code> 내부 태그 (메타 데이터 삽입 태그)

- <strong><code>\<title></code></strong> : 웹페이지에 타이틀 달기 (브라우저 탭에 표시)

  - <code>\<title>제목\</title></code>

<br/>

- <strong><code>\<meta></code></strong> : 다양한 종류의 메타 데이터를 나타낸다.

  - <code>\<meta charset="UTF-8"></code>

    - 브라우저에서 HTML 텍스트를 어떻게 render할 지 설명해주는 역할을 한다. (미작성시 글자가 깨질 수 있으니 항상 넣어줄 것)

    - 한글, 일본어, 중국어가 포함된 페이지라면 <code>UTF-8</code> 이라는 값으로 문자 인코딩을 추가해줘야 한다.

  - <code>\<meta content="..." name="description"></code>

    - Google이 검색할 때 찾는 태그. Google 검색 시 링크 창의 설명란에 해당 요소의 내용을 표시한다.

  - <code>\<meta name="viewport" content="width=device-width"></code>

    - '디바이스의 가로 크기 == 웹페이지의 가로 크기' 라는 의미이다.

    - 모바일 환경에서 웹페이지가 잘 보여지도록 해준다.

<br/>

- <strong><code>\<link></code></strong>

  - <code>\<link rel="shortcut icon" sizes="16x16 32x32 64x64" href="(img 주소)" /></code>

    - 웹 브라우저 탭의 이미지를 설정한다.

  - <code>\<link rel="stylesheet" href="style.css" /></code>

    - <strong>style 이름의 css 파일과 연결한다.</strong>

<br/>

- <strong><code>\<style></code></strong> : 웹 페이지 전체에 적용할 css(스타일 시트) 코드 작성

<br/><br/>

## <code>\<body></code> 내부 태그

### 태그의 분류 - block, inline

- <strong>블록 (<code>block</code>) 태그</strong> : 양 옆에 다른 content 배치 X, 한 라인 독점 사용

  - <strong><code>\<div></code>, <code>\<p></code>, <code>\<h1></code>, <code>\<ul></code></strong>

- <strong>인라인 (<code>inline</code>) 태그</strong> : 블록 속에 삽입되어 블록의 일부로 출력

  - <strong><code>\<strong></code>, <code>\<a></code>, <code>\<img></code>, <code>\<span></code></strong>

<br/>

### 제목 태그

- <strong><code>\<h1></code></strong>, <strong><code>\<h2></code></strong>, <strong><code>\<h3></code></strong>, <strong><code>\<h4></code></strong>, <strong><code>\<h5></code></strong> : 제목을 표시해주는 태그

  (h 뒤에 붙는 숫자가 클수록 글씨 크기가 작아진다.)

<br/>

### 줄바꿈

- <strong><code>\<br></code></strong> 또는 <code>\<br/></code> : 강제 줄바꿈 태그 (Self-Closing 태그)

<br/>

- <strong><code>\<p></code></strong> : 단락 표시

  (의미를 담고 있는 태그이므로 <code>\<br></code>보다 좋은 태그이다.)

- <strong><code>\<div></code></strong> : 보편적으로 쓰이는 단락 표시 태그

<br/>

### 목록 (리스트)

- <strong><code>\<ol></code></strong> : ordered list - 순서가 있는 목록

- <strong><code>\<ul></code></strong> : unordered list - 순서가 없는 목록

- <strong><code>\<li></code></strong> : 목록의 각 항목을 나열하는 태그

  - <code>\<ol></code> 혹은 <code>\<li></code> 태그의 내부에 자식 태그로 쓰인다.

```html
<ol>
  <li>사과</li>
  <li>김치</li>
  <li>고기</li>
</ol>

<ul>
  <li>1번</li>
  <li>2번</li>
  <li>3번</li>
</ul>
```

<br/>

- <code>\<ol></code> 태그의 type 속성(attribute)

  - <code>\<ol type="A"></code> : 1,2,3 숫자 순이 아닌 A,B,C 알파벳 순으로 리스트 항목 표시

<br/>

### 미디어 content 태그

- <strong><code>\<img></code></strong> : 이미지 삽입 태그 (Self-Closing Tag)

  - <code>\<img src="... .jpg" width="150" height="200" alt="사진 없음 아무튼 없음"></code>

- <strong><code>\<video></code></strong> : 비디오 삽입 태그

<br/>

### 표 (테이블) 태그

- <strong><code>\<table></code></strong> : 표 전체를 담는 컨테이너

- <strong><code>\<caption></code></strong> : 표 제목

<br/>

- <strong><code>\<tr></code></strong> : 행 (가로줄) (table row)

- <strong><code>\<th></code></strong> : 열 (세로줄) (table heading)

- <strong><code>\<td></code></strong> : 데이터 셀 (table data)

<br/>

- 셀 합치기

  - <code>\<td></code> 요소의 <strong><code>rowspan</code></strong> 속성(attribute) : 위 아래 줄(rows)의 셀 병합 (가로줄끼리 병합)

  - <code>\<td></code> 요소의 <strong><code>colspan</code></strong> 속성(attribute) : 옆 칸(column)의 셀 병합 (세로줄끼리 병합)

<br/>

- 자세한 건 검색을 활용하자.

<br/>

### ✨ Form 태그

- <strong><a href="https://developer.mozilla.org/ko/docs/Web/HTML/Element#%EC%96%91%EC%8B%9D">MDN 문서 - Form 태그 바로가기</a></strong>

- 정보를 제출하기 위한 대화형 컨트롤을 포함하는 문서 구획을 나타낸다.

<br/>

- <strong><code>\<label></code></strong>

  - <code>label</code>은 클릭 시 for 속성과 같은 값의 id를 가지고 있는 <code>input</code>을 작동시킨다.

<br/>

- <strong><code>\<input></code></strong>

  - 사용자로부터 데이터를 입력 받을 수 있는 공간 생성

  - <strong><a href="https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input">MDN 문서</a></strong>에 가서 input의 다양한 유형과 속성을 확인해보자.

    ```html
    <!--label과 함께 쓰이는 input 태그 예시 코드-->
    <form>
      <div>
        <label for="profile">Profile</label>
        <input id="profile" type="file" accept=".txt, image/*" />
      </div>
      <div>
        <input type="color" />
        <input type="range" />
        <input type="date" />
      </div>
    </form>

    <form>
      <div>
        <label for="username">User Name</label>
        <input id="username" type="text" placeholder="Username" required />
        <input type="password" placeholder="Password" minlength="8" required />
      </div>
      <div>
        <input type="submit" value="Create Account" />
      </div>
    </form>

    <form>
      <div>
        <label for="website">Website</label>
        <input type="url" id="website" />

        <label for="email">Email</label>
        <input type="url" id="email" />
      </div>
      <div>
        <input type="submit" value="Submit" />
      </div>
    </form>
    ```

<br/>

- <code>form</code> 내부에서 <code>input</code> 안에 있는 버튼을 누르거나, <code>type="submit"</code>인 input을 클릭하거나, 엔터를 누르면 (<code>input</code>이 더 이상 존재X)  
  작성된 form이 자동으로 submit되고, 웹페이지는 새로고침 된다.

- <strong>form 속성</strong>

  - <strong><code>action</code></strong> : form 제출 시, 어떤 html 파일로 데이터를 보낼 지를 지정하는 것

  - <strong><code>method</code></strong> : form의 데이터를 보내는 방식. GET 방식 또는 POST 방식이 있음.  
    (GET 방식은 URL, POST 방식은 서버에 전송하는 방식)

<br/>

### 기타 태그

- <strong><code>\<a></code></strong> : 하이퍼링크 태그 (anchor의 줄임말)

  - <code>href</code> 속성(attribute)으로 주소를 주어야 한다.

    ```html
    <a href="https://www.google.com/">구글로 이동</a>
    ```

  <br/>

  - <code>target</code> 속성을 부여하면 링크를 어디에서 열지 정할 수 있다.

    - <code>\_self</code>: 현재 창(혹은 탭)에서 링크를 연다.

    - <code>\_target</code>: 새 창(혹은 탭)에서 링크를 연다.

      ```html
      <!--다른 탭으로 구글 웹 페이지 열기-->
      <a href="https://www.google.com/" target="_blank">구글로 이동</a>
      ```

<br/>

- <strong><code>\<hr></code></strong> : 수평선 긋기

<br/><br/>

## Semantic HTML

- 의미가 있는 <code>div</code> 태그

- 문서와 코드가 의미를 가지도록 시멘틱 태그를 사용하는 것이 좋다.

  - <a href="https://sylagape1231.tistory.com/57">Semantic Tag (시멘틱 태그) 를 사용하여 웹 개발을 해야하는 이유</a>

- <code>\<header></code>, <code>\<main></code>, <code>\<footer></code> 등등

<br/>

- <strong>MDN 문서</strong> (시맨틱 태그 예시 참고)

  - <a href="https://developer.mozilla.org/ko/docs/Web/HTML/Element#%EC%BD%98%ED%85%90%EC%B8%A0_%EA%B5%AC%ED%9A%8D">블록 시맨틱 태그</a> & <a href="https://developer.mozilla.org/ko/docs/Web/HTML/Element#%EC%9D%B8%EB%9D%BC%EC%9D%B8_%ED%85%8D%EC%8A%A4%ED%8A%B8_%EC%8B%9C%EB%A9%98%ED%8B%B1">인라인 시맨틱 태그</a>

<br/>

<img src="img/html_semantic.jpeg">
