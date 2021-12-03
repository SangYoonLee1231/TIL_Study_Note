# HTML의 다양한 태그

>  참고 강의 : 「<a href="https://nomadcoders.co/kokoa-clone">노마드 코더 - 코코아톡 클론코딩</a>」, 「<a href="https://youtube.com/playlist?list=PLuHgQVnccGMAE4Sn_SYvMw5-qEADJcU-X">생활코딩 - 웹 애플리케이션 만들기</a>」

<br/>

* HTML 자주 쓰이는 태그를 정리하였다. 단순 암기하지 말고 자주 쓰면서 익숙해지자.

* 모르는 태그는 구글에 검색하여 MDN Web Docs에 가서 찾아 쓰자. https://developer.mozilla.org/ko/docs/Web/HTML/Element

## 줄바꿈 태그

* \<br> : 강제 줄바꿈 태그 (Self-CLosing 태그)

* \<p> : 단락 표시  
(의미를 담고 있는 태그이므로 \<br>보다 좋은 태그이다.)

## \<head> 내부 태그

* \<title> : 웹페이지에 타이틀 달기

* \<meta> :  다양한 종류의 메타 데이터 나타냄
  
  * \<meta charset="UTF-8"> : 브라우저에서 text를 어떻게 render할 지 말해주는 역할 (미작성시 글자가 깨질 수 있으니 항상 넣어줄 것)
  
  * \<meta content="..." name="description" /> : Google이 검색할 때 찾는 태그. Google 검색 시 링크 창의 설명란에 표시.

* \<link>

  * \<link rel="shortcut icon" sizes="16x16 32x32 64x64" href="(img 주소)" /> : 웹 브라우저 탭의 이미지 설정

  * \<link rel="stylesheet" href="style.css" /> : style이름의 css파일과 연결
