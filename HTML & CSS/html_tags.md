# HTML의 다양한 태그

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

* ✨ HTML에서 자주 쓰이는 태그를 최대한 많이 정리하였다. 단순 암기하지 말고 계속 쓰면서 익숙해지자.

* 모르는 태그는 구글에 검색하여 MDN Web Docs에 가서 찾아 쓰자. <br/>
https://developer.mozilla.org/ko/docs/Web/HTML/Element

<br/>

## \<head> 내부 태그 (메타 데이터 삽입 태그)

* <strong>\<title></strong> : 웹페이지에 타이틀 달기

* <strong>\<meta></strong> :  다양한 종류의 메타 데이터 나타냄
  
  * <strong>\<meta charset="UTF-8"></strong> : 브라우저에서 text를 어떻게 render할 지 말해주는 역할 (미작성시 글자가 깨질 수 있으니 항상 넣어줄 것)
  
  * <strong>\<meta content="..." name="description" /></strong> : Google이 검색할 때 찾는 태그. Google 검색 시 링크 창의 설명란에 표시.

* <strong>\<link></strong>

  * <strong>\<link rel="shortcut icon" sizes="16x16 32x32 64x64" href="(img 주소)" /></strong> : 웹 브라우저 탭의 이미지 설정

  * <strong>\<link rel="stylesheet" href="style.css" /></strong> : style이름의 css파일과 연결

* <strong>\<style></strong> : 웹 페이지 전체에 적용할 css(스타일 시트) 코드 작성

<br/>

## \<body> 내부 태그

### 블록, 인라인 태그
    
* 블록(Block) 태그 : 양 옆에 다른 content 배치 X, 한 라인 독점 사용
    
    * <strong>\<div>, \<p>, \<h1>, \<ul></strong>
    
* 인라인(Inline) 태그 : 블록 속에 삽입되어 블록의 일부로 출력
    
    * <strong>\<strong>, \<a>, \<img>, \<span></strong>

### 줄바꿈

* <strong>\<br></strong> : 강제 줄바꿈 태그 (Self-Closing 태그)

* <strong>\<p></strong> : 단락 표시  
(의미를 담고 있는 태그이므로 \<br>보다 좋은 태그이다.)

### 목록 (리스트)

* <strong>\<ol></strong> : ordered list - 순서가 있는 목록 (부모 태그)

* <strong>\<ui></strong> : unordered list - 순서가 없는 목록 (부모 태그)

* <strong>\<li></strong> : 목록의 각 항목을 나열하는 태그 (자식 태그)

```html
<ol>
    <li> 사과 </li>
    <li> 김치 </li>
    <li> 고기 </li>
</ol>
```

* ol 태그의 type 속성(attribute) 

  * <strong>\<ol type="A"></strong> : 1,2,3 숫자 순이 아닌 A,B,C 알파벳 순으로 리스트 항목 표시


### 미디어 content 태그

* <strong>\<img></strong> : 이미지 삽입 태그 (Self-Closing Tag)

  * <strong>\<img src="... .jpg" width="150" height="200" alt="사진 없음 아무튼 없음"></strong>

* <strong>\<video></strong> : 비디오 삽입 태그

### 표 (테이블) 태그

* <strong>\<table></strong> : 표 전체를 담는 컨테이너

* <strong>\<caption></strong> : 표 제목

* <strong>\<tr>,\<th>,\<td></strong> : 행(가로줄), 열(세로줄), 데이터 셀

* 셀 합치기

  * \<td> 요소의 rowspan 속성(attribute) : 위 아래 줄(rows)의 셀 병합

  * \<td> 요소의 colspan 속성(attribute) : 옆 칸(column)의 셀 병합

* 자세한 건 검색을 활용하자.

### Form 태그

*  

### 기타 태그

* <strong>\<hr></strong> : 수평선 긋기

* <strong>\<a></strong> : 하이퍼링크 태그

<br/>

## Semantic HTML