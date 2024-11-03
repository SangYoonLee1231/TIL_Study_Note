# 타입스크립트 기본

## 타입스크킙트 초기 세팅

- `npm init`

- `sudo npm install -g typescript`

- `npm i @type/node`

- `tsconfig.json` 파일 만들어 설정

  ```json
  {
    "compilerOptions": {
      "target": "ESNext", // 변환되는 JS의 버전 설정
      "module": "ESNext", // 변환되는 JS의 모듈 설정
      "outDir": "dist", // 컴파일러 결과 생성된 JS 파일의 저장 위치 설정
      "strict": true, // 엄격한 타입 검사 모드 설정
      "moduleDetection": "force" // 각 파일을 독립된 모듈로 인식
    },
    "include": ["src"] // 컴파일 범위 설정
  }
  ```

- `tsc` 명령어를 통해 ts 파일이 잘 컴파일 되는지 확인

<br/><br/>

## 기본 타입

- TS가 자체적으로 제공하는 타입, 내장 타입이라고도 부름

- 타입스크립트가 기본적으로 제공하는 타입

    <img src="img/type.png" />

<br/><br/>

## 원시 타입

- 하나의 값만 저장하는 타입, Primitive Type

- number, string, boolean, null, undefined

- 타입 주석 (Type Annotation): 콜론과 함께 어떤 변수의 타입을 명시해주는 코드 부분

- **number**

  ```ts
  // number
  let num1: number = 123;
  let num2: number = -123;
  let num3: number = 0.123;
  let num4: number = -0.123;
  let num5: number = Infinity;
  let num6: number = -Infinity;
  let num7: number = NaN;
  num1 = "hello"; // 에러!
  num1.toUpperCase(); // 에러!
  num1.toFixed();
  ```

- **string**

  ```ts
  // string
  let str1: string = "hello";
  let str2: string = `hello ${num1}`;
  str1.toFixed(); // 에러!
  str1.toUpperCase();
  ```

- **boolean**

  ```ts
  // boolean
  let bool1: boolean = true;
  let bool2: boolean = false;
  ```

- **null**, **undefined**

  ```ts
  // null
  let null1: null = null;
  ```

  ```ts
  // undefined
  let unde1: undefined = undefined;
  ```

- null에 대한 엄격한 모드를 풀어 숫자 변수에 초기값으로 null 할당하기

  ```json
  {
    "compilerOptions": {
      "target": "ESNext",
      "module": "ESNext",
      "outDir": "dist",
      "strict": true,
      "strictNullChecks": false, // 엄격한 null 검사
      "moduleDetection": "force"
    },
    "include": ["src"]
  }
  ```

  - `strict` 옵션은 `strictNullChecks`의 상위 옵션이다.

  ```ts
  // strictNullChecks
  let numA: number = null;
  ```

- **리터럴 타입**

  - 값 그 자체가 타입이 되는 타입 (리터럴이 값이라는 뜻)

  - 나중에 복합적인 타입들을 만들 때 굉장히 유용하게 사용된다고 한다.

  ```ts
  // 리터럴 타입
  let numB: 10 = 10;
  numB = 12; // 에러!

  let strA: "hello" = "hello";
  let boolA: true = false; // 에러!
  ```

<br/><br/>

## 배열과 튜플

- **배열**

  ```ts
  // 배열
  let numArr: number[] = [1, 2, 3];

  let strArr: string[] = ["hello", "hi", "annyoung"];

  let boolArr: Array<boolean> = [true, false, true]; // <>을 제네릭 문법이라 부름 (잘 쓰지 않음)
  ```

  ```ts
  // 배열에 들어가는 요소들의 타입이 다양할 경우
  let multiArr: (number | string)[] = [1, "hello"]; // 유니온 타입
  ```

  ```ts
  // 다차원 배열의 타입을 정의하는 방법
  let doubleArr: number[][] = [
    [1, 2, 3],
    [4, 5],
  ];
  ```

- **튜플**

  ```ts
  // 튜플 (TS에서만 제공)
  let tup1: [number, number] = [1, 2];
  // tup1 = [1, 2, 3];
  // tup1 = ["1", "2"];

  let tup2: [number, string, boolean] = [1, "2", true];
  // 튜플은 사실 배열이다.

  tup1.push(1);
  tup1.pop();
  tup1.pop();
  tup1.pop();
  // 배열 메소드를 사용할 때는 길이 제한이 발생하지 않는다.
  // 그렇기 때문에 각별히 주의해서 메서드를 사용해야 한다.

  // 튜플이 유용한 경우 예시
  const users = [
    ["이아무개", 1],
    ["김아무개", 2],
    ["박아무개", 3],
    [4, "윤아무개"], // 잘못
  ];

  const usersCopy: [string, number][] = [
    ["이아무개", 1],
    ["김아무개", 2],
    ["박아무개", 3],
    //[4, "윤아무개"], // 잘못된 요소에 오류 발생!
  ];
  // 인덱스 위치에 따라 넣어야 할 값이 정해져 있을 때 튜플을 이용하면 오류를 방지할 수 있다.
  ```

<br/><br/>

## 객체

```ts
let user: object = {
  id: 1,
  name: "이상윤",
};

user.id; // 에러!
```

- TS에 object라는 이 타입은 그냥 이 값이 객체인 것 외에는 아무런 정보도 없는 타입이기 때문에

- 이렇게 정의를 하면 이 객체의 프로퍼티나 메소드가 뭐가 있는지 이 타입은 알 수가 없다.

<br/>

```tsx
let userCopy: {
  id: number;
  name: string;
} = {
  id: 1,
  name: "이상윤",
};

userCopy.id;
```

- 객체의 타입을 정의할 때는 객체의 모든 프로퍼티들의 타입까지 구조적으로 다 정의하는 방식인 **객체 리터럴 타입**을 사용한다.

<br/>

```tsx
let dog: {
  name: string;
  color: string;
} = {
  name: "바둑이",
  color: "Brown",
};
```

- TS는 객체의 구조를 기준으로 타입을 정의한다. → 구조적 타입 시스템 (프로퍼티를 기준으로 타입을 결정한다, 프로퍼티 기반 타입 시스템)

- 이름만으로 타입을 정의: 명목적 타입 시스템

<br/>

- `?`: 프로퍼티가 있어도 되고 없어도 된다. 선택적 프로퍼티(옵셔널 프로퍼티)라 부름

```tsx
let user2: {
  id?: number; // 선택적 프로퍼티
  name: string;
} = {
  name: "홍길동",
};
```

<br/>

```tsx
let config: {
  readonly apiKey: string;
} = {
  apiKey: "MY API KEY",
};

//config.apiKey = "hacked"; // 에러!
```

- readonly 키워드를 붙여주면 프로퍼티 값을 바꾸는 것을 막아준다.

<br/><br/>

## 타입 별칭

- 타입을 정의하는 코드가 중복될 수 있음을 방지하고자, 타입을 변수처럼 선언하는 문법

```tsx
let user: {
  id: number;
  name: string;
  nickname: string;
  birth: string;
  bio: string;
  location: string;
} = {
  id: 1,
  name: "이상윤",
  nickname: "syl",
  birth: "1998.01.23",
  bio: "안녕하세요",
  location: "서울시",
};

let user2: {
  id: number;
  name: string;
  nickname: string;
  birth: string;
  bio: string;
  location: string;
} = {
  id: 2,
  name: "이상윤",
  nickname: "syl",
  birth: "1998.01.23",
  bio: "안녕하세요",
  location: "서울시",
};
```

- 위의 예시에서 user들의 타입을 정의하는 코드가 중복되므로, 타입 별칭을 이용하여 아래와 같이 코드를 줄일 수 있다.

```tsx
// 타입 별칭 만들기
type User = {
  id: number;
  name: string;
  nickname: string;
  birth: string;
  bio: string;
  location: string;
};

let userCopy: User = {
  id: 1,
  name: "이상윤",
  nickname: "syl",
  birth: "1998.01.23",
  bio: "안녕하세요",
  location: "서울시",
};

let user2Copy: User = {
  id: 2,
  name: "이상윤",
  nickname: "syl",
  birth: "1998.01.23",
  bio: "안녕하세요",
  location: "서울시",
};
```

<br/>

- 타입 별칭을 사용할 땐 같은 스코프 내에서는 타입의 이름이 중복되지 않도록 해주어야 한다.

- 타입 별칭 코드를 컴파일하여 JS로 변환하면 이 코드는 제거된다.

<br/><br/>

## 인덱스 시그니쳐

- 객체 타입 정의 시 key와 value의 규칙을 기준으로 정의할 수 있는 문법

- 아주 유연한 타입 정의가 가능하다.

- 객체에 정의해야 할 프로퍼티가 너무 많을 때, key와 value의 타입이 어떤 규칙을 가질 때 유용하다.

```tsx
// key와 value의 규칙을 기준으로 객체의 타입을 정의할 수 있는 문법
type CountryCodes = {
  [key: string]: string;
};

let countryCodes: CountryCodes = {
  Korea: "ko",
  UnitedStates: "us",
  UnitedKingdom: "us",
};

type CountryNumberCodes = {
  [key: string]: number;
  Korea: number;
};

let countryNumberCodes: CountryNumberCodes = {
  Korea: 410,
  UnitedState: 840,
  UnitedKindom: 826,
};
```

- 주의점

  - 객체의 프로퍼티가 아예 없더라도 타입 규칙을 위반하진 않으므로 에러가 발생하지 않는다.
  - 그렇기에, 꼭 있어야 할 프로퍼티는 반드시 타입 정의 시 적어주자.
  - 다만 이런 경우에는 추가적인 프로퍼티의 Value 타입이 인덱스 시그니처의 Value 타입과 일치하거나 호환해야 한다.

<br/><br/>

## 기타 타입

### any

- 특정 변수의 타입을 확실히 모를 때 사용할 수 있는 타입

- 어떠한 타입의 변수도 담을 수 있다.

```tsx
let anyVar: any = 10;
anyVar = "hello";

anyVar = true;
anyVar = {};
anyVar = () => {};

anyVar.toUpperCase();
anyVar.tofixed();

let num: number = 10;
num = anyVar;
```

- 다만, any 타입을 사용한다는 것은 TS의 이점을 모두 포기하는 것이므로, 가능한 사용하지 않는 것이 좋다.

<br/>

### unknown

- any처럼 모든 값을 다 할당받을 순 있지만, any와 다르게 그 반대는 허용되지 않는다.

- unknown 타입은 any 타입보다는 안전하다.

- unknown은 안전함을 추구하는 any 자료형인 느낌. any 쓰면 TS 쓰는 이유가 없다시피 하니까, 그냥 안전한 의미로 unknown을 쓰면 될 것 같은 느낌이다.

```ts
let unknownVar: unknown;
unknownVar = "";
unknownVar = 1;
unknownVar = () => {};

if (typeof unknownVar == "number") {
  num = unknownVar;
}
```

<br/>

### void

- void는 '공허'라는 뜻. 아무것도 없음을 의미하는 타입

```ts
function func1(): string {
  return "hello";
}

function func2(): void {
  console.log("hello");
}
```

- 리턴값이 없는 함수의 리턴값 타입을 설정할 때 void를 쓴다.

- undefined나 null로 설정한다면 함수에서 return문이 반드시 필요하게 되므로, 그래서 void 타입을 사용하는 것이다.

- return 하더라도 반환 값이 없는 경우(`return;`)또한 void를 사용한다.

- void 타입으로 정의한 변수에는 어떠한 값도 담을 수 없다. 오직 undefined만 담을 수 있다.

- 다만 `tsconfig.js`의 `strictNullChecks`를 끄면 void 타입 변수에 null을 할당할 수 있다.

<br/>

### never

- 존재하지 않는 불가능한 타입

```ts
function func3(): never {
  while (true) {}
}
```

- 함수가 절대로 정상적으로 종료될 수 없어서, 함수의 반환값 자체가 있는 것이 모순인 상활일 때 never 타입이 필요하다.

```ts
function func4(): never {
  throw new Error();
}
```

- 실행되면 바로 프로그램이 중지되므로, never로 정의하는 것이 바람직하다.

- any 타입의 변수도 never 타입의 변수에는 절대 담을 수 없다.

- never은 다음과 같은 경우에도 활용할 수 있다. → <a href="https://www.pumpkiinbell.com/blog/typescript/exhaustive-checking">Exhaustiveness Checking</a>

<br/><br/>
