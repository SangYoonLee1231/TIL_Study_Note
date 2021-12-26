# CSS - ID와 Class

<br/>

>  참고 강의 : 「<a href="https://nomadcoders.co/kokoa-clone" target="_blank">노마드 코더 - 코코아톡 클론코딩</a>」

<br/>

## ID

* id는 <strong>고유한 값</strong>으로 한 요소당 하나만 가질 수 있다.

* id명을 통해 <strong>특정 요소를 직접</strong> 가리킬 수 있다.

* CSS 코드에서 선택자로 id를 쓸 때, 값 앞에 '<strong>#</strong>'을 꼭 붙여야 한다.

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