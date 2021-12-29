# CSS - Display 속성 : Block과 Inline

<br/>

>  참고 강의 : 「<a href="https://nomadcoders.co/kokoa-clone" target="_blank">노마드 코더 - 코코아톡 클론코딩</a>」

<br/>

## ✨ Block VS Inline

* <strong>Block</strong>

  * Block 태그 옆엔 다른 요소가 올 수 <strong>없다.</strong>  

  * Block은 높이(height)와 너비(width)를 <strong>가진다.</strong>  

  * Block은 <strong>Box</strong>이고, 3가지 중요한 특징을 가진다.  

    :   <strong>margin, border, padding</strong>  

  *  ex) \<div>, \<p>, \<address>
  
* <strong>Inline</strong>

  * Inline 태그 옆에 다른 요소들이 올 수 <strong>있다.</strong>   

  * Inline은 높이(height)와 너비(width)를 <strong>가질 수 없다.</strong>  

  * ex) \<span>, \<a>, \<img>

<br/>

## Box가 갖는 속성 1 : 《 margin 》

* margin은 <strong>box의 경계(border)의 바깥에 있는 영역</strong>이다.

```css
div {
    margin: 20px; /* 전방향 */
    margin: 20px 15px; /* 상하 좌우 */
    margin: 20px 5px 15px 10px; /* 상 우 하 좌 */

    margin-top: 20px;
    margin-bottom: 15px;
    margin-right: 5px;
    margin-left: 10px;
}
```

* <strong>user agent stylesheet</strong> :  

  브라우저가 기본적으로 부여한 style 속성  
  ex) body { margin : 8px; }

* <strong>Collasping Margins</strong> :  

  box 요소의 경계가 부모 box 요소의 경계와 일치하면, 이 두 margin이 하나로 취급되는 현상

<br/>

## Box가 갖는 속성 2 : 《 padding 》

* padding은 <strong>box의 경계(border)로부터 안쪽에 있는 영역</strong>이다.

```css
div {
    padding: 20px; /* 전방향 */
    padding: 20px 15px; /* 상하 좌우 */
    padding: 20px 5px 15px 10px; /* 상 우 하 좌 */

    padding-top: 20px;
    padding-bottom: 15px;
    padding-right: 5px;
    padding-left: 10px;

    /* 규칙은 margin과 동일하다. */
}
```

<br/>

## Box가 갖는 속성 3 : 《 border 》

* border은 말 그대로 박스의 '<strong>경계</strong>'이다.

* border은 <strong>box(block)뿐만 아니라 inline 태그에도 적용</strong>된다.

```css
div {
  border: 1px solid black;
  /* border: 너비 스타일 색깔 */
}
span {
  border: 2px dotted blue;
}
```

* border은 여러 속성이 존재하나 대부분 이쁘지 않으므로 거의 한 종류만 쓴다.

<br/>

## 또 하나의 Display 속성 : Inline Block

* Inline Block은 높이와 너비를 가지는 동시에, 바로 옆에 다른 요소가 올 수 있는 display 속성이다.
```css
div {
  display: inline-block;
}
```

* 그러나 <strong>많은 문제점</strong>을 가지고 있으므로 사용을 지양한다.

* Inline Block의 문제점

  * 정해진 형식이 없고 inline Block 요소들 사이에 의미불명한 빈 공간이 생긴다.

  * <strong>반응형 디자인(Responsive Design)을 자원하지 않는다.

    * 창 크기가 달라지면 영향을 받는다.</strong>