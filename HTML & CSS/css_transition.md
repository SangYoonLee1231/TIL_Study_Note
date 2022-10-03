# CSS - Transition, 애니메이션

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

## Transition 소개

- <code>transition</code>이란 어떤 상태에서 다른 상태로 가는 변화를 애니매이션화 하는 CSS 속성이다.

- 구체적으로, <strong>어떤 요소의 속성이 state에 따라 달라지면, 이 변화를 단번에 일으키지 않고

  애니메이션을 적용하여 서서히 변화시킨다. </strong>

<br/>
    
* <code>transition</code> <strong>속성값 순서</strong>
    
    ［transition 적용 대상 속성］, ［애니메이션 시간］, ［Easing 함수］

```css
a {
  color: wheat;
  border-radius: 10px;
  background-color: tomato;
  text-decoration: none;
  padding: 3px 5px;
  font-size: 50px;

  transition: color 0.5s ease-in-out, border-radius 0.5s ease-in-out;

  /* 전체 속성 지정 ☞ transition: all 0.5s ease-in-out; */
}

a:hover {
  color: tomato;
  border-radius: 25px;
  background-color: wheat;
}
```

```html
<body>
  <a href="#">Go home</a>
</body>
```

- 위 코드에선 [Go home] 링크에 마우스를 올리면 <code>color</code>과 <code>border-radius</code>가 0.5초동안 변하게 된다. (<code>background-color</code>은 바로 변한다)

<br/>

### 주의 사항

- ✨ <code>transition</code> 속성은 <strong>반드시 state가 아닌 root에 작성해야 한다.</strong>

<br/><br/>

## Easing 함수

- <code>transition</code>의 마지막 속성값에 들어가는 함수로, <strong>시간 흐름에 따른 애니메이션 변화 속도를 설정</strong>한다.

- ☞ <a href="https://matthewlein.com/tools/ceaser">Easing 함수에 따른 애니메이션 변화를 직접 눈으로 확인할 수 있는 사이트</a>

- Easing 함수 기본값으로 가지고 있는 것

  - <code>linear</code> : 일정한 속도로 진행

  - <code>ease-in</code> : 점점 가속 진행

  - <code>ease-in-out</code> : 시작은 가속, 끝에서 감속

  - <code>ease-out</code> : 점점 감속 진행

  - <code>ease</code> (default)

<br/>

### cubiz-bezier

- <strong>자신만의 Easing 함수 커브를 설정</strong>할 수 있도록 하는 속성

```css
p {
  transition: all 0.5s cubic-bezier(1, 0, 0, 1);
  /* EaseInOutExpo */
}
```

<br/><br/>

## CSS 애니메이션

- CSS로 애니메이션을 부여하려면 다음과 같은 형태로 CSS 코드를 작성하면 된다.

  ```css
  .div {
    animation: animation-name 3s initial;
  }

  @keyframes animation-name {
    0% {
      opacity: 0;
    }
    50% {
      opacity: 1;
    }
    100% {
      opacity: 0;
    }
  }
  ```
