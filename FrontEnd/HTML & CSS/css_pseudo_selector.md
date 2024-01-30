# CSS - 결합자, 속성 선택자, 가상 클래스, 가상 요소

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

### 목차

  - <a href="">결합자 (Combinator)</a>
  - <a href="">속성 선택자</a>
  - <a href="">가상 클래스 (Pseudo-class)</a>
  - <a href="">가상 요소 (Pseudo-elements)</a>
  - <a href="">토막 지식</a>

<br/><br/>

* 선택자의 기본 3가지 종류

    * 태그의 이름을 쓰는 선택자

    * 점<code>.</code>을 쓰고 클래스 이름을 쓰는 선택자

    * 해시 기호<code>#</code>를 쓰고 id값을 쓰는 선택자

* 이 외에, 좀 더 세부적으로 Element를 선택하는 도구(선택자)가 있다.

<br/>

## 결합자 (Combinator)

* 여러 선택자를 결합하여, 더 정밀히 요소를 찾아 가리키는 선택자를 결합자(Combinator)라 한다.

<br/>

* <strong>자손 결합자</strong> : <code>A B</code>

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

* <strong>자식 결합자</strong> : <code>A > B</code>

```css
p > span {
    ...
}
```
    p의 바로 밑 자손 span을 모두 가리킨다.

<br/>

* <strong>인접 형제 결합자</strong> : <code>A + B</code>

```css
p + span {
    ...
}
```
    p 다음에 오는 형제 span 1개만을 가리킨다.

<br/>

* <strong>일반 형제 결합자</strong> : <code>A ~ B</code>

```css
p ~ span {
    ...
}
```
    p의 형제 span을 모두 가리킨다.

<br/><br/>

## 속성 선택자

* 속성 선택자는 지정한 input 태그의 type과 동일한 HTML 요소의 속성(attribute)을 선택자로 지정한다.

* 속성 선택자를 통해 지정한 속성의 속성값을 가진 Element를 가리킬 수 있다.

```css
input[type="password"] {
    ...
}
/* input 태그들 중 type 속성이 password인 모든 태그에 효과를 적용 */
```
```css
input[placeholder="username"] {
    ...
}
/* input 태그들 중 placeholder 속성이 username인 모든 태그에 효과를 적용 */
```
```css
input[placeholder~="name"] {
    ...
}
/* input 태그들 중 placeholder 속성에 name을 '포함'하는 모든 태그에 효과를 적용 (단, name의 앞뒤에 '공백'이 반드시 있어야 한다.) */
```
```css
input[placeholder*="name"] {
    ...
}
/* input 태그들 중 placeholder 속성에 name을 '포함'하는 모든 태그에 효과를 적용 (단, name의 앞뒤에 '공백'이 없어도 된다.) */
```

<br/><br/>

## 가상 클래스 (Pseudo-class)

* ☞ <a href="https://developer.mozilla.org/ko/docs/Web/CSS/Pseudo-classes">공식 문서 바로가기</a>

* 가상 클래스(의사 클래스)는 선택자 뒤에 <code>:</code>을 붙여 추가하는 키워드이다.

* 어떤 요소의 특정 상태에서 발생할 효과를 주기 위해 사용한다.

```css
선택자:가상클래스 { property: value; }
```

* 가상 클래스는 HTML 문서에 실제로 존재하지 않는다. 그래서 '가상'인 것이다.

<br/>

```css
div:first-child {...}  /* div들 중 첫번째 요소만 효과 적용 */

div:last-child {...}  /* div들 중 마지막 요소만 효과 적용 */

span:nth-child(2) {...}  /* span들 중 2번째 요소만 효과 적용 */

span:nth-child(2),
span:nth-child(4) {...}  /* span들 중 2번째 요소와 4번째 요소에 효과 적용 */

span:nth-child(even) {...}  /* span들 중 짝수번째 요소만 효과 적용 */

span:nth-child(3n+1) {...}  /* span들 중 3n+1번째 요소만 효과 적용 (n은 0 이상의 정수) */
```

```css
input:required {...}  /* required 속성을 가진 input에 효과 적용 */

input:optional {...}  /* required 속성을 가지지 않는 input에 효과 적용 */
```

<br/>

* 상태 (States) 가상 클래스 선택자

```css
button:active {...}  /* button을 마우스로 클락했을 때, button에 효과 적용 */

button:hover {...}  /* button에 마우스를 올렸을 때, button에 효과 적용 */

button:focus {...}  /* 키보드나 마우스로 button을 선택했을 때, button에 효과 적용 */

form:focus-within {...}  /* form의 자식 요소 중 하나가 focused 되었을 때, form에 효과 적용 */

a:visited {...}  /* 해당 a 링크가 이미 방문한 사이트일 때, a에 효과 적용 */
```

<br/>

* 상태 (State) 가상 클래스 선택자를 다른 Element와 연계해서 사용할 수도 있다.

```css
form:hover input {...}  /* form이 hover되면, input에 효과를 적용한다. */

form:hover input:focus {...}  /* form이 hover되고, 동시에 input이 focus되면, input에 효과를 적용한다. */
```

<br/><br/>

## 가상 요소 (Pseudo-elements)

* ☞ <a href="https://developer.mozilla.org/ko/docs/Web/CSS/Pseudo-elements">공식 문서 바로가기</a>

* 가상 클래스와 달리 <code>::</code>을 붙여 사용한다.

```css
input::placeholder {...} /* input의 placeholder에 들어길 문자에 스타일 효과를 적용한다. */

p::selection {...} /* 택스트를 드래그 했을 때 효과를 적용한다. */

p::first-letter {...} /* 글의 첫 번째 문자에 효과를 적용한다. (Block 요소 한정) */

p::first-line {...} /* 글의 첫 문장에 효과를 적용한다. (Block 요소 한정) */
```

* 외우지 말고 원리를 이해한 후, 공식 문서를 보거나 검색해서 찾아 쓰자.

<br/>

### 토막 지식

* <code>button</code> 요소 중 <code>background-color</code>(배경색) 같이 어떤 속성 하나를 바꾸면, 지정되어 있던 <code>button</code>의 <code>border</code>의 속성은 사라지게 된다.