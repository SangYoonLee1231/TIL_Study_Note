# CSS - Transition

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

## 

```css
a {
    color: wheat;
    border-radius: 10px;
    background-color: tomato;
    text-decoration: none;
    padding: 3px 5px;
    font-size: 50px;

    transition: all 0.5s cubic-bezier(1, 0, 0, 1);
}

a:hover {
    color: tomato;
    border-radius: 25px;
    background-color: wheat;
}
```
```html
<body>
    <a href="#">Go home</a>
</body>
```