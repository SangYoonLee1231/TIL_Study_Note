# CSS - 속성 선택자, 가상 클래스 선택자

<br/>

>  참고 자료 : 《<a href="https://github.com/SangYoonLee1231/TIL/blob/main/HTML%20%26%20CSS/html_basic_concept.md">HTML의 기본</a>》 페이지 참고

<br/>

## 속성 선택자

* 특정 속성이나 특정 속성값을 가지는 Element를 선택할 수 있는 선택자이다.

```css
input[type="password"] {...}
/* type 속성의 속성값이 password인 input 태그에 적용 */

input[placeholder="username"] {...}
/* placeholder 속성의 속성값이 username인 input 태그에 적용 */

input[placeholder~="name"] {...}
/* placeholder 속성의 속성값에 name을 포함하는 input 태그에 적용 (단, name의 앞뒤에 공백이 반드시 있어야 한다.) */

input[placeholder*="username"] {...}
/*placeholder 속성의 속성값에 name을 포함하는 input 태그에 적용 (단, name의 앞뒤에 공백이 없어도 된다.) */
```

## 가상 클래스 선택자(Pseudo-class Selector)란

* 선택자를 작성하는 3가지 기본 방법

    * 태그의 이름을 쓰는 방법

    * 점(.)을 쓰고 클래스 이름을 쓰는 방법

    * 해시 기호(#)를 쓰고 id값을 쓰는 방법

* 이 방법 외에 다른 도구로 좀 더 세부적으로 Element를 선택하는 방법이 있다.

### 상태 (States) 가상 클래스 선택자

<br/>

```css
div:first-child {...} /* div들 중 첫번째 요소만 적용 */
div:last-child {...} /* div들 중 마지막 요소만 적용 */
```

```css
input:required {...} /* required 속성을 가진 input에 적용 */
input:optional {...} /* required 속성을 가지지 않는 input에 적용 */
```
