# 제네릭

## 제네릭 소개

- 제네릭은 General, 즉 이것도 되고 저것도 된다.

- 제네릭 함수

  ```ts
  function func<T>(value: T): T {
    return value;
  } // <T>: 타입을 저장하는 변수. '타입 변수'라 부름. 인수의 타입에 따라 결정

  let num = func(10);

  let boolean = func(true);

  let str = func("string");

  let arr = func([1, 2, 3]);

  let arr2 = func<[number, number, number]>([1, 2, 3]);
  // 배열을 튜플 타입으로 전달하고 싶을 때
  ```

- 우리가 원하는 대로 함수의 인수에 따라서 반환값의 타입을 가변적으로 정해줄 수 있다.

- 마치 함수계의 종합 병원

<br/><br/>

## 타입 변수 응용하기

- 총 3가지 사례를 살펴본다.

- 사례 1

  ```ts
  function swap<T, U>(a: T, b: U) {
    return [b, a];
  }

  const [a, b] = swap("1", 2);
  ```

  - 타입 변수를 여러 개 선언해서 사용할 수 잇다.

<br/>

- 사례 2

  ```ts
  function returnFirstValue<T>(data: T[]) {
    return data[0];
    // T 자체는 unknown 타입으로 추론
  }

  let num = returnFirstValue([0, 1, 2]); // 0
  let str = returnFirstValue(["Hello", "my", "name", "is"]); // Hello
  ```

  - 이런 식으로 타입 변수를 매개변수에 그대로 갖다가 쓸 필요 없이 배열 타입과 함께 쓸 수도 있다.

<br/>

- 사례 2 심화

  ```ts
  function returnFirstValueCopy<T>(data: [T, ...unknown[]]) {
    return data[0];
  }

  let str2 = returnFirstValueCopy([1, "Hello", "my", "name", "is"]); // Hello
  ```

<br/>

- 사례 3

  ```ts
  function getLength<T extends { length: number }>(data: T) {
    return data.length;
  } // length 프로퍼티가 있을 때만 읽도록 타입을 제한하기

  let var1 = getLength([1, 2, 3]); // 3

  let var2 = getLength("12345"); // 5

  let var3 = getLength({ length: 10 }); //10

  // let var4 = getLength(10); // 에러! length 가지고 있지 않음
  ```

<br/><br/>

## map, forEach 메서드 타입 정의하기

#### 1. map 메서드

```ts
const arr = [1, 2, 3];
const newArr = arr.map((it) => it * 2);
// [2, 4, 6]
```

- it이 자동으로 number 타입으로 추론되고 있다.
- 이는 이 map 메서드의 타입이 어딘가에 별도로 선언되어 있기 때문

<br/>

```ts
function map<T>(arr: T[], callback: (item: T) => T) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    result.push(callback(arr[i]));
  }

  return result;
}

map(arr, (it) => it * 2);
map(["hi", "hello"], (it) => it.toUpperCase());

// map(["hi", "hello"], (it) => parseInt(it));
// 이렇게 하면 위의 코드는 에러를 발생한다.
// return 값의 타입이 number가 아니기 때문
// 하지만 실제 map 함수는 위와 같은 코드도 동작해야 하므로, 타입 변수를 하나 더 선언해준다.
```

```ts
function map2<T, U>(arr: T[], callback: (item: T) => U) {
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    result.push(callback(arr[i]));
  }

  return result;
}

map2(["hi", "hello"], (it) => parseInt(it));
```

<br/>

#### 2. forEach 메서드

```ts
const arr2 = [1, 2, 3];
arr2.forEach((it) => console.log(it));

function forEach<T>(arr: T[], callback: (item: T) => void) {
  for (let i = 0; i < arr.length; i++) {
    callback(arr[i]);
  }
}

forEach(arr2, (it) => {
  console.log(it.toFixed());
});

forEach(["123", "456"], (it) => {
  console.log(parseInt(it));
});
```

<br/><br/>

## 제네릭 인터페이스

- 제레릭 함수처럼 타입 변수를 이용한다.

```ts
interface KeyPair<K, V> {
  key: K;
  value: V;
}

let keyPair: KeyPair<string, number> = {
  key: "key",
  value: 0,
}; // 제네릭 인터페이스를 사용할 때는 반드시 타입 변수에 할당할 타입을 꺾쇠와 함께 사용해야 한다.
```

- 타입 변수 (TS 공식 문서 용어)
  = 타입 파라미터
  = 제네릭 타입 변수
  = 제네릭 타입 파라미터

```ts
let keyPair2: KeyPair<boolean, string[]> = {
  key: true,
  value: ["1"],
};
```

<br/>

- 제네릭 인터페이스는 특히 객체의 인덱스 시그니쳐 문법과 함께 사용하면 굉장히 유연한 객체 타입을 만들 수 있다.

```ts
// 인덱스 시그니쳐
interface NumberMap {
  [key: string]: number;
}

let numberMap1: NumberMap = {
  key: -1231,
  key2: 123234,
};

interface Map<V> {
  [key: string]: V;
}

let stringMap: Map<string> = {
  key: "value",
};

let booleanMap: Map<boolean> = {
  key: true,
};
```

<br/>

#### 제네릭 타입 별칭

```ts
type Map2<V> = {
  [key: string]: V;
};

let stringMap2: Map2<string> = {
  key: "hello",
};
```

<br/>

#### 제네릭 인터페이스의 활용 예시

```ts
// 유저 관리 프로그램 -> 학생 유저와 개발자 유저로 나뉨

interface Student {
  type: "student";
  school: string;
}

interface Developer {
  type: "developer";
  skill: string;
}

interface User<T> {
  name: string;
  profile: T;
}

// 학생만 할 수 있는 기능
function goToSchool(user: User<Student>) {
  //   if (user.profile.type !== "student") {
  //     console.log("잘 못 오셨습니다");
  //     return;
  //   }
  // 제네릭을 사용하면 타입 좁히기를 안 해도 된다.

  const school = user.profile.school;
  console.log(`${school}로 등교 완료`);
}

const developerUser: User<Developer> = {
  name: "이상윤",
  profile: {
    type: "developer",
    skill: "TypeScript",
  },
};

const studentUser: User<Student> = {
  name: "홍길동",
  profile: {
    type: "student",
    school: "한국외대",
  },
};
```

<br/><br/>

## 제네릭 클래스

```ts
class List<T> {
  constructor(private list: T[]) {}

  push(data: T) {
    this.list.push(data);
  }
  pop() {
    return this.list.pop();
  }

  print() {
    console.log(this.list);
  }
}

const numberList = new List([1, 2, 3]);
numberList.pop();
numberList.push(4);
numberList.print();

const stringList = new List(["1", "2"]);

// 클래스의 생성자를 호출할 때, 이 생성자의 인수로 전달하는 값(["1", "2"])을 기준으로 타입 변수의 타입을 추론한다.
// 제네릭 인터페이스랑 제네릭 타입 변수와는 다르게 변수 선언 시 앞에 타입을 명시해주지 않아도 된다.
// const stringList = new List<number>(["1", "2"]); <- 이럴 필요 없다
```

<br/><br/>

## 프로미스와 제네릭

```ts
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve(20);
  }, 3000);
});

promise.then((response) => {
  console.log(response); // 20
  // 이 때 response는 unknown 타입이다.
});

// 이럴 때 제네릭을 이용한다.
```

- JavaScript의 내장 클래스인 Promise는 TypeScript에서는 제네릭 클래스로 타입이 별도로 선언되어 있다.

```ts
const promise2 = new Promise<number>((resolve, reject) => {
  setTimeout(() => {
    resolve(20);
  }, 3000);
});

promise2.then((response) => {
  console.log(response); // 20
  // 이제 response는 number 타입으로 잘 추론된다.
});

// 실패했을 때
const promise3 = new Promise<number>((resolve, reject) => {
  setTimeout(() => {
    reject("~~ 때문에 실패");
  }, 3000);
});

promise.catch((err) => {
  // 여기서 err은 any 타입이다.
  // 타입 좁히기를 사용해야 한다. 다른 방법은 없다.
  if (typeof err === "string") {
    console.log(err);
  }
});

// reject, 즉 실패의 상황에서는 타입을 정해줄 수 없다. 그래서 타입 좁히기를 사용해야 한다.
```

<br/>

#### 프로미스를 반환하는 함수의 타입을 정의

- 보통 Promise는 어떤 데이터를 불러오는 함수의 반환값으로 자주 쓰인다.

- 이러한 상황을 살펴보자.

```ts
interface Post {
  id: number;
  title: string;
  content: string;
}

function fetchPost() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({
        id: 1,
        title: "게시글 제목",
        content: "게시글 컨텐츠",
      });
    });
  });
}

const postRequest = fetchPost(); // Promise 객체가 할당

postRequest.then((post) => {
  // console.log(post.id); // post는 unknown 타입이라 읽을 수 없음
});

// 이를 제네릭을 이용해 해결하는 방법
function fetchPost2(): Promise<Post> {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({
        id: 1,
        title: "게시글 제목",
        content: "게시글 컨텐츠",
      });
    });
  });
}
```

<br/><br/>
