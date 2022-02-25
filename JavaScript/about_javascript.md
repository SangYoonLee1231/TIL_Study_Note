# JavaScript 소개 (By 공식 문서)

> <a href="https://developer.mozilla.org/ko/docs/Web/JavaScript">JS 공식 문서 - JavaScript 메인 페이지 바로 가기 (MDN Web Docs)</a>

<br/>

### JavaScript는 <strong>just-in-time</strong> 컴파일 프로그래밍 언어이다.

- JavaScript는 동적 프로그래밍 언어(Dynamic Programming Language)이다.

  - 동적 프로그래밍 언어(혹은 동적 언어)란, 다른 언어에서 컴파일 과정 중 수행하는 특정 일들을, 런타임(실행 도중)에 수행하는 고급 언어를 의미한다.

* JIT(just-in time) 컴파일은 프로그램을 만드는 2가지 방식인 인터프리트 방식과 정적 컴파일 방식의 절충안(혼합)이다.

- JIT(just-in time) 컴파일은 실행 시점에서 고수준의 프로그래밍 언어를 저수준의 기계어로 번역한다.

- 이 때, 같은 함수가 여러 번 불려 똑같은 기계어 코드가 생성되는 것을 방지하기 위해, 기계어 코드 생성 시 이를 <strong>캐싱</strong>하는 방식으로 컴파일을 수행한다.

> 참고 자료 : <a href="https://ko.wikipedia.org/wiki/%EB%8F%99%EC%A0%81_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%96%B8%EC%96%B4"> 동적 프로그래밍 언어 (위키백과)</a>,  
> <a href="https://ko.wikipedia.org/wiki/JIT_%EC%BB%B4%ED%8C%8C%EC%9D%BC"> JIT 컴파일 (위키백과)</a>

<br/>

- 캐싱(Caching)은, 속도가 느린 데이터를 캐시(Cache)라고 하는 더 빠른 메모리 영역으로 가자고 와서 읽기, 쓰기와 같은 연산을 수행하는 것을 말한다.

* 이 때, 자주 사용되는, 지역성(Locality)을 가진 데이터를 더 빠른 속도를 가진 메모리상에 저장하면, CPU가 더욱 빠르게 데이터를 꺼내서 사용할 수 있다. 이는 물론 성능 개선에도 기여한다.

* (참고) 데이터의 지역성(Locality)

  - 공간 지역성 : 한 번 접근된 데이터의 주변에 저장되어 있는 다른 데이터가 순서대로 접근될 가능성이 높다.

  - 시간 지역성 : 한 번 접근된 데이터가 가까운 시간 내에 다시 접근될 가능성이 높다.

> 참고 자료 : <a href="https://m.blog.naver.com/complusblog/221204759836">캐싱(Caching)과 버퍼링(Buffering) 그리고 스풀링(Spooling) (개인 블로그)</a>,  
> <a href="https://literate-t.tistory.com/73">[Cache] 시간 지역성, 공간 지역성 :: 안 주면 훔칩니다 (개인 블로그)</a>

<br/><br/>

### JavaScript는 일급 함수를 지원한다.

- 함수를 마치 변수처럼 다루는 언어를 '일급 함수를 가진 언어'라고 표현한다.

- 일급 함수를 가진 언어에선 다음 3가지가 모두 가능하다.

  - 함수를 다른 함수에 변수처럼 인자로 넘겨줄 수 있다.

  - 함수가 다른 함수를 반환할 수 있다.

  * 함수를 변수에 할당할 수 있다.

* 함수를 어떻게 변수처럼 다루는 지는 아래 공식 문서에 기술된 여러 예시를 통해 자세히 알 수 있다.

> 참고 자료 : <a href="https://developer.mozilla.org/ko/docs/Glossary/First-class_Function"> 일급 함수 (MDN Web Docs)</a>

<br/><br/>

### JavaScript는 웹페이지를 위한 스크립트 언어로 잘 알려져 있지만, 많은 비 브라우저 환경에서도 사용하고 있다.

- JavaScript가 쓰이는 비 브라우저 환경 예시

  - Node.js, Apache CouchDB, Adobe Acrobat

<br/><br/>

### JavaScript는 프로토타입 기반(Prototype-Based) 언어이다.

- 프로토타입 기반(prototype-based) 프로그래밍은 객체지향 프로그래밍의 한 형태로, 클래스 대신 원형 객체(프로토타입) 복제해서 사용하는, 일종의 디자인 패턴이다.

* JavaScript에서 객체는 함수를 통해서 만들어지고, 객체는 함수의 프로토타입 객체를 복제하여 생성한다.

* JavaScript의 모든 객체는 다른 프로토타입 객체를 복제해서 만들어지는데, 이러한 복제 과정을 거슬러 올라가보면, 그 시작점은 Object 함수의 프로토타입인 Object.prototype임을 알 수 있다.

  - JavaScript의 모든 함수는 Function.prototype 객체를 자신의 원본으로 가진다. 그리고 Function.prototype은 결국 객체이므로, 원본으로 Object.prototype 객체를 가진다.

* 자세한 내용은 아래 링크를 참조

> 참고 자료 : <a href="https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9C%ED%86%A0%ED%83%80%EC%9E%85_%EA%B8%B0%EB%B0%98_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D">프로토타입 기반 프로그래밍 (위키백과)</a>,  
> <a href="https://medium.com/@bluesh55/javascript-prototype-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-f8e67c286b67">[Javascript] 프로토타입 이해하기 (개인 블로그)</a>,  
> <a href="https://evan-moon.github.io/2019/10/23/js-prototype/">✨ [JS 프로토타입] 자바스크립트의 프로토타입 훑어보기 (개인 블로그)</a>

<br/><br/>

### JavaScript는 다중 패러다임(Multi-Paradigm) 언어이다.

- 다중 패러다임 (프로그래밍) 언어는 두 가지 이상의 프로그래밍 패러다임을 지원하는 언어를 말한다.

* "모든 문제를 가장 쉽고 효율적으로 풀 수 있는 단 하나의 패러다임은 존재하지 않는다"  
  이 사실을 인정하고, 프로그래머가 자신의 작업에 가장 알맞는 패러다임을 선택할 수 있도록 하는 것이 다중 패러다임 언어의 설계 목적이다.

* 객체지향 프로그래밍, 함수형 프로그래밍, 명령형 프로그래밍, 선언형 프로그래밍, 절차적 프로그래밍 등등 프로그래밍 패러다임의 종류는 다양하다.

* JavsScript는 프로토타입 기반의 객체 지향형, 명령형(imperative), 선언형(declarative) (함수형 프로그래밍 등) 패러다임을 지원하는 언어이다.

> 참고 자료 : <a href="https://ko.wikipedia.org/wiki/%EB%8B%A4%EC%A4%91_%ED%8C%A8%EB%9F%AC%EB%8B%A4%EC%9E%84_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%96%B8%EC%96%B4">다중 패러다임 프로그래밍 언어 (위키백과)</a>,  
> <a href="https://velog.io/@j-_-eun125/자바스크립트는-다중-패러다임-프로그래밍-언어">자바스크립트는 다중 패러다임 프로그래밍 언어 (개인 블로그)</a>,

<br/><br/>

### JavaScript는 싱글 스레드(Single-Threaded) 언어이다.

- 스레드(Thread)란, 어떤 프로그램 내에서 실행되는 흐름의 최소 단위이다.

* 프로세스(process)란, 컴퓨터에서 실행 중인 프로그램을 말한다.

* 하나의 프로세스는 여러 개의 스레드로 구성할 수 있으며, 스레드는 프로세스의 실행 단위라고도 할 수 있다.

* 싱글 스레드란 하나의 프로세스에서 하나의 스레드만 실행하는 것을 의미한다. 하나의 레지스터와 스택으로만 표현할 수 있다.

* JavaScript는 메인 스레드인 이벤트 루프가 싱글 스레드이기 때문에 JavaScript는 싱글 스레드를 기반으로 동작하는 언어이다.

> 참고 자료 : <a href="https://namu.wiki/w/%EC%8A%A4%EB%A0%88%EB%93%9C">스레드 (나무위키)</a>,  
> <a href="https://ko.wikipedia.org/wiki/%EC%8A%A4%EB%A0%88%EB%93%9C_(%EC%BB%B4%ED%93%A8%ED%8C%85)">스레드 (컴퓨팅) (위키백과)</a>,  
> 그 외 다수의 개인 블로그 게시글 (너무 많아서 열거 불가)

<br/><br/>

### JavaScript의 표준은 ECMAScript 언어 사양 (ECMA-262) 및 ECMAScript 국제화 API 사양 (ECMA-402)이다.
