# CSS - ID와 Class

<br/>

>  참고 강의 : 「<a href="https://nomadcoders.co/kokoa-clone" target="_blank">노마드 코더 - 코코아톡 클론코딩</a>」

<br/>

## ID

* id는 <strong>고유한 값</strong>으로 한 요소당 하나만 가질 수 있다.

* id명을 통해 <strong>특정 요소를 직접</strong> 가리킬 수 있다.

* CSS 코드에서 선택자로 id를 쓸 때, 값 앞에 '<strong>#</strong>'을 붙여서 쓴다.

```css
#first {
    padding: 20px 15px;
}
#second {
    background-color: tomato;
}
```
```html
<div id="first">
    <div id="second"></div>
</div>
```

* 여러 같은 html 태그를 생성하였을 때, id를 이용하여 각각을 구분할 수 있고, 서로 다른 속성을 적용시킬 수 있다.

* CSS 코드의 id명은 HTML 코드에서 썼던 id명과 동일해야 한다.

</br>

## Class

* class는 id와 달리, <strong>여러 요소에 같은 이름으로</strong> 부여할 수 있다.

* class명을 통해 <strong>여러 요소를 동시에</strong> 가리킬 수 있다.

* CSS 코드에서 선택자로 class를 쓸 때, 값 앞에 '<strong>.</strong>'을 붙여쓴다.

* 하나의 HTML 요소에 여러 종류의 class가 쓰일 수 있다.

```css
.btn {
    width: 50px;
    height: 25px;
    border-radius: 5px;
}
.tomato {
    background-color: tomato;
}
.potato {
    background-color: teal;
}
```
```html
<span class="btn tomato">HELLO!</span>
<span class="btn potato">HELLO!</span>
```

* class 특징을 이용하여 <strong>반복되는 코드를 하나로 묶음으로써</strong> 코드 길이를 줄일 수 있다.

  (위의 btn class처럼)