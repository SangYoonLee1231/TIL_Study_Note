# CSS - Flexbox 기초

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

## Flexbox란

* Element(요소)들의 배치를 바꾸는 유용한 방법으로, 2차원 레이아웃에서 잘 작동한다.

* flex는 display의 속성값 중 하나이다.

```css
body {
    display: flex;
}
```

* 어떤 HTML Element(요소)에 CSS 코드 display: flex를 명시하면, 해당 요소는 flex 컨테이너가 되고, 내부 요소는 flex 아이템이 된다.

<br/>

## ✨ Flexbox 사용 시 유의할 점

* 반드시 flex로 관리하려는 Element(요소)의 <strong>부모 Element에 display: flex를 명시</strong>해야 한다.

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

* 단, 자식의 자식 Element 또한 flex로 관리하려면, 자식의 Element에도 display: flex를 명시해야 한다.  

  (부모만 display: flex를 명시한다고 해서 손자까지 영향이 미치진 않는다.)

<br/>

## 주축(main axis)과 교차축(cross axis)

* flex 컨테이너는 2개의 축을 가지고 있다.

    * <strong>주축 (main axis)</strong>

    * <strong>교차축 (cross axis)</strong>

<img src="img/main_axis_cross_axis.png">

</br>

* <strong>justify-content</strong>는 <strong>주축(main axis)에 적용</strong>하는 flex의 속성이다.

* <strong>align-items</strong>는 <strong>교차축(cross axis)에 적용</strong>하는 flex의 속성이다.

```css
body {
    display: flex;

    justify-content: center;

    justify-content: flex-end;  /* 축의 끝점으로 정렬 배치*/
    justify-content: flex-start;  /* 축의 시작점으로 정렬 배치*/

    justify-content: space-evenly;  /*빈 공간을 같은 크기로 나누어서 중앙 정렬 배치*/
    justify-content: space-around;
    justify-content: space-between;

    justify-content: stretch;
}
/* justify-content(또는 align-items)의 다양한 속성값 */
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="img/flex_space.jpg" width="450px">

<br/>

## Flex Direction

* <strong>flex-direction</strong> : 주축의 방향을 지정하는 속성


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
    
        * 뒤에 -reverse가 붙으면 교차축 방향은 그대로 두고, 교차축을 중심으로 주축 방향만 선대칭하면 된다.

<br/>

## Flex Wrap

* flex-wrap 속성은 flex 아이템을 한 줄에 강제로 배치할 지, 아님 여러 줄에 나누어 배치할 지를 결정하는 속성이다.

```css
body {
    flex-wrap: wrap;
}
```  

* flex-wrap 속성값

    * <strong>wrap</strong> : flex 아이템을 여러 줄로 나누어 배치.  
    화면 크가가 줄어들면 flex 아이템을 순서대로 다음 줄로 보낸다. 〈Default 값〉

    * <strong>nowrap</strong> : flex 아이템을 한 줄에 강제로 배치.  
    화면 크기가 줄어들면 flex 아이템의 원래 크기를 (비율에 맞게) 줄여서라도 강제로 배치시킨다.

    * <strong>wrap-reverse</strong> : wrap과 마찬가지로 flex 아이템을 여러 줄로 나누어 배치하되, 요소 배치 순서의 기준이 정반대로 뒤집힌다.  
    (문자의 표기 방향과 정반대 방향)

    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="img/flex_wrap2.jpg" width="600px">

<br/>

## 유용한 자료

<a href="https://flexboxfroggy.com/#ko">Flex에 익숙해질 수 있는 유익한 게임 : FLEXBOX FROGGY</a>