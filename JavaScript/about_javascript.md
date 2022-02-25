# JavaScript 소개 (By 공식 문서)

> <a href="https://developer.mozilla.org/ko/docs/Web/JavaScript">JS 공식 문서 - JavaScript 메인 페이지 바로 가기 (MDN Web Docs)</a>

<br/>

### JavaScript는 <strong>just-in-time</strong> 컴파일 프로그래밍 언어이다.

- JIT(just-in time) 컴파일은 프로그램을 만드는 2가지 방식인 인터프리트 방식과 정적 컴파일 방식의 절충안(혼합)이다.

* JIT(just-in time) 컴파일은 실행 시점에서 고수준의 프로그래밍 언어를 저수준의 기계어로 번역한다.

* 이 때, 같은 함수가 여러 번 불려 똑같은 기계어 코드가 생성되는 것을 방지하기 위해, 기계어 코드 생성 시 이를 <strong>캐싱</strong>하는 방식으로 컴파일을 수행한다.

> 참고 자료 : <a href="https://ko.wikipedia.org/wiki/JIT_%EC%BB%B4%ED%8C%8C%EC%9D%BC"> JIT 컴파일 (위키백과)</a>

<br/>

- 캐싱(Caching)은, 속도가 느린 데이터를 캐시(Cache)라고 하는 더 빠른 메모리 영역으로 가자고 와서 읽기, 쓰기와 같은 연산을 수행하는 것을 말한다.

* 이 때, 자주 사용되는, 지역성(locality)을 가진 데이터를 더 빠른 속도를 가진 메모리상 저장하면 CPU가 더욱 빠르게 꺼내서 사용할 수 있다. 이는 성능 개선에도 기여한다.

* (참고) 데이터의 지역성(locality)

  - 공간 지역성 : 한 번 접근한 데이터의 근처에 저장된 다른 데이터가 순서대로 접근할 가능성이 높다.

  - 시간 지역성 : 한 번 접근한 데이터가 가까운 시간 내에 다시 접근할 가능성이 높다.

> 참고 자료 : <a href="https://m.blog.naver.com/complusblog/221204759836">캐싱(Caching)과 버퍼링(Buffering) 그리고 스풀링(Spooling) </a>, <a href="https://literate-t.tistory.com/73">[Cache] 시간 지역성, 공간 지역성 :: 안 주면 훔칩니다</a>

<br/><br/>

### JavaScript는 일급 함수를 지원한다.

- 함수를 마치 변수처럼 다루는 언어를 '일급 함수를 가졌다'고 표현한다.

- 일급 함수를 가진 언에에선 다음이 모두 가능하다.

  - 함수를 다른 함수에 변수처럼 인자로 넘겨줄 수 있다.

  - 함수가 다른 함수를 반환할 수 있다.

  * 함수를 변수에 할당할 수 있다.

* 함수를 어떻게 변수처럼 다루는 지는 아래 공식 문서에 기술된 여러 예시를 통해 알 수 있다.

> 참고 자료 : <a href="https://ko.wikipedia.org/wiki/JIT_%EC%BB%B4%ED%8C%8C%EC%9D%BC"> 일급 함수 (MDN Web Docs)</a>

<br/><br/>

### JavaScript는 웹페이지를 위한 스크립트 언어로 잘 알려져 있지만, 많은 비 브라우저 환경에서도 사용하고 있다.

<br/><br/>

### JavaScript는 프로토타입 기반(prototype-based), 다중 패러다임(multi-paradigm), 단일 스레드(single-threaded), 동적 언어(dynamic language)이다.

<br/><br/>

### JavaScript는 객체지향형, 명령형(imperative), 선언형(declarative) (함수형 프로그래밍 등) 스타일을 지원한다.
