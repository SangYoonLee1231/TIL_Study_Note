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

  box 요소의 경계가 부모 box 요소의 경계가 일치하면, 이 두 margin이 하나로 취급되는 현상

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

* border은 box(block)뿐만 아니라 inline 태그에도 적용된다.

```css
div {
  border: 1px solid black;
  /* border: 너비 스타일 색깔 */
}
span {
  border: 2px dotted blue;
}
```

* border은 여러 속성이 존재하나 대부분 이쁘지 아니하므로 거의 한 종류만 쓴다.