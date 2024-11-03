# 타입스크립트 이해하기

## 타입스크립트를 이해한다는 것은?

- 어떤 기준으로 타입을 정의하는지

- 어떤 기준으로 타입간의 관계를 정의하는지

- 어떤 기준으로 타입의 오류를 검사하는지

- 타입스크립트의 구체적인 원리와 동작 방식을 낱낱이 살펴보는 것

<br/>

- 타입스크립트는 문법만 달달 외운다고 실무에 바로 적용할 수 있는 만만한 언어가 아니다.

- 원리와 개념의 뒷받침이 없으면 낯선 상황 앞에서 문제를 해결해나갈 수 없다.

- 따라서 한 번 배울 때 제대로 배워서 JS를 사용했을 때보다 더 안정적이고 좋은 코드를 만들어낼 수 있어야 한다.

<br/><br/>

## 타입은 집합이다

- TS가 말하는 '타입'은 **집합**이다.

- 동일한 속성과 특징을 갖는 여러 개의 값들을 모아둔 집합이다.

- 그리고 예를 들어, number literal Type 집합은 Number Type 집합의 부분 집합이다.

  - 더 큰 타입을 슈퍼 타입(부모 타입), 더 작은 타입을 서브 타입(자식 타입)이라 부른다.

- 이렇듯 TS는 타입들이 서로 집합이고 계층을 이룬다.

<br/>

### 타입 호환성

- 어떤 타입을 다른 타입으로 취급해도 괜찮은 지 판단하는 것을 말한다.

- 예를 들어, Number 리터럴 타입을 Number 타입으로 취급하는 것은 가능하지만, 그 역은 안 된다.

  ```tsx
  let num1: number = 10;
  let num2: 10 = 10;

  num1 = num2; // 가능 - 업 캐스팅
  num2 = num1; // 불가능 (에러) - 다운 캐스팅
  ```

<br/><br/>

## 타입 계층도와 함께 기본타입 살펴보기

- 타입 계층도

    <img src='img/type.png' />

<br/>

- unknown 타입

  ```tsx
  // unknown 타입
  // 모든 타입의 슈퍼 타입, 전체 집합

  function unknownExam() {
    let a: unknown = 1;
    let b: unknown = "hello";
    let c: unknown = true;
    let d: unknown = null;
    let e: unknown = undefined;
    // 업 캐스팅

    let unknownVar: unknown;

    //   let num: number = unknownVar;
    //   let str: string = unknownVar;
    //   let bool: boolean = unknownVar;
    // 다운 캐스팅 (안됨)
  }
  ```

<br/>

- never 타입

  ```tsx
  // never 타입
  // 모든 타입의 서브 타입
  // 수학의 집합으로 보면 공집합 개념

  function neverExam() {
    function neverFunc(): never {
      while (true) {}
    }

    let num: number = neverFunc();
    let str: string = neverFunc();
    let bool: boolean = neverFunc();
    // 업 캐스팅

    //   let never1: never = 10;
    //   let never2: never = "hello";
    //   let never3: never = true;
    // 다운 캐스팅 (에러)
  }
  ```

<br/>

- void 타입

  ```tsx
  // vold 타입
  // void는 undefined의 슈퍼 타입

  function voidExam() {
    function voidFunc(): void {
      console.log("hi");
    }

    let voidVar: void = undefined; // 업 캐스팅

    function voidFunc2(): void {
      console.log("hello");
      return undefined;
    } // 반환값도 업 캐스팅
  }
  ```

<br/>

- any 타입

  ```tsx
  // any 타입
  // 치트키 타입, 타입 계층도를 완벽히 무시
  // 모든 타입의 슈퍼 타입이자, 모든 타입의 서브 타입이기도 함 (never만 예외)

  function anyExam() {
    let unknownVar: unknown;
    let anyVar: any;

    anyVar = unknownVar; // 다운 캐스팅이 가능

    let undefinedVar: undefined;
    undefinedVar = anyVar; // 다운 캐스팅이 가능

    let neverVar: never;
    // neverVar = anyVar; // 네버 타입은 정말 순수한 공집합이므로
    // 네버 타입 변수에는 그 어떤 타입도 다운 캐스팅이 불가능
  }
  ```

<br/><br/>

## 객체 타입의 호환성

- 기본 타입 간의 호한성: 특정 타입을 다른 타입으로 취급해도 괜찮은지 판단

  ```tsx
  let num1: number = 10;
  let num2: 10 = 10;

  num1 = num2;
  ```

<br/>

- 객체 타입 간의 호환성

  ```tsx
  type Animal = {
    name: string;
    color: string;
  };

  type Dog = {
    name: string;
    color: string;
    breed: string;
  };

  let animal: Animal = {
    name: "기린",
    color: "yellow",
  };

  let dog: Dog = {
    name: "돌돌이",
    color: "brown",
    breed: "진돗개",
  };

  animal = dog;
  ```

- 이처럼 객체 타입들도 기본 타입들처럼 서로 슈퍼 타입 관계를 갖는다.

- 객체는 프로퍼티를 기준으로 타입 관계가 정해진다.

  - 추가 프로퍼티 없는 객체가 슈퍼 타입이 된다.

```tsx
type Book = {
  name: string;
  price: number;
};

type ProgrammingBook = {
  name: string;
  price: number;
  skill: string;
};

let book: Book;
let programmingBook: ProgrammingBook = {
  name: "한 입 크기로 잘라먹는 타입스크립트",
  price: 33000,
  skill: "reactjs",
};

book = programmingBook;
```

<br/>

- 초과 프로퍼티 검사: 정의해놓지 않은 프로퍼티를 작성하면 안 되도록 막는 검사

```tsx
let book2: Book = {
  name: "한 입 크기로 잘라먹는 타입스크립트",
  price: 33000,
  // skill: "reactjs",
};
```

- 다만, 초과된 프로퍼티를 가진 객체를 할당하는 것은 가능

```tsx
let book3: Book = programmingBook;

function func(book: Book) {}
func({
  name: "한 입 크기로 잘라먹는 타입스크립트",
  price: 33000,
  // skill: "reactjs", // 이런 경우에도 초과 프포퍼티 검사가 발동
});
func(programmingBook); // 이렇게 변수에 저장한 후 전달해주어야 한다.
```

<br/><br/>

## 대수 타입

- 여러 개의 타입을 합성해서 새롭게 만들어낸 타입

- 합잡합과 교집합 타입이 존재한다.

<br/>

### 합잡합 타입 - Union

```tsx
let a: string | number; // 스트링 넘버 유니온 타입
a = 1;
a = "hello";

let b: string | number | boolean;
b = 1;
b = "hello";
b = true;

let arr: (number | string | boolean)[] = [1, "hello", true];
```

```tsx
// 객체 타입들을 이용해서 유니온 타입 만들기
type Dog = {
  name: string;
  color: string;
};

type Person = {
  name: string;
  language: string;
};

type Union1 = Dog | Person;

let union1: Union1 = {
  name: "",
  color: "",
};

let union2: Union1 = {
  name: "",
  language: "",
};

let union3: Union1 = {
  name: "",
  color: "",
  language: "",
};

/*
let union4: Union1 = {
name: "",
}; // name만 있는 객체는 Dog 타입과 Person 타입의 슈퍼 타입에 해당하는 객체, 어디에도 포함될 수 없다.
*/
```

- 객체들의 유니온 타입은 집합 개념으로 이해하면 좋다.

<br/>

### 교집합 타입 - Intersection

```tsx
let c: number & string; // Never 타입만 할당 가능

type DogCopy = {
  name: string;
  color: string;
};

type PersonCopy = {
  name: string;
  language: string;
};

type Intersection = DogCopy & PersonCopy;

let intersection: Intersection = {
  name: "",
  color: "",
  language: "",
};
```

<br/><br/>

## 타입 추론

- TS는 점진적인 타입 시스템을 채택하는 언어

```tsx
let variable = 10; // 변수 타입을 number로 자동 추론
```

- 어떤 상황에서 TS가 자동으로 타입을 잘 추론하는지
- 또 어떤 원리로 타입을 추론하는지 함께 살펴보자

<br/>

```tsx
let a = 10; // number로 잘 추론
let b = "hello"; // string으로 잘 추론
let c = {
  id: 1,
  name: "이상윤",
  profile: {
    nickname: "SYL",
  },
}; // 객체의 구조를 정확히 파악하여 추론

let { id, name, profile } = c; // 객체를 구조분해할당을 해도 각각 변수의 타입 잘 추론
```

```tsx
let [one, two, three] = [1, "hello", true];
// 웬만한 변수 선언은 잘 추론
```

```tsx
function func() {
  return "hello";
} // 함수의 반환값 타입을 추론할 때는 초기화하는 값이 아닌 return문 다음에 오는 반환값을 기준으로 추론

function func2(message = "hello") {
  return "hello";
}
```

- 다 암기 필요 X
- 추론할 정보가 있다면 추론이 되고, 추론할 정보가 없다면 추론이 되지 않는다.

<br/>

- 우리의 예상과 다르게 타입이 추론되는 당황스러운 상황을 살펴보자.

- 상황 1

  ```tsx
  let d; // 추론 가능한 정보가 없으면 any 타입으로 추론
  d = 10; // d가 number 타입으로 추론
  d.toFixed();

  d = "hello"; // d에 다른 타입 할당 가능, 이제 d는 string으로 추론
  d.toUpperCase();
  ```

  - 이렇게 타입이 계속 바뀌는 상황을 'any 타입의 진화'라고 부른다.
  - 변수의 초기값을 지정하지 않으면 이 때는 암묵적인 any 타입으로 추론된다.
  - 이러한 상황은 안 만드는 것이 좋다.
  - `tsconfig`에 `noImplicitAny`를 true로 설정하면 any 타입 진화를 원천적으로 막을 수 있다고 한다.

<br/>

- 상황 2

  ```tsx
  const num = 10; // numebr 리터럴 타입으로 추론
  // 어차피 상수이기 때문에 다른 값이 담길 일이 없으므로

  const str = "hello"; // string 리터럴 타입으로 추론
  ```

<br/>

- 다른 상황

  ```tsx
  let arr = [1, "string"]; // numebr string 유니온 타입으로 추론
  ```

<br/>

- 범용적으로 프로그래머가 특정 변수를 사용할 수 있도록 조금 더 넓은 타입으로 자동으로 추론해주는 과정을 '타입 넓히기'라고 표현한다.

  ```tsx
  let num2 = 10; // 이 케이스도 타입 넓히기에 포함
  ```

<br/><br/>

## 타입 단언

```tsx
type Person = {
  name: string;
  age: number;
};

let person: Person = {};
person.name = "이상윤";
person.age = 27;
// 이런 식으로 객체를 초기화 해주고 싶으면 어떻게 해야 할까?
```

- 이럴 때 타입 단언을 사용한다.

```tsx
let person = {} as Person;
person.name = "이상윤";
person.age = 27;
```

- 다른 예제

```tsx
type Dog = {
  name: string;
  color: string;
};

let dog = {
  name: "돌돌이",
  color: "brown",
  breed: "진도",
} as Dog;
```

- 위의 예제처럼 초과 프로퍼티 검사 피할 때 as를 쓸 수 있다.

<br/>

- 타입 단언을 사용하려면 적어도 하나의 규칙을 만족해 주어야 한다.

  - A as B일 떄, A가 B의 슈퍼타입 or 서브타입 이어야 함

```tsx
let num1 = 10 as never; // A는 B의 슈퍼타입
let num2 = 10 as unknown; // A는 B의 서브타입
// let num3 = 10 as string; // A는 B의 슈퍼타입 X, 서브타입 X
let num4 = 10 as unknown as string; // 중간에 unknown을 끼고 다중으로 단언을 하면 이런 식으로 단언이 안 되는 타입으로도 단언을 해줄 수 있다.
// 다만, 이 것은 절대로 좋은 방법이 아니다. (TS를 쓰는 이유가 없어짐)
```

<br/>

### const 단언

- const로 선언한 변수와 동일한 효과를 보도록 만들어주는 단언

- const 단언은 특별히 객체 타입과 함께 사용할 때 좀 활둉도가 있다.

```tsx
let cat = {
  name: "야용이",
  color: "yellow",
} as const; // 모든 프로퍼티가 readonly가 된 객체로 추론

cat.name = ""; // 에러
```

- 모든 프로퍼티를 readonly 프로퍼티로 만들 수 있어서 상황에 따라 굉장히 편리하게 사용할 수 있다.

<br/>

### Non Null 단언

```tsx
type Post = {
  title: string;
  author?: string;
};

let post: Post = {
  title: "게시글1",
  author: "이상윤",
};

const len: number = post.author!.length;
// author 값이 없으면 number 값 전체가 undefined로 인식
// ! 붙인 값이 null이나 undefined가 아니라고 컴파일러가 믿도록 만듦
```

<br/><br/>

## 타입 좁히기

- 조건문을 이용해 넓은 타입에서 좁은 타입으로 타입을 상황에 따라 좁히는 방법

```tsx
function func(value: number | string) {
  if (typeof value === "number") {
    console.log(value.toFixed());
    // value는 이 조건문 내에서는 number 타입으로 TS에서 자동으로 추론해줌
  } else if (typeof value === "string") {
    console.log(value.toUpperCase());
    // value는 이 조건문 내에서는 string 타입으로 TS에서 자동으로 추론해줌
  }
}
```

- 이렇게 조건문을 통해 타입을 좁히는 표현을 '타입 가드'로 부른다.

<br/>

- 대표적으로 사용하는 몇 가지 타입 가드들

  ```tsx
  function func2(value: number | string | Date | null) {
    if (typeof value === "number") {
      console.log(value.toFixed());
      // value는 이 조건문 내에서는 number 타입으로 TS에서 자동으로 추론해줌
    } else if (typeof value === "string") {
      console.log(value.toUpperCase());
      // value는 이 조건문 내에서는 string 타입으로 TS에서 자동으로 추론해줌
    }
    //   } else if (typeof value === "object") {
    //     console.log(value.getTime());
    //   } // 이렇게 하면 안된다.
    else if (value instanceof Date) {
      console.log(value.getTime());
    }
  }
  ```

  ```tsx
  type Person = {
    name: string;
    age: number;
  };

  function func3(value: number | string | Date | null | Person) {
    if (typeof value === "number") {
      console.log(value.toFixed());
      // value는 이 조건문 내에서는 number 타입으로 TS에서 자동으로 추론해줌
    } else if (typeof value === "string") {
      console.log(value.toUpperCase());
      // value는 이 조건문 내에서는 string 타입으로 TS에서 자동으로 추론해줌
    }
    //   } else if (typeof value === "object") {
    //     console.log(value.getTime());
    //   } // 이렇게 하면 안된다.
    else if (value instanceof Date) {
      console.log(value.getTime());
    }
    //   else if (value instanceof Person) {
    //   } // instanceof 연산자는 우측에 '타입'이 들어와서는 안된다.
    else if (value && "age" in value) {
      console.log(`${value.age}는 ${value.age}살 입니다.`);
    } // value가 있고, age가 value 안에 있다
  }
  ```

<br/><br/>

## 서로소 유니온 타입

- 더 쉽고 정확하게 직관적으로 타입을 좁힐 수 있도록 객체 타입을 정의하는 특별한 방법

- 교집합이 없는 타입들로만 만든 유니온 타입

- 교집합이 없는 두 개의 집합을 서로소 집합이라고 표현한다.
  `ex) string | number`

```tsx
// 예시
type Admin = {
  tag: "ADMIN"; // string 리터럴 타입
  name: string;
  kickCount: number;
};

type Member = {
  tag: "MEMBER"; // string 리터럴 타입
  name: string;
  point: number;
};

type Guest = {
  tag: "GUSET"; // string 리터럴 타입
  name: string;
  visitCount: number;
};
// Admin, Member, Guest 각각이 서로소 관계
```

```tsx
type User = Admin | Member | Guest; // 서로소 유니온 타입 정의

// 가독성이 떨어지는 방식
function login1(user: User) {
  if ("kickCount" in user) {
    // Admin 타입
    console.log(
      `${user.name} 관리자님 현재까지 ${user.kickCount}명 강퇴했습니다.`
    );
  } else if ("point" in user) {
    // Member 타입
    console.log(`${user.name} 맴버님 현재까지 ${user.point}포인트 모았습니다.`);
  } else {
    // Guest 타입
    console.log(
      `${user.name} 손님 현재까지 ${user.visitCount}번 방문하셨습니다.`
    );
  }
}

// 가독성을 높히는 방식
function login2(user: User) {
  switch (user.tag) {
    case "ADMIN": {
      console.log(
        `${user.name} 관리자님 현재까지 ${user.kickCount}명 강퇴했습니다.`
      );
      break;
    }
    case "MEMBER": {
      console.log(
        `${user.name} 맴버님 현재까지 ${user.point}포인트 모았습니다.`
      );
      break;
    }
    case "GUSET": {
      `${user.name} 손님 현재까지 ${user.visitCount}번 방문하셨습니다.`;
      break;
    }
  }
}
```

```tsx
// 예시 2
// 비동기 작업의 결과를 처리하는 객체
type LoadingTask = {
  state: "LOADING";
};

type FailedTask = {
  state: "FAILED";
  error: {
    message: string;
  };
};

type SuccessTask = {
  state: "SUCCESS";
  response: {
    data: string;
  };
};

// type AsyncTask = {
//   state: "LOADING" | "FAILED" | "SUCCESS";
//   error?: {
//     message: string;
//   };
//   response?: {
//     data: string;
//   };
// };

type AsyncTask = LoadingTask | FailedTask | SuccessTask;

function processResult(task: AsyncTask) {
  switch (task.state) {
    case "LOADING": {
      console.log("로딩 중");
      break;
    }
    case "FAILED": {
      console.log(`에러 발생: ${task.error?.message}`);
      break;
    }
    case "SUCCESS": {
      console.log(`성공: ${task.response?.data}`);
      break;
    }
  }
}

const loading: AsyncTask = {
  state: "LOADING",
};

const failed: AsyncTask = {
  state: "FAILED",
  error: {
    message: "오류 발생 원인은 ...",
  },
};

const success: AsyncTask = {
  state: "SUCCESS",
  response: {
    data: "데이터 ..",
  },
};
```

<br/><br/>
