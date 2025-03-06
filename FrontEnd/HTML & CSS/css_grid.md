# CSS - Display 속성 : Grid

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고 +
>
> 「<a href="https://nomadcoders.co/css-layout-masterclass" target="_blank">노마드 코더 - CSS Layout 마스터클래스</a>」

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_grid.md#grid-%EC%86%8C%EA%B0%9C">Grid 소개</a>
- <a href="">Grid의 기본적인 속성</a>

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_grid.md#grid-template-columns"><code>grid-template-columns</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_grid.md#grid-template-rows"><code>grid-template-rows</code></a>
  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_grid.md#gap-column-gap-row-gap"><code>gap</code> (<code>column-gap</code>, <code>row-gap</code>)</a>

- <a href=""></a>
- <a href=""></a>

<br/><br/>

## Grid 소개

- <code>grid</code>는 <code>display</code>의 속성값 중 하나이다.

- Element(요소)들을 <strong>격자(grid)</strong> 형태로 배치하고자 할 때 유용한 방법이다.

<br/>

- <code>grid</code>도 Flexbox와 마찬가지로, 관리하려는 Element(요소)의 <strong>부모 Element에</strong> <code>display: grid</code><strong>를 명시</strong>한다.

  ```css
  .father {
    display: grid;
  }
  ```

<br/><br/>

## Grid의 기본적인 속성

### <code>grid-template-columns</code>

- 세로줄을 어떻게 나눌 것인지 설정하는 속성

- <code>grid-template-columns: 20px 30px 40px 50px</code>

  - 세로 4줄을 생성하되, 첫 번째는 <code>20px</code>, 두 번째는 <code>30px</code>, 세 번째는 <code>40px</code>, 네 번째는 <code>50px</code>으로 설정한다.

  - 다섯 번째 자식 요소가 있다면, 그 다음 줄로 넘어가서 배치된다.

<br/>

### <code>grid-template-rows</code>

- 가로줄를 어떻게 나눌 것인지 설정하는 속성

- <code>grid-template-row: 20px 20px 20px</code>

  - 가로 3줄을 생성하되, 전부 <code>20px</code>로 설정한다.

<br/>

### <code>gap</code> (<code>column-gap</code>, <code>row-gap</code>)

- 각 요소 간의 간격을 설정하는 속성이다.

  - <code>gap</code> : 가로줄, 세로줄 간의 간격을 모두 설정

  - <code>column-gap</code> : 세로줄 간의 간격을 설정

  - <code>row-gap</code> : 가로줄 간의 간격을 설정

<br/>

### 참고 코드

```html
<div class="grid-container">
  <div class="grid-item">1</div>
  <div class="grid-item">2</div>
  <div class="grid-item">3</div>
  <div class="grid-item">4</div>
  <div class="grid-item">5</div>
  <div class="grid-item">6</div>
  <div class="grid-item">7</div>
  <div class="grid-item">8</div>
  <div class="grid-item">9</div>
</div>
```

```css
/* Part 1 */
.grid-container {
  display: grid;
  grid-template-columns: [first] 100px [second] 200px [third] 50px [fourth];
  grid-template-rows: [first] 200px [second] 100px [third] 50px [fourth];
  row-gap: 10px;
  column-gap: 20px;
}

.grid-item {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: tomato;
  color: white;
}

.grid-item:last-child {
  /* grid-column-start: 2;
  grid-column-end: -1; */
  /* grid-column: second / fourth; */
  grid-column: first / span 2;
  background-color: khaki;
}

.grid-item:first-child {
  /* grid-row-start: 1;
  grid-row-end: 3; */
  grid-row: 1 / -1;
}
```

<br/>

```html
<div class="grid-container-2">
  <header>Header</header>
  <section>Section</section>
  <aside>Aside</aside>
  <footer>Footer</footer>
</div>
```

```css
/* Part 2 */
.grid-container-2 {
  margin-top: 50px;
  display: grid;
  height: 50vh;

  /* grid-template-columns: 1fr 1fr 1fr 1fr;
  grid-template-rows: 1fr 1fr 1fr;
  grid-template-areas:
    "header header header header"
    "main main . sidebar"
    "footer footer footer footer"; */

  grid-template:
    "header header header header" 1fr
    "main main . sidebar" 1fr
    "footer footer footer footer" 1fr / 1fr 1fr 1fr 1fr;
}
header {
  grid-area: header;
  background-color: #f1c40f;
}

main {
  grid-area: main;
  background-color: #3498db;
}

sidebar {
  grid-area: sidebar;
  background-color: #2ecc71;
}

footer {
  grid-area: footer;
  background-color: #e74c3c;
}
```

<br/>

```html
<div class="grid-container-3">
  <div class="grid-item-3">1</div>
  <div class="grid-item-3">2</div>
  <div class="grid-item-3">3</div>
  <div class="grid-item-3">4</div>
  <div class="grid-item-3">5</div>
  <div class="grid-item-3">6</div>
  <div class="grid-item-3">7</div>
  <div class="grid-item-3">8</div>
  <div class="grid-item-3">9</div>
  <div class="grid-item-3">10</div>
</div>
```

```css
/* Part 3 */
.grid-container-3 {
  margin-top: 50px;
  display: grid;
  gap: 10px;
  min-height: 50vh;
  grid-template-columns: repeat(2, 1fr); /* repeat(반복 횟수, 반복할 값) */
  grid-template-rows: repeat(2, 1fr);
  grid-auto-flow: column; /* 새로운 행이 추가되면 어디에 생성할 것인가, 행 또는 열 */
  grid-auto-rows: 1fr; /* 새로운 행이 추가되면 어떻게 처리할 것인가 */
  grid-auto-columns: 1fr; /* 새로운 열이 추가되면 어떻게 처리할 것인가 */
  /* 동적 데이터를 다룰 때 유용 */
}

.grid-item-3 {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: tomato;
  color: white;
  font-size: 28px;
}
```

<br/>

```html
<div class="grid-container-3">
  <div class="grid-item-3">1</div>
  <div class="grid-item-3">2</div>
  <div class="grid-item-3">3</div>
  <div class="grid-item-3">4</div>
  <div class="grid-item-3">5</div>
  <div class="grid-item-3">6</div>
  <div class="grid-item-3">7</div>
  <div class="grid-item-3">8</div>
  <div class="grid-item-3">9</div>
  <div class="grid-item-3">10</div>
</div>
```

```css
/* Part 4 */
.grid-container-3 {
  justify-items: stretch; /* 아이템이 가로로 최대한 늘어남 */
  align-items: stretch; /* 아이템이 세로로 최대한 늘어남 */
  justify-items: start; /* 아이템이 가로로 왼쪽에 붙음 */
  align-items: start; /* 아이템이 세로로 위에 붙음 */
  justify-items: end; /* 아이템이 가로로 오른쪽에 붙음 */
  align-items: end; /* 아이템이 세로로 아래에 붙음 */
  justify-items: center; /* 아이템이 가로로 중앙에 붙음 */
  align-items: center; /* 아이템이 세로로 중앙에 붙음 */
  /* */
  place-items: center; /* justify-items, align-items를 한 번에 설정 */
}

.grid-item-3 {
  /* width: 50px; */
  height: 50px;
}

.grid-item-3:nth-child(6) {
  background-color: teal;

  /* 한 개의 내용물만 이동시킴 */
  justify-self: center;
  align-self: center;

  place-self: center center; /* justify-self, align-self를 한 번에 설정 */
}
```

<br/>

```html
<div class="grid-container-3">
  <div class="grid-item-3">1</div>
  <div class="grid-item-3">2</div>
  <div class="grid-item-3">3</div>
  <div class="grid-item-3">4</div>
  <div class="grid-item-3">5</div>
  <div class="grid-item-3">6</div>
  <div class="grid-item-3">7</div>
  <div class="grid-item-3">8</div>
  <div class="grid-item-3">9</div>
  <div class="grid-item-3">10</div>
</div>
```

```css
/* Part 5 */
.grid-container-3 {
  align-content: center; /* 셀 전체를 세로로 중앙에 정렬 */
  justify-content: center; /* 셀 전체를 가로로 중앙에 정렬 */
  /* */
  justify-content: space-around; /* 셀 전체를 가로로 여백을 동일하게 설정 */
  justify-content: space-between; /* 셀 전체를 가로로 양 끝에 붙이고 사이 여백을 동일하게 설정 */
  justify-content: space-evenly; /* 셀 전체를 가로로 여백을 동일하게 설정 */
  /* */
  place-content: center center; /* align-content, justify-content를 한 번에 설정 */
  /* Grid Container에 남는 공간이 있어야만 사용 가능! */
}
```

<br/>

```html
<div class="grid-container-4">
  <div class="grid-item-3">1</div>
  <div class="grid-item-3">2</div>
  <div class="grid-item-3">3</div>
</div>
```

```css
/* Part 6 */
.grid-container-4 {
  display: grid;
  gap: 10px;
  height: 100vh;
  /* */
  grid-template-columns: 1fr max-content 1fr; /* max-content: 내용물의 최대 너비 (내부 콘텐츠에 따라 달라짐) */
  grid-template-rows: 1fr min-content 1fr; /* min-content: 내용물의 최소 너비 (내부 콘텐츠에 따라 달라짐) */
  /* */
  grid-template-columns: 1fr minmax(250px, 1fr) 1fr; /* minmax(최소값, 최대값): 최소값보다 작으면 최소값, 최대값보다 크면 최대값 */
  grid-template-rows: repeat(3, minmax(300px, 1fr));
}
```

<br/>

```html
<div class="grid-container-4">
  <div class="grid-item-3">1</div>
  <div class="grid-item-3">2</div>
  <div class="grid-item-3">3</div>
</div>
```

```css
/* Part 7 */
.grid-container-4 {
  /* 반응형 그리드 만들기 */
  /* auto-fill: 가능한 많은 행을 채움, auto-fit: 필요한 만큼만 행을 채움 */
  grid-template-rows: repeat(auto-fill, minmax(300px, 1fr));
  grid-template-rows: repeat(auto-fit, minmax(300px, 1fr));
}
```

<br/>
