# CSS - Display 속성 : Grid

<br/>

> 참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

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
