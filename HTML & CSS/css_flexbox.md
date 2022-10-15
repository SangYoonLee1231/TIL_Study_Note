# CSS - Display 속성 : Flexbox

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고 +
>
> 「<a href="https://nomadcoders.co/css-layout-masterclass" target="_blank">노마드 코더 - CSS Layout 마스터클래스</a>」

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#flexbox-%EC%86%8C%EA%B0%9C">Flexbox 소개</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#-flexbox-%EC%82%AC%EC%9A%A9-%EC%8B%9C-%EC%9C%A0%EC%9D%98%ED%95%A0-%EC%A0%90">Flexbox 사용 시 유의할 점</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#-flex-direction">Flex Direction</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#%EC%A3%BC%EC%B6%95main-axis%EA%B3%BC-%EA%B5%90%EC%B0%A8%EC%B6%95cross-axis">주축(main axis)과 교차축(cross axis)</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#justify-content"><code>justify-content</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#align-items"><code>align-items</code></a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#flex-wrap">Flex Wrap</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#%EC%98%A4%EC%A7%81-%EC%9E%90%EC%8B%9D-%EC%9A%94%EC%86%8C%EC%97%90%EB%A7%8C-%EC%A4%84-%EC%88%98-%EC%9E%88%EB%8A%94-flexbox-%EC%86%8D%EC%84%B1">오직 자식 요소에만 줄 수 있는 Flexbox 속성</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#align-self"><code>align-self</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#order"><code>order</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#flex-grow"><code>flex-grow</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#flex-shrink"><code>flex-shrink</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#flex-basis"><code>flex-basis</code></a>

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md#%EC%9C%A0%EC%9A%A9%ED%95%9C-%EC%9E%90%EB%A3%8C">유용한 자료 (FLEXBOX FROGGY)</a>

<br/><br/>

## Flexbox 소개

- <code>flex</code>는 <code>display</code>의 속성값 중 하나이다.

- Element(요소)들의 배치를 바꾸는 유용한 방법으로, 2차원 레이아웃에서 잘 작동한다.

  ```css
  body {
    display: flex;
  }
  ```

<br/>

- Flexbox는 <strong>반응형 웹 디자인</strong>을 위해 등장하였다.

  - 반응형웹 디자인(responsive web design, RWD)이란 하나의 웹사이트에서 PC, 스마트폰, 태블릿 PC 등 접속하는 디스플레이의 종류에 따라 화면의 크기가 자동으로 변하도록 만든 웹페이지 접근 기법을 말한다.

<br/>

- 어떤 HTML Element(요소)에 CSS 코드 <code>display: flex</code>를 명시하면, 해당 요소는 <strong>flex 컨테이너</strong>가 되고, 내부 요소는 <strong>flex 아이템</strong>이 된다.

<br/><br/>

## ✨ Flexbox 사용 시 유의할 점

- 반드시 <code>flex</code>로 관리하려는 Element(요소)의 <strong>부모 Element에</strong> <code>display: flex</code><strong>를 명시</strong>해야 한다.

  - <code>display: flex</code>

    == 이 박스를 flex 컨테이너로 만든다.

    == 이 box '<strong>안</strong>'에 들어있는 자식 Element들을 이제부터 <code>flex</code>로 관리한다.

  - <strong>자식 Element에는 <code>display: flex</code>를 작성해선 안 된다.</strong> (처음에 하기 쉬운 실수)

    ```css
    body {
      display: flex;
    }
    /* body의 '자식 요소'들에 flex가 적용된다. */
    ```

<br/>

- 단, 자식의 자식 Element 또한 <code>flex</code>로 관리하려면, 자식의 Element에도 <code>display: flex</code>를 명시해야 한다.

  (부모만 <code>display: flex</code>를 명시한다고 해서 손자까지 영향이 미치진 않는다.)

<br/><br/>

## ✨ Flex Direction

- <strong><code>flex-direction</code></strong> : 메인이 되는 축(주축)의 방향을 지정하는 속성

  - <strong><code>row</code></strong> 〈Default 값〉

    <img src="img/row.png">

    <br/>

  - <strong><code>column</code></strong>

    <img src="img/column.png">

    <br/>

        * row와 column은 두 축의 방향은 모두 같으나 주축과 교차축이 서로 반대이다.

    <br/>

  - <strong><code>row-reverse</code></strong>

    <img src="img/row-reverse.png">

    <br/>

  - <strong><code>column-reverse</code></strong>

    <img src="img/column-reverse.png">

    <br/>

        * 뒤에 -reverse가 붙으면 교차축 방향은 그대로 두고, 교차축을 기준으로 주축 방향만 선대칭하면 된다.

<br/><br/>

## 주축(main axis)과 교차축(cross axis)

- flex 컨테이너는 2개의 축을 가지고 있다.

  - <strong>주축 (main axis)</strong>

  - <strong>교차축 (cross axis)</strong>

    <img src="img/main_axis_cross_axis.png">

</br>

### <strong><code>justify-content</code></strong>

- <strong>주축(main axis)에 적용</strong>하는 <code>flex</code>의 속성이다.

### <strong><code>align-items</code></strong>

- <strong>교차축(cross axis)에 적용</strong>하는 <code>flex</code>의 속성이다.

<br/>

- 사용 예시

  ```css
  body {
    display: flex;

    justify-content: center;

    justify-content: flex-end; /* 축의 끝점으로 정렬 배치*/
    justify-content: flex-start; /* 축의 시작점으로 정렬 배치*/

    justify-content: space-evenly; /*빈 공간을 같은 크기로 나누어서 중앙 정렬 배치*/
    justify-content: space-around;
    justify-content: space-between;

    justify-content: stretch;
  }
  /* justify-content(또는 align-items)의 다양한 속성값 */
  ```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="img/flex_space.jpg" width="550px">

<br/><br/>

## Flex Wrap

- <strong><code>flex-wrap</code></strong> 속성은 flex 아이템을 한 줄에 강제로 배치할 지, 아님 여러 줄에 나누어 배치할 지를 결정하는 속성이다.

  ```css
  body {
    flex-wrap: wrap;
  }
  ```

<br/>

### <code>flex-wrap</code> 속성값

- <strong><code>nowrap</code> 〈Default 값〉 </strong>: <strong>flex 아이템을 한 줄에 강제로 배치.</strong>

  화면 크기가 줄어들면, flex 아이템의 원래 크기를 (비율에 맞게) 줄여서라도 강제로 배치시킨다.

  (아이템의 크기가 <strong>왜곡될 수 있다.</strong>)

- <strong><code>wrap</code></strong> : <strong>flex 아이템들을 여러 줄로 나누어 배치.</strong>

  화면 크기가 줄어들면, flex 아이템을 순서대로 다음 줄로 보낸다.

  (아이템의 크기가 <strong>왜곡되지 않는다.</strong>)

- <strong><code>wrap-reverse</code></strong> : wrap과 마찬가지로 flex 아이템을 여러 줄로 나누어 배치하되, <strong>요소 배치 순서의 기준이 정반대로 뒤집힌다.</strong>

  (문자의 표기 방향과 정반대 방향)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="img/flex_wrap2.jpg" width="550px">

<br/>

### <code>align-content</code>

- <code>align-content</code>는 line 간의 빈 공간 (줄 나눔 공간) 을 수정할 때 쓰이는 속성이다.

- 이 속성은 다음의 값들을 인자로 받는다.

  - <code>flex-start</code>: 여러 줄들을 컨테이너의 꼭대기에 정렬한다.
  - <code>flex-end</code>: 여러 줄들을 컨테이너의 바닥에 정렬한다.
  - <code>center</code>: 여러 줄들을 세로선 상의 가운데에 정렬한다.
  - <code>space-between</code>: 여러 줄들 사이에 동일한 간격을 둔다.
  - <code>space-around</code>: 여러 줄들 주위에 동일한 간격을 둔다.
  - <code>stretch</code>: 여러 줄들을 컨테이너에 맞도록 늘립니다.

<br/>

### <code>flex-flow</code>

- <code>flex-direction</code>와 <code>flex-wrap</code> 자주 같이 사용되기 때문에, <code>flex-flow</code>가 이를 대신할 수 있다.

- 이 속성은 공백문자를 이용하여 두 속성의 값들을 인자로 받는다.

  ```css
  .father {
    display: flex;
    flex-flow: row wrap;
  }
  ```

<br/><br/>

## 오직 자식 요소에만 줄 수 있는 Flexbox 속성

### <strong><code>align-self</code></strong>

- <strong><code>align-items</code>와 동일한 기능</strong>을 수행하는 Flexbox 속성이다.

- 하지만 Flex Container의 <strong>자식 요소</strong>에만 줄 수 있는 속성이라는 점에서 <code>align-items</code>와 차이가 있다.

- <code>align-self</code>는 하나의 자식 요소에 부여하는 것도 가능하고, 여러 요소에 부여하는 것도 가능하다.

<br/>

### <strong><code>order</code></strong>

- Flex Container의 <strong>자식 요소의 순서를 부여</strong>하는 Flexbox 속성이다.

- 모든 자식 요소의 기본 order 값은 <code>0</code>이다.
  따라서 특정 자식 요소에 양수 order 값을 부여하면 가장 끝으로 옮겨진다.

- HTML을 조작할 수 없는 상황일 때 유용하다.

<br/>

### <strong><code>flex-grow</code></strong>

- Flexbox 주위 빈 공간이 생길 때, element의 행동을 정의한다.

- 화면의 크기가 커지면, Flexbox가 (남는 빈 공간을 차지하여) 얼마나 더 커지게 되는지 설정할 수 있다.

  - default 값 = <code>0</code>

<br/>

### <strong><code>flex-shrink</code></strong>

- Flexbox가 쥐어짜질 때, element의 행동을 정의한다.

- <code>flex-wrap: no-wrap</code>인 상태에서 화면 크기가 작아지면, 해당 Box가 얼마나 더 빠르게 수축하는 지 설정할 수 있다.

  - default 값 = <code>1</code>

  - 값이 증가할수록 화면이 작아질 때 해당 Box가 더 빠르게 수축한다.

<br/>

### <strong><code>flex-basis</code></strong>

- 해당 자식 요소에게 초기 사이즈를 지정할 때 쓰는 속성이다.

- 사이즈가 높이인지 너비인지는 주축의 방향에 따라 달라진다.

  - <code>flex-direction: row</code>이면, 주축이 가로축이므로 <code>flex-basis</code>는 너비(<code>width</code>)가 된다.

  - 반대로 <code>flex-direction: column</code>이면, 주축이 세로축이므로 <code>flex-basis</code>는 높이(<code>height</code>)가 된다.

- (자주 쓰이진 않는다고 한다.)

<br/><br/>

## 유용한 자료

- <a href="https://flexboxfroggy.com/#ko">Flex에 익숙해질 수 있는 유익한 게임 : FLEXBOX FROGGY</a>

<br/>

> 사진 출처 : https://webdesign.tutsplus.com/tutorials/a-comprehensive-guide-to-flexbox-alignment--cms-30183, https://studiomeal.com/archives/197, https://velog.io/@dev-leesaerom/%EA%B9%80%EC%9D%98-CSS%EB%8A%94-%EC%9E%AC%EB%B0%8C%EB%8B%A4-6-Flexbox
