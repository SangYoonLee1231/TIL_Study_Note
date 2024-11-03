# 인터페이스

## 인터페이스

- 타입 별칭과 동일하게 타입의 이름을 지어주는 문법

- 인터페이스의 의미: 상호간에 약속된 규칙

- 타입 문법의 인터페이스: 객체의 형태를 정하는 약속 또는 규칙을 만들어주는 문법

- 또 인터페이스는 **객체의 구조를 정의하는데 특화된 문법**이므로, 타입 별칭에서는 제공하지 않는 상속이나 합침 등의 객체 타입을 다루는 여러가지 특수한 기능들을 제공한다.

<br/>

```ts
interface Person {
  name: string;
  age: number;
}

const person: Person = {
  name: "이상윤",
  age: 27,
};
```

```ts
interface Person2 {
  readonly name: string;
  age?: number;
  sayHi: () => void;
  sayBye(): void;
}
```

<br/>

```ts
type Func = {
  (): void;
};

const personTwo: Person2 = {
  name: "이상윤",
  age: 27,
  sayHi: function () {
    console.log("Hi");
  },
  sayBye: function () {
    console.log("Bye");
  },
};
```

<br/>

- 메서드에 오버로딩을 구현하고 싶으면 호출 시그너쳐를 아래와 같이 사용해주어야 한다.

  ```ts
  interface Person3 {
    readonly name: string;
    age?: number;
    sayHi(): void;
    sayHi(a: number, b: number): void;
  }
  ```

<br/>

- 인터페이스의 타입 별칭과의 차이점

  ```ts
  type Type1 = number | string;
  type Type2 = number & string;

  const personThree: Person3 | number = {
    // ...
  };
  ```

  - 인터페이스에서는 유니온 타입, 인터섹션 타입을 만들 수 없다.

<br/>

- 인터페이스를 정의할 때 이름 앞에 I를 붙여 정의하는 경우가 있다. (헝가리안 표기법))

  ```ts
  interface Iperson {}
  ```

  - 관습적인 방법이지만 논란이 조금 있음
  - 자바스크립트에서는 잘 안쓰는 방식
  - 자바스크립트에서는 파스칼, 카멜, 스네이크 표기법을 보통 쓰는데
  - 인터페이스 하나를 위해서 또 형가리안 표기법을 써야 되냐는 부정적인 의견도 꽤 있다.
  - 이러한 규칙은 팀의 컨벤션을 따라가는 것이 맞다.

<br/><br/>

## 인터페이스 확장

- 타입 별칭에는 없는데 인터페이스에사만 특별히 사용할 수 있는 독특한 기능

```ts
import { SourceOrigin } from "module";

interface Animal {
  name: string;
  age: number;
}

interface Dog {
  name: string;
  age: number;
  isBark: boolean;
}

interface Cat {
  name: string;
  age: number;
  isScratch: boolean;
}

interface Chicken {
  name: string;
  age: number;
  isFly: boolean;
}
```

- 위의 코드에서 name과 age 프로퍼티를 벌써 4번이나 중복해서 정의했다.

- 이는 굉장히 번거롭고 비효율적이다.

<br/>

- 이 때 인터페이스 상속을 통해 중복된 코드를 줄일 수 있다.

```ts
interface Animal {
  name: string;
  age: number;
}

interface DogCopy extends Animal {
  isBark: boolean;
}

interface CatCopy extends Animal {
  isBark: boolean;
}

interface ChickenCopy extends Animal {
  isBark: boolean;
}

const dog: DogCopy = {
  name: "",
  age: 10,
  isBark: true,
};
```

<br/>

- 상속을 받는 인터페이스에서 동일한 프로퍼티의 타입을 다시 정의할 수 있다.

- 다만, 다시 정의하려는 타입이 원본 타입의 서브 타입이어야 한다.

```ts
interface Animal {
  name: string;
  age: number;
}

interface DogCopy2 extends Animal {
  name: "hello";
  isBark: boolean;
}

const dog2: DogCopy2 = {
  name: "hello",
  age: 10,
  isBark: true,
};
```

<br/>

- 타입 별칭도 확장이 가능하다.

```ts
type AnimalCopy = {
  name: string;
  color: string;
};

interface Dog extends AnimalCopy {
  name: string;
  age: number;
  isBark: boolean;
}
```

<br/>

#### 다중 확장

```ts
nterface Dog {
  name: string;
  age: number;
  isBark: boolean;
}

interface Cat {
  name: string;
  age: number;
  isScratch: boolean;
}

interface DogCat extends Dog, Cat {
  name: "";
  color: "";
  isBark: true;
  isScratch: true;
} // 여러 개의 타입을 함께 상속받을 수 있다.
```

<br/><br/>

## 인터페이스 합치기

- 인터페이스는 동일한 이름으로 중복 선언이 가능하다.

- 그 이유는 동일한 이름으로 정의한 인터페이스는 결국 다 합쳐지기 때문이다.

- 이러한 현상을 선언합침(선업머징)이라고 부른다.

```ts
interface Person {
  name: string;
}

interface Person {
  // name: number; // 충돌(타입을 다르게 중복 정의)은 허용하지 않음
  name: string;
  age: number;
}
```

<br/>

#### 모듈 보강

- 인터페이스 합치기는 TS의 모듈 보강 작업을 할 떄 주로 사용한다.

```ts
// 이미 정의된 라이브러리라 가정
interface Lib {
  a: number;
  b: number;
}

// 모듈 보강을 위해 인터페이스 재정의
interface Lib {
  c: string;
}

const lib: Lib = {
  a: 1,
  b: 2,
  c: "hello",
};
```

<br/><br/>
