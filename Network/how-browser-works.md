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

  - <strong>브라우저 엔진 / 레이아웃 엔진</strong>

    - 사용자 인터페이스와 렌더링 엔진 사이의 동작을 제어한다.

    - UI를 그리는 UI 스레드, 네트워크 통신을 위한 네트워크 스레드, 파일에 접근하기 위한 스토리지 스레드 등이 존재한다.

  - <strong>렌더링 엔진</strong>

    - 브라우저 엔진과 밀접히 관련된 엔진으로, 웹 페이지가 표시되는 모든 영역을 제어한다.

    - 요청한 콘텐츠(HTML, CSS 등)를 파싱하고, 화면에 나타내는 일을 수행한다.

  - <strong>자료 저장소 / 데이터 저장소</strong>

    - 말 그대로 자료 저장소다.

    - 쿠기나, localStorage, IndexedDM 같이 로컬에 저장되어 좀 더 오래 유지되어야 하는 데이터들을 보관할 수 있도록 지원하는 영역이다.

  <br/>

  - <strong>통신 (Networking)</strong>

    - HTTP/HTTPS 네트워크 처리를 한다.

    - 플랫폼과 독립적인 인터페이스로, 각 플랫폼의 하부에서 실행된다.

  - <strong>자바스크립트 해석기 (JS Interpreter) / 자바스크립트 엔진</strong>

    - 스크립트(JS 코드)를 파싱(해석)할 때 사용하는 JS 엔진이다.

    - HTML을 파싱(해석) 중 script 태그를 만나면, JS 엔진이 제어 권한을 넘겨받는다. 이 작업은 동기적으로 진행된다.

      - 동기적으로 진행 → JS 엔진이 작업을 마칠 때까지 HTML에서 진행 중인 과정은 잠시 중지된다.

  - <strong>UI 백엔드 (UI Backend)</strong>

    - 기본 위젯를 그릴 때 사용한다.

<br/>

- 인터넷 브라우저에는 Chrome, Safari, IE, Firefox, 오페라 등 여러 종류가 있고, 각 브라우저마다 아키텍처가 조금씩 다르지만 큰 틀은 위의 구조와 같다.

<br/><br/>

- 그럼 이제 브라우저 주소 창에 naver.com 을 치고 Enter을 누르면 무슨 일이 일어나는 지 본격적으로 살펴보자.

### Step 1. 브라우저 엔진에서 일어나는 일

- (주소창에 n을 치면 자동완성 기능으로 검색어가 표시될 수 있다.)

- 우선, 사용자가 주소창에 입력한 텍스트가 '검색어'인지 'URL'인지 확인한다.

  (이 작업의 주체는 브라우저 엔진의 UI 스레드이다.)

- 입력한 텍스트가 '검색어'이면, 검색 엔진 URL에 검색어를 포함한 주소로 페이지를 이동시킨다.

- 입력한 텍스트가 'URL'이면, 네트워크 호출을 수행한다.

<br/>

- URL은 도메인 네임이라고도 한다.

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
