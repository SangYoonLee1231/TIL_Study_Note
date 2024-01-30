# C++ - 자주 쓰이는 메소드 정리

<br/>

### 목차

- <a href="">입출력 관련 메소드</a>
<!-- - <a href=""></a> -->

<br/><br/>

## 입출력 관련 메소드

- <code>cout << fixed;</code>  
  <code>cout.precision(n);</code> : 소수점 아래 n번째 까지 출력하기 (반올림 반영)

- <code>cin.get();</code> : 표준 입력 버퍼에서 문자를 하나 받아온다.

  - 입력 받아도 쓰일 곳이 없는 문자를 처리할 때 쓰기 좋다.

- <code>getline(cin, 받고자 하는 문자열)</code> : 문자열 한 줄을 모두 입력받는다. (띄어쓰기도 포함)

<br/>

## 문자열 관련 메소드

문자열 관련 메소드는 헤더에 <code>#include \<string></code>를 작성해야 사용할 수 있다.

- <code>문자열.length()</code> : 문자열의 길이 구하기

- <code>문자열.substr(시작 index, 길이)</code> : 시작 index부터 해당 길이만큼 문자열 자르기

- <code>stoi(숫자로 구성된 문자열)</code> : 문자열을 숫자로 형변환

- <code>to_string(숫자)</code> : 숫자를 문자열로 형변환

<br/>

## 기타 메소드

- <code>sizeof(배열)/sizeof(배열 원소의 자료형)</code> : 원소의 개수 구하기
