# React JS - Hook

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>, 부트캠프 학습 자료

<br/>

### 목차

- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/><br/>

## Hook이란?

- Hook은 클래스 컴포넌트에서만 사용할 수 있었던 <strong>상태 관리</strong>와 <strong>라이프 사이클 관리 기능</strong>을 함수 컴포넌트에서도 사용할 수 있도록 연동해주는 함수를 의미한다.

- 미리 만들어 둔 함수를 가져와서 사용을 해 주는 것이기 때문에 Hook이라는 이름을 사용한다.

- Hook의 모음을 Hooks라 한다.

<br/><br/>

## Hook의 등장 배경

- 기존엔 클래스 컴포넌트만을 사용하여 컴포넌트를 생성하였는데, 함수 컴포넌트의 장점으로 인해 이를 사용하고자 하는 니즈가 점점 많아지게 되었다.

  - 함수 컴포넌트의 장점 : 선언하기 편리함, 직관적, 메모리 자원을 덜 사용함

- 이로 인해 클래스 컴포넌트에서만 가능했던 기능을 함수 컴포넌트에서도 사용하고자 Hook이 등장하였다.

<br/><br/>

## Hook의 특징

- 함수 컴포넌트에서<strong>만</strong> 사용 가능하다.

- Hook의 이름은 반드시 <strong><code>use-</code></strong>로 시작한다.

  따라서 함수 이름을 보고 Hook임을 짐작할 수 있다.

- <strong>내장 Hook</strong>이 존재한다. (<code>useState</code>, <code>useEffect</code>)

  이런 Hook들은 외부 라이브러리 설치 없이 사용할 수 있다.

- 직접 Hook을 만들어 사용할 수도 있다. 이를 <strong>Custom Hook</strong>이라 한다.

<br/><br/>

## Hook의 사용 규칙

- Hook은 함수 컴포넌트 혹은 Custom Hook 안에서만 호출할 수 있다.

  그 외의 장소에서는 Hook을 사용할 수 없다.

- Hook은 함수 컴포넌트 내의 최상위(at the top level) 에서만 호출해야 한다.

  반복문, 조건문 등 중첩 함수 내에서는 Hook을 호출할 수 없다.
