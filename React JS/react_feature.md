# React JS 특징 + Virtual DOM

> 참고 자료 : <a href="https://nomadcoders.co/react-for-beginners">노마드 코더 - React JS로 영화 웹서비스 만들기</a>, 부트캠프 학습 자료

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_feature.md#react-js%EC%9D%98-%EB%8C%80%ED%91%9C%EC%A0%81%EC%9D%B8-%ED%8A%B9%EC%A7%95-2%EA%B0%80%EC%A7%80">React JS의 대표적인 특징 2가지</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_feature.md#1-%EC%84%A0%EC%96%B8%ED%98%95">1. 선언형</a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_feature.md#2-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-%EA%B8%B0%EB%B0%98">2. 컴포넌트 기반</a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_feature.md#virtual-dom">Virtual DOM</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/React%20JS/react_feature.md#react-js%EC%9D%98-%EC%9E%A5%EC%A0%90">React JS의 장점</a>

<br/><br/>

## React JS의 대표적인 특징 2가지

### 1. 선언형

#### 절차적 vs 선언적

- <strong>절적(명령형) 프로그래밍</strong>

  - 원하는 결과를 만들기 위한 <strong>절차(How)</strong>에 중점을 두는 프로그래밍 방식

  - 자바스크립트에서 직접 DOM을 조작하는 방식

  - 모든 과정을 일일이 기술해야 하므로 생산성이 저하될 수 있다.

- <strong>선언적 프로그래밍</strong> ☑

  - 원하는 결과가 <strong>무엇(What)</strong>인지 <strong>선언</strong>하는 형태로 프로그래밍 하는 방식

  - 자바스크립트에서 DOM 조작은 React에 위임

  - 컴퓨터는 절차적으로 동작하기에 결국 모든 명령을 다 절차적으로 해주어야 하지만, 개발을 하는 개발자는 (최대한 절차적인 부분은 감추가나 위임하고) <strong>선언적인 부분에만 집중</strong>하게 하는 방식이 선언적인 프로그래밍 방식이다.

<br/>

### 2. 컴포넌트 기반

#### 컴포넌트 (Component) 란?

- 컴퓨터 과학에서 컴포넌트란?

  - 독립적이고, 재사용할 수 있는 소프트웨어 구성

- 프론트엔드에서 컴포넌트란?

  - <strong>독립적이고, 재사용할 수 있는 UI 단위</strong>

<br/>

- 로고믈록을 조립해서 큰 성을 만들듯이, 작은 UI를 조합해서 큰 UI를 구성할 수 있다.

<br/>

#### 컴포넌트 단위 개발의 이점

1. 컴포넌트를 한 번 생성하면 여러 곳에서 재사용할 수 있다. ➡️ 유지보수에 용이

2. 다른 컴포넌트를 포함할 수 있다. ➡️ 컴포넌트를 조합해서 큰 컴포넌트를 만들 수 있다.

3. UI가 어떻게 구성되어 있는지 파악하기 쉽다. ➡️ 가독성 향상, 유지보수에 용이

<br/><br/><br/>

## Virtual DOM

- Virtual DOM은 React가 DOM을 효율적으로 조작하기 위해 내부적으로 가지고 있는 "DOM의 미니어쳐"이다.

- 리엑트가 UI를 자동으로 업데이트 하는 과정을 좀 더 효율적으로 하기 위한 개념이다.

<br/>

- 매 DOM 조작마다 브라우저에서 일어나는 일은 내가 포스팅한 <a href="">'웹 브라우저 동작 원리' 중 렌더링 프로세스 부분</a>를 참고하자.

- 위와 같은 과정이 매번 일어난다면 브라우저가 처리해야 할 연산량이 늘어나므로, React는 Virtual DOM을 통해 필요한 DOM 조작만을 계산한 뒤 이를 실제 DOM에 한 번에 반영하는 방식으로 작업을 수행한다.

<br/>

- Virtual DOM에 대한 좀 더 자세한 내용은 <a href="https://velog.io/@yesbb/virtual-dom의-성능이-더-좋은이유">해당 포스트를</a> 참고하자.

<br/><br/><br/>

## React JS의 장점

- 다른 프레임워크 (혹은 라이브러리)에 비해 문법이 자바스크립트를 그대로 사용하기 때문에, React를 사용하는 것만으로도 JS 문법과 훨씬 더 친숙해질 수 있다.

- Meta(구 Facebook)에서 지속적으로 관리해주는 라이브러리로, 사용자가 많아 생태계가 잘 활성화되어 있다. (현재 FE에서 가장 많이 사용)

  - 이에 따라 React에 대해 개발자들이 고민하고 도출한 많은 해결방법이 존재한다.

  - 또한 React 기반으로 개발된 기술이나 서비스가 많이 존재하고 제공된다.

  - 이는 곧 React를 이용한 개발의 생산성이 높아진다는 것을 의마한다.

- UI를 구축하는 기능만을 담당하므로, 유연하게 확장해서 사용할 수 있는 기술이다. (ex : React Native)
