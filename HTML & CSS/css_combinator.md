# CSS - 결합자 (Combinator)

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

* 선택자의 기본 3가지 종류

    * 태그의 이름을 쓰는 선택자

    * 점(.)을 쓰고 클래스 이름을 쓰는 선택자

    * 해시 기호(#)를 쓰고 id값을 쓰는 선택자

* 이 외에, 좀 더 세부적으로 Element를 선택하는 도구(선택자)가 있다.

<br/>

## 결합자 (Combinator)

* 여러 선택자를 결합하여, 더 정밀히 요소를 찾아 가리키는 선택자를 결합자(Combinator)라 한다.

<br/>

* <strong>자손 결합자</strong> : [<strong>A B</strong>]

```css
p span {
    ...
}
```
    p 안의 모든 span을 가리킨다.

```css
div p span {
    ...
}
```
    div 안의 모든 p, 그 모든 p 안의 모든 span을 가리킨다.

<br/>

* <strong>자식 결합자</strong> : [<strong>A > B</strong>]

```css
p > span {
    ...
}
```
    p의 바로 밑 자손 span을 모두 가리킨다.

<br/>

* <strong>인접 형제 결합자</strong> : [<strong>A + B</strong>]

```css
p + span {
    ...
}
```
    p 다음에 오는 형제 span 1개만을 가리킨다.

<br/>

* <strong>일반 형제 결합자</strong> : [<strong>A ~ B</strong>]

```css
p ~ span {
    ...
}
```
    p의 형제 span을 모두 가리킨다.

<br/>