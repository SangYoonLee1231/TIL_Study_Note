# CSS - Flexbox

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

## Flexbox란

* Element(요소)들의 배치를 바꾸는 쉬운 방법으로, 2차원 레이아웃에서 잘 작동한다.

* display의 속성 중 하나이다.

```css
body {
    display: flex;
}
```

<br/>

## ✨ Flexbox 사용 시 유의할 점

* 반드시 flex를 적용하고자 하는 Element(요소)의 <strong>부모 Element에 display: flex를 명시</strong>해야 한다.

    * display: flex  

      == 이 박스를 flex 컨테이너로 만든다.  

      == 이 box '<strong>안</strong>'에 들어있는 자식 Element들을 이제부터 flex로 관리한다.

    * <strong>자식 Element에 display: flex 작성 금지</strong> (처음에 하기 쉬운 실수)

```css
body {
    display: flex;
}
/* body의 '자식 요소'들에 flex가 적용된다. */
```

<br/>

## 주축(main axis)과 교차축(cross axis)

* flex 컨테이너는 2개의 축을 가지고 있다.

<img src="img/main_axis_cross_axis.png">

</br>

* <strong>justify-content</strong>는 <strong>주축(main axis)에 적용</strong>하는 flex의 속성이다.

* <strong>align-items</strong>는 <strong>교차축(cross axis)에 적용</strong>하는 flex의 속성이다.

```css
body {
    display: flex;

    justify-content: center;

    justify-content: flex-end;  /* 축의 제일 끝쪽으로 정렬 배치*/
    justify-content: flex-start;  /* 축의 제일 앞쪽으로 정렬 배치*/

    justify-content: space-evenly;  /*빈 공간을 같은 크기로 나누어서 중앙 정렬 배치*/
    justify-content: space-around;
    justify-content: space-between;

    justify-content: stretch;
}
/* justify-content(또는 align-items)의 다양한 속성값 */
```

<br/>

## Flex Direction

* flex-direction : 주축의 방향을 지정하는 속성


    * <strong>row</strong> 〈Default 값〉

    <img src="img/row.png">

    <br/>

    * <strong>column</strong>

    <img src="img/column.png">

    <br/>

        * row와 column은 두 축의 방향은 모두 같으나 주축과 교차축이 서로 반대이다.

    * <strong>row-reverse</strong>

    <img src="img/row-reverse.png">

    <br/>

    * <strong>column-reverse</strong>

    <img src="img/column-reverse.png">

    <br/>
    
        * 뒤에 -reverse가 붙으면 교차축은 그대로 두고, 교차축을 중심으로 주축만 선대칭하면 된다.

<br/>

## 유용한 자료

<a href="https://flexboxfroggy.com/#ko">Flex에 익숙해질 수 있는 유익한 게임 : FLEXBOX FROGGY</a>