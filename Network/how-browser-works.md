# 브라우저의 동작 원리

<br/>

> 참고 자료
>
> - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">브라우저는 어떻게 동작하는가?</a> (NAVER D2)
> - <a href="https://youtu.be/dh406O2v_1c">What happens when you type google.com into your browser and press enter? (Detailed Analysis)</a> (유튜브 영상)
> - 책 『<a href="http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791165921057">기초부터 완성까지, 프론트엔드</a>』 (이재성, 한전 지음 / 비제이퍼블릭 출판) - 8장. 브라우저 렌더링 과정
> - 2018학년도 수능 모의고사 국어 영억 비문학 지문 - 『DNS 스푸핑』
> - <a href="https://poiemaweb.com/js-browser">브라우저 동작 원리</a> (PoiemaWeb)
> - <a href="https://velog.io/@thyoondev/웹-브라우저의-동작원리를-알아보자">웹 브라우저의 동작원리를 알아보자</a> (블로그 포스트)

<br/>

- 스터디 발표를 준비하며 공부한 내용입니다.

- 브라우저 주소 창에 naver.com 을 쳤을 때 일어나는 일을 <strong>네트워크의 관점</strong>에서 정리했습니다.

<br/>

### 목차

- <a href=""></a>

<br/><br/>

## Step 0. 브라우저 아키텍처

- 브라우저의 주 기능은 사용자가 서버에 필요한 자원을 요청하고, 응답받은 자원을 화면에 표시하는 것이다.

<br/>

- 브라우저의 구조

  <img src="img\browser_architecture.png">

  - <strong>사용자 인터페이스 (User Interface / UI)</strong>

    - 페이지를 보여주는 창을 제외한 나머지 모든 영역.

    - 주소 표시줄, 이전, 이후 버튼, 홈버튼, 북마크 버튼 등

  - <strong>브라우저 엔진</strong>

    - 페이지를 보여주는 창을 제외한 나머지 모든 영역.

  - <strong>렌더링 엔진</strong>

    - 페이지를 보여주는 창을 제외한 나머지 모든 영역.

  - <strong>자료 저장소 / 데이터 저장소</strong>

    - 페이지를 보여주는 창을 제외한 나머지 모든 영역.

  <br/>

  - <strong>통신 (Networking)</strong>

    - 페이지를 보여주는 창을 제외한 나머지 모든 영역.

  - <strong>자바스크립트 해석기 (JavaScript Interpreter)</strong>

    - 페이지를 보여주는 창을 제외한 나머지 모든 영역.

  - <strong>UI 백엔드 (UI Backend)</strong>

    - 페이지를 보여주는 창을 제외한 나머지 모든 영역.

<br/>

- 인터넷 브라우저에는 많은 종류의

  - Internet Explorer

<br/><br/>

### Step 1. 브라우저 엔진에서 일어나는 일

- 주소창에 n을 치면 자동완성으로 검색어가 표시된다.

<br/><br/>

## 브라우저 렌더링 과정 (렌더링 엔진에서 일어나는 일)

<br/>

### Step 2. HTML 파싱 → DOM 트리 생성

<br/><br/>

### Step 3. CSS 파싱 → CSSOM 트리 생성

<br/><br/>

### Step 4. Render Tree 생성

<br/><br/>

### Step 5. 레이아웃 (Layout)

<br/><br/>

### Step 6. 페인트 (Paint)

<br/><br/>
