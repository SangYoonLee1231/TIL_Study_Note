# Display 속성 : Block과 Inline

>  참고 강의 : 「<a href="https://nomadcoders.co/kokoa-clone" target="_blank">노마드 코더 - 코코아톡 클론코딩</a>」

<br/>

## ✨ Block VS Inline

* Block

  * block 태그 옆엔 다른 요소가 <strong>올 수 없다.</strong>  

  * block은 <strong>높이(height)와 너비(width)를 가진다.</strong>  

  * <strong>Block은 Box</strong>이고, 3가지 중요한 특징을 가진다.  
  :   <strong>margin, border, padding</strong>  

  *  ex) \<div>, \<p>, \<address>
  
* Inline

  * inline 태그 옆에 다른 요소들이 <strong>올 수 있다.</strong>   

  * inline은 <strong>높이(height)와 너비(width)를 가질 수 없다.</strong>  

  * ex) \<span>, \<a>, \<image>

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

* user agent stylesheet :  
브라우저가 기본적으로 부여한 style 속성  
  ex) body { margin : 8px; }

* Collasping Margins :  
box 요소의 경계가 부모 box 요소의 경계가 일치하면, 이 두 margin이 하나로 취급되는 현상