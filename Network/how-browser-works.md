# 브라우저의 동작 원리

<br/>

- 스터디 발표를 준비하며 공부한 내용입니다.

- 브라우저 주소 창에 naver.com 을 쳤을 때 일어나는 일을 <strong>네트워크의 관점</strong>에서 정리했습니다.

<br/>

### 목차

- <a href="">사전 지식</a>

  - <a href="">브라우저 아키텍처</a>
  - <a href="">네트워크 기초 사전 지식</a>

- <a href="">브라우저 주소 창에 naver.com를 치고 Enter을 누르면 일어나는 과정</a>

  - <a href="">Step 1. 주소창에 입력한 텍스트 정보 확인</a>
  - <a href="">Step 2. 네트워크 호출</a>
  - <a href="">Step 3. 렌더링 작업</a>

- <a href="">렌더링 프로세스</a>
  - <a href="">1. HTML 파싱 → DOM 트리 생성</a>
  - <a href="">2. CSS 파싱 → CSSOM 트리 생성</a>
  - <a href="">3. Render Tree 생성</a>
  - <a href="">4. 레이아웃 (Layout)</a>
  - <a href="">5. 페인트 (Paint)</a>

<br/><br/>

## 사전 지식

### 브라우저 아키텍처

- 브라우저의 주 기능은 사용자가 서버에 필요한 자원을 요청하고, 응답받은 자원을 화면에 표시하는 것이다.

<br/>

- <strong>브라우저의 구조</strong>

  <img src="img\browser_architecture.png">

  👉 <a href="https://d2.naver.com/helloworld/59361">사진 출처</a>

  <br/>

  - <strong>사용자 인터페이스 (User Interface / UI)</strong>

    - 페이지를 보여주는 창을 제외한 나머지 모든 영역.

    - 주소 표시줄, 이전, 이후 버튼, 홈버튼, 북마크 버튼 등

  - <strong>브라우저 엔진 / 레이아웃 엔진</strong>

    - 사용자 인터페이스와 렌더링 엔진 사이의 동작을 제어한다.

    - (UI를 그리는 <strong>UI 스레드</strong>, 네트워크 통신을 위한 <strong>네트워크 스레드</strong>, 파일에 접근하기 위한 <strong>스토리지 스레드</strong> 등이 존재한다.)

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

<br/>

### 네트워크 기초 사전 지식

- URL <code>www.\*\*\*.\*\*\*</code>에서 \*\*\*.\*\*\* 에 해당하는 부분을 <strong>도메인 네임 (또는 도메인)</strong>이라 한다.

- 웹 브라우저는 도메인 네임을 해석할 수 없기 때문에, 이 도메인을 IP 주소로 변환해주는 <strong>DNS (Domain Name System)</strong>가 필요하다.

- DNS는 <strong>네임 서버 (Name Server)</strong> 가 운영하는 장치이다.

<br/><br/>

## 브라우저 주소 창에 naver.com를 치고 Enter을 누르면 일어나는 과정

### Step 1. 주소창에 입력한 텍스트 정보 확인

(주소창에 n을 치면 자동완성 기능으로 검색어가 표시될 수 있다.)

- 우선, 사용자가 주소창에 입력한 텍스트가 '<strong>검색어</strong>'인지 '<strong>URL</strong>'인지 확인한다.

  (이 작업의 주체는 브라우저 엔진의 UI 스레드이다.)

- 입력한 텍스트가 '<strong>검색어</strong>'이면, 검색 엔진 URL에 검색어를 포함한 주소로 페이지를 이동시킨다.

- 입력한 텍스트가 '<strong>URL</strong>'이면, 브라우저 엔진에서 네트워크 스레드를 통해 '<strong>네트워크 호출</strong>'을 수행한다.

<br/>

### Step 2. 네트워크 호출

(위에 정리해놓은 <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Network/how-browser-works.md#%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EA%B8%B0%EC%B4%88-%EC%82%AC%EC%A0%84-%EC%A7%80%EC%8B%9D">네트워크 기초 사전 지식</a>을 숙지해야 한다)

- 사용자가 주소창에 도메인 네임이 포함된 URL (여기서는 <code>www.naver.com</code>) 를 입력하면

- <strong>클라이언트 (사용자의 컴퓨터)</strong> 는 hosts 파일에서 그 도메인 네임 (<code>naver.com</code>) 에 대응하는 <strong>IP 주소 정보</strong>가 있는지 확인한다.

- 만일 없다면, 클라이언트는 네임 서버에게 도메인의 IP 주소를 질의하는 <strong>요청 패킷</strong>을 보낸다.

- 네임 서버는 자신의 데이터베이스 목록에 해당 IP 주소를 찾아 클라이언트에게 <strong>응답 패킷</strong>을 보낸다.

<br/>

- 클라이언트는 이렇게 알아낸 IP 주소(<code>125.209.222.142</code>)를 바탕으로 <strong>TCP 소켓</strong>을 통해 네이버 서버에 <strong>HTTP Request</strong>를 보낸다.

- HTTP Request를 받은 네이버 서버는 <strong>HTTP Reply</strong>를 클라이언트에 보낸다.

- 네이버 서버로부터 응답을 받은 클라이언트의 브라우저는 페이지를 띄우는데 필요한 <strong>데이터 (HTML, CSS, Javascript, 이미지 파일 등)</strong> 를 얻었다.

<br/>

### Step 3. 렌더링 작업

- 네트웨크 스레드는 이렇게 얻은 데이터를 우선 <strong>검사</strong>한다.

  - 악성 바이러스가 있는지 없는지..

  - (만일 다운로드 파일 형식의 데이터가 응답될 경우, 다운로드 매니저에게 이를 전달한다.)

- 모든 검사가 끝나면 UI 스레드는 <strong>렌더링 엔진</strong>에게 해당 웹 페이지를 화면에 띄울 것을 요청한다.

- 요청을 받은 렌더링 엔진은 응답받은 데이터를 가지고 <strong>렌더링 프로세스</strong>를 수행한다.

- 렌더링이 끝나면 웹 페이지에 화면에 띄워지고 모든 과정이 종료된다.

<br/><br/>

## 렌더링 프로세스

<br/>

### 1. HTML 파싱 → DOM 트리 생성

<br/><br/>

### 2. CSS 파싱 → CSSOM 트리 생성

<br/><br/>

### 3. Render Tree 생성

<br/><br/>

### 4. 레이아웃 (Layout)

<br/><br/>

### 5. 페인트 (Paint)

<br/><br/>

> 참고 자료
>
> - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">브라우저는 어떻게 동작하는가?</a> (NAVER D2)
> - <a href="https://youtu.be/dh406O2v_1c">What happens when you type google.com into your browser and press enter? (Detailed Analysis)</a> (유튜브 영상)
> - 책 『<a href="http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9791165921057">기초부터 완성까지, 프론트엔드</a>』 (이재성, 한전 지음 / 비제이퍼블릭 출판) - 8장. 브라우저 렌더링 과정
> - 2018학년도 수능 모의고사 국어 영억 비문학 지문 - 『DNS 스푸핑』
> - <a href="https://velog.io/@thyoondev/웹-브라우저의-동작원리를-알아보자">웹 브라우저의 동작원리를 알아보자</a> (블로그 포스트)
> - <a href="https://poiemaweb.com/js-browser">브라우저 동작 원리</a> (PoiemaWeb)
> - <a href="https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=pxkey&logNo=221216492103">IP 주소와 도메인의 관계</a> (블로그 포스트)
> - <a href="https://hanamon.kr/dns%eb%9e%80-%eb%8f%84%eb%a9%94%ec%9d%b8-%eb%84%a4%ec%9e%84-%ec%8b%9c%ec%8a%a4%ed%85%9c-%ea%b0%9c%eb%85%90%eb%b6%80%ed%84%b0-%ec%9e%91%eb%8f%99-%eb%b0%a9%ec%8b%9d%ea%b9%8c%ec%a7%80/">DNS란? (도메인 네임 시스템 개념부터 작동 방식까지)</a> (블로그 포스트)
> - <a href="https://code-lab1.tistory.com/154">[네트워크] 웹사이트 접속 과정에 대하여 (네트워크 과목 총 정리) | 주소창에 www.google.com을 입력하면 생기는 일</a> (블로그 포스트)
