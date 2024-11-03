# 함수와 타입

## 함수 타입 정의 방법

- 함수를 설명하는 가장 좋은 방법은 '어떤 타입의 매개변수를 받고, 어떤 타입의 결과값을 변환하는지'를 이야기하는 것이다.

```ts
function func(a: number, b: number): number {
  return a + b;
}

// 화살표 함수의 타입을 정의하는 방법
const add = (a: number, b: number): number => a + b;
```

<br/>

- 함수의 매개변수

```ts
function introduce(name = "이상윤", age: number, tall?: number) {
  console.log(`name: ${name}`);
  if (typeof tall === "number") {
    console.log(`tall: ${tall + 10}`);
  }
} // 매개 변수에 초기값을 지정해주면, 해당값의 타입으로 자동 추론해준다.

introduce("이상윤", 27, 176);
introduce("이상윤", 27);
```

- 선택적 매개변수는 undefined 값도 올 수 있으므로, 함수 내부에서 해당 값에 연산이 필요할 땐 타입 가드를 해주어야 한다.

- 선택적 매개변수는 필수 매개변수들 앞에 오면 안된다.

<br/>

- Rest Parameter의 타입 정의

  ```ts
  function getSum(...rest: number[]) {
    let sum = 0;
    rest.forEach((it) => {
      return (sum += it);
    });
  }

  getSum(1, 2, 3);
  getSum(1, 2, 3, 4, 5);
  ```

<br/><br/>

## 함수 타입 표현식과 호출 시그니쳐

- 함수의 타입을 별도로 정의하는 문법들

### 함수 타입 표현식 (Function Type Expression)

```ts
type Add = (a: number, b: number) => number;

const add: Add = (a, b) => a + b;
```

- 이 문법을 호출 시그니쳐 또는 함수 시그니쳐라고도 부르지만, 공식 문서에 적혀있는 정식 명칙은 '함수 타입 표현식'이다.

<br/>

- 중복되는 함수 타입 표현식을 굉장히 깔끔하게 고칠 수 있는 방법

  ```ts
  type Operation = (a: number, b: number) => number;

  const add1: Operation = (a, b) => a - b;
  const sub: Operation = (a, b) => a - b;
  const multiply: Operation = (a, b) => a - b;
  const divide: Operation = (a, b) => a - b;

  const add1Copy: (a: number, b: number) => number = (a, b) => a + b;
  ```

<br/>

### 호츨 시그니쳐

```ts
type Operation2 = {
  (a: number, b: number): number;
};

const add2: Operation2 = (a, b) => a - b;
const sub2: Operation2 = (a, b) => a - b;
const multiply2: Operation2 = (a, b) => a - b;
const divide2: Operation2 = (a, b) => a - b;
```

- 함수의 타입을 정의하는데 이렇게 중괄호를 열어서 마치 객체 타입을 정의하듯이 하는 이유는, 사실 JavaScript의 함수도 객체이기 때문이다.

<br/>

- 하이브리드 타입

  ```ts
  type Operation3 = {
    (a: number, b: number): number;
    name: string; // 하이브리드 타입
  };
  ```

<br/><br/>

## 함수 타입의 호환성

- 특정 함수 타입을 다른 함수 타입으로 취급해도 괜찮은가를 판단하는 것

- 함수 타입의 호환성을 판단하려면 다음 두 가지를 체크해봐야 한다.

  - 반환값의 타입이 호환되는가

  - 매개변수의 타입이 호환되는가

<br/>

### 1. 반환값의 타입이 호환되는가

```ts
type A = () => number;
type B = () => 10;

let a: A = () => 10;
let b: B = () => 10;

a = b; // 하용 (반환값 업캐스팅)
// b = a; // 허용 안됨 (반환값 다운캐스팅)
```

<br/>

### 2. 매개변수의 타입이 호환되는가

#### Case 1) 매개변수의 개수가 같을 때

```ts
type C = (value: number) => void;
type D = (value: 10) => void;

let c: C = (value) => {};
let d: D = (value) => {};

// c = d; // 허용 안됨 (매개변수 업캐스팅)
d = c; // 허용 됨 (매개변수 다운캐스팅)
```

- 매개변수를 기준으로 함수 타입의 호환성을 판단할 때는, 기존과 반대로 업캐스팅 땐 오히려 안되고, 다운캐스팅 땐 된다.

<br/>

- 이렇게 되는 이유를 알아보기 위해 다음 예시를 살펴보자.

```ts
// 매개변수가 객체 타입을 사용하는 예시
type Animal = {
  name: string;
};

type Dog = {
  name: string;
  color: string;
};

let animalFunc = (animal: Animal) => {
  console.log(animal.name);
};

let dogFunc = (dog: Dog) => {
  console.log(dog.color);
};

// animalFunc = dogFunc; // 업캐스팅 (에러)

let testFunc = (animal: Animal) => {
  console.log(animal.name);
  // console.log(animal.color); // color을 할당해줄 수 없다.
};

dogFunc = animalFunc;

let testFunc2 = (animal: Dog) => {
  console.log(animal.name);
};
```

- 프로퍼티가 늘어나면 집합의 범위가 축소되므로 업캐스팅 시 할당할 수 없는 프로퍼티가 생긴다.

<br/>

#### Case 2) 매개변수의 개수가 다를 때

- 전제: 매개변수의 타입이 모두 같아야 함 (안그러면 에러)

```ts
type Func1 = (a: number, b: number) => void;
type Func2 = (a: number) => void;

let func1: Func1 = (a, b) => {};
let func2: Func2 = (a) => {};

func1 = func2;
// func2 = func1; // 매개변수 하나를 할당해줄 수 없다
```

<br/><br/>

## 함수 오버로딩

- 함수의 매개변수의 개수나 타입에 따라 여러가지 버전으로 정의하는 문법

- JS는 지원하지 않고 TS만 지원한다.

```ts
// 오버로드 시그니쳐 (선언식만 써놓은 코드)
function func(a: number): void;
function func(a: number, b: number, c: number): void;

// 구현 시그니쳐 (실제 구현부)
function func(a: number, b?: number, c?: number) {
  if (typeof b === "number" && typeof c === "number") {
    // 매개변수가 3개일 때
    return a + b + c;
  } else {
    // 매개변수가 1개일 때
    return a * 20;
  }
}

func(1);
func(1, 2, 3);
```

<br/><br/>

## 사용자 정의 타입 가드

- 사용자 입맛 대로 타입 가드를 작성하는 방법

```ts
// 에시의 전제: 서로소 유니온 타입 이용 불가 (타입을 바꿀 수 없는 상황)

type Dog = {
  name: string;
  isBark: boolean;
};

type Cat = {
  name: string;
  isScratch: boolean;
};

type Animal = Dog | Cat;

// 안 좋은 방법
function warning(animal: Animal) {
  if ("isBark" in animal) {
    // 강아지
    animal;
  } else if ("isScratch" in animal) {
    // 고양이
  }
}

// 사용자 정의 타입 가드를 사용한 좋은 방법
function isDog(animal: Animal): animal is Dog {
  return (animal as Dog).isBark !== undefined;
  // animal을 Dog 타입으로 단언하고, 그러했을 때 isBark의 유무를 확인
} // animal is Dog: 만일 함수가 true를 반환한다면, animal은 Dog이다.

function isCat(animal: Animal): animal is Cat {
  return (animal as Cat).isScratch !== undefined;
}

function warning2(animal: Animal) {
  if (isDog(animal)) {
    // 강아지
    animal;
  } else if ("isScratch" in animal) {
    // 고양이
  }
}
// 타입스크립트는 우리가 직접 만든 함수의 반환값을 가지고는 타입을 잘 좁혀주지 못한다.
// is 문법을 통해 이를 보완
```

<br/><br/>
