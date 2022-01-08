# CSS - 속성 선택자, 가상 클래스, 가상 요소

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

## 속성 선택자

* 특정 속성이나 속성값을 가진 Element를 선택할 수 있는 선택자이다.

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

<br/>

## 가상 클래스 (Pseudo-class)

* 가상 클래스는 어떤 요소의 특정한 이벤트마다 적용할 스타일(효과)를 설정하기 위해 사용한다.

* 선택자 뒤에 【:<strong>가상 이벤트</strong>】를 붙인다.

```css
선택자:가상이벤트 { property: value; }
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

<br/>

## 가상 요소 (Pseudo-elements)

<br/>

### 토막 지식

* button 요소 중 background-color(배경색) 같이 어떤 속성 하나를 바꾸면, 지정되어 있던 border의 속성은 사라지게 된다.