# Chapter 9. CSS Next Level

<br/>

## 1. Float

- 떠오르다. 자식이 부모로부터

  → **margin을 없에버리다**

- 자식 요소의 width값 자체가 바뀌는 것이 아니라, 부모 요소의 width값 만큼 margin이 생기는 것이다.

- 가로 배치를 하고 싶은 요소에 전부 float를 선언하면 요소들이 겹치쳐지 않고 가로 배치를 성공적으로 할 수 있다.

  ```css
  div.pink div.blue {
    width: 50px;
    height: 50px;
    float: left;
  }
  ```

<br/><br/>

## 2. Clear

- Float와 밀접한 연관

- 생기게 된 배경: 페이지 Layout을 짜다 보면 꼭 생기는 콘텐츠 범람 현상을 해결하기 위함

- div 요소의 가로 배치를 위해 float 적용, float로 없어진 margin 영역에 대응하기 위해 clear 적용

- clear은 float로 없어진 margin 영역을 무시하지 올라가지 않도록 처리해주는 역할을 한다.

  ```css
  div.pink {
    float: left;
  }
  div.blue {
    clear: left;
  }
  ```

<br/>

#### Clearflx

- Clearflx는 clear이라는 속성으로 Layout을 바로잡는 기법이다.

  ```css
  (범람을 막고 싶은 요소)::after {
    content: " ";
    display: block;
    clear: both; /* lett, right 둘 다 막음 */
  }
  ```

<br/><br/>

## 3. Flex

- 가로 배치 문제를 쉽게 해결해줌

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_flexbox.md">내용 보러 가기</a>

<br/><br/>

## 4. Position

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_position.md">내용 보러 가기</a>

<br/><br/>

## 5. Grid

- 열이 12개이고 행이 무한한 바둑판

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/css_grid.md">내용 보러 가기</a>
