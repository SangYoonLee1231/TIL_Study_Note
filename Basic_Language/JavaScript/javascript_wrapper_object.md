# JavaScript - Wapper Object(래퍼 객체)

<br/>

<!-- <br/>

### 목차

- <a href=""></a>

<br/><br/> -->

## 자바스크립트의 래퍼 객체(Wrapper Object)란?

- 자바스크립트에는 Primitive 타입(원시 타입)과 Object 타입(객체 타입)이 존재한다.

  - Primitive 타입은 **불변성 및 값 자체를 저장**한다는 특징이 있는 반면,

  - Object 타입은 **가변성 및 참조(reference)를 저장**한다는 특징을 가진다.

- Primitive 타입은 Object 타입이 아니므로 본래 메서드나 프로퍼티를 가지고 있지 않다. 그러나 JS에서는 `string`, `number`, `boolean` 타입의 값을 마치 Object처럼 다룰 수 있다고 한다.

- 이것이 가능한 이유는 자바스크립트 엔진이 **래퍼 객체(Wrapper Object)를 자동으로 생성하기 때문**이다.

<br/><br/>

## 래퍼 객체(Wrapper Object)의 동작 방식

- `string`, `number`, `boolean` 이 3가지 타입은 각각 `String`, `Number`, `Boolean` 래퍼 객체가 존재한다.

- 이 객체들은 원시 값과 관련된 메스드 및 프로퍼티를 제공하는 역할을 한다. 아래 코드를 살펴보자.

```js
let str = "hello";

console.log(str.length); // 5
console.log(str.toUpperCase()); // "HELLO"
```

- **문자열은 원시 타입인데 어떻게 .length나 .toUpperCase()를 호출할 수 있을까?**  
  👉 **바로 래퍼 객체가 자동으로 생성되기 때문이다.**

<br/>

### Boolean과 Number의 래퍼 객체 예시

```js
let bool1 = true;
console.log(bool1.toString()); // "true"

let num1 = 42;
console.log(num1.toFixed(2)); // "42.00"
```

<br/><br/>

## 래퍼 객체의 내부 동작 과정

- 자바스크립트 엔진은 다음과 같은 과정을 거칩니다.

```js
let str = "hello"; // (1) Primitive 값 생성

console.log(str.length);
// (2) 내부적으로 new String(str) 생성 → 임시 객체 생성
// (3) 임시 객체에서 .length 값을 참조
// (4) 임시 객체가 메모리에서 제거됨 (Garbage Collection)
```

- **즉, 래퍼 객체는 일시적으로 생성되었다가 바로 사라진다.**

<br/>

- 이를 코드로 표현하면 아래처럼 동작한다.

```js
let tempStr = new String("hello"); // (2) String 객체 생성
let length = tempStr.length; // (3) length 프로퍼티 참조
tempStr = null; // (4) 객체 제거 (Garbage Collection)
```

- 하지만 우리는 위 과정을 직접 수행할 필요 없이, 자바스크립트가 알아서 처리해준다.

<br/><br/>

## 명시적으로 래퍼 객체를 생성해주기 (권장 X)

- 자바스크립트는 래퍼 객체를 자동으로 생성하지만, 개발자가 명시적으로 생성할 수도 있다.

```js
let str1 = "hello"; // 원시 타입
let str2 = new String("hello"); // String 객체

console.log(typeof str1); // "string"
console.log(typeof str2); // "object"

console.log(str1 === str2); // false (타입이 다름)
console.log(str1 == str2); // true  (값이 같아서)
```

<br/>

- **하지만 명시적 래퍼 객체 사용은 권장되지 않는다.**

  - 원시 값이 객체로 변환되면서 예상치 못한 동작이 발생할 수 있음
  - `===` 비교에서 타입이 다르게 평가됨
  - 메모리 사용량 증가 및 퍼포먼스 저하 가능

- 대부분의 경우 자동으로 생성되는 래퍼 객체를 활용하면 충분하다.

<br/>

- 또한, 명시적 래퍼 객체의 생성은 **예상치 못한 동작**을 발생시킬 수 있다.

```js
let bool2 = new Boolean(false);

if (bool2) {
  console.log("참으로 평가됨!"); // 실행됨 😱
}

// `new Boolean(false)`는 false가 아니라 객체이므로 Truthy 값이 됨
```

<br/>

#### 결론: 자바스크립트가 제공하는 자동 래핑 기능만 활용하고, 직접 new 키워드로 래퍼 객체를 만드는 것은 피하는 것이 좋다!

<br/>
