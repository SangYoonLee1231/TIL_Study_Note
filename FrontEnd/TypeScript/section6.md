# 클래스

## 자바스크립트의 클래스

```js
let studentA = {
  name: "SYL",
  grade: "A+",
  age: 27,
  study() {
    console.log("열심히 공부 함");
  },
  introduce() {
    console.log("안녕하세요");
  },
}; // 한 명의 학생을 객체로 표현

let studentB = {
  name: "길동 홍",
  grade: "A+",
  age: 27,
  study() {
    console.log("열심히 공부 함");
  },
  introduce() {
    console.log("안녕하세요");
  },
}; // 한 명의 학생을 객체로 표현
```

- 중복 코드 발생!

- 이럴 때 JS 클래스를 이용한다.

<br/>

- 클래스: 객체를 만들어내는 틀

```js
class Student {
  // 필드 (객체의 프로퍼티)
  name;
  grade;
  age;

  // 생성자 (클래스 호출 시 객체를 만드는 메서드)
  constructor(name, grade, age) {
    this.name = name;
    this.grade = grade;
    this.age = age;
  }

  // 메서드
  study() {
    console.log("열심히 공부 함");
  }

  introduce() {
    console.log(`안녕하세요 ${this.name} 입니다.`);
  }
}

let studentC = new Student("이상윤", "A+", 27);
console.log(studentC); // Student { name: '이상윤', grade: 'A+', age: 27 }
// 클래스를 이용해서 만든 객체를 '인스턴스'라 부른다.

studentC.study(); // 열심히 공부 함
studentC.introduce(); // 안녕하세요 이상윤 입니다.
```

<br/>

#### 클래스의 상속

```ts
class StudentDeveloper extends Student {
  // 필드
  favoriteSkill;

  // 생성자
  constructor(name, grade, age, favoriteSkill) {
    super(name, grade, age);
    this.favoriteSkill = favoriteSkill;
  }

  // 메서드
  programming() {
    console.log(`${this.favoriteSkill}f로 프로그래밍 함`);
  }
}

const studentDeveloper = new StudentDeveloper("이상윤", "B+", 27, "TypeScript");
console.log(studentDeveloper);
studentDeveloper.programming();
```

<br/>

- 타입스크립트에서의 클래스는 자바스크립트의 클래스로 취급이 동시에 되면서 타입으로도 취급될 수 있다.

```ts
const empolyeeC: Empolyee = {
  name: "",
  age: 0,
  position: "",
  work() {},
};
```

<br/>

- 클래스를 확장해보자.

```ts
class ExecutiveOfficer extends Empolyee {
  // 필드
  officeNumber: number;

  // 생성자
  constructor(
    name: string,
    age: number,
    position: string,
    officeNumber: number
  ) {
    super(name, age, position);
    this.officeNumber = officeNumber;
  }
}
```

<br/><br/>

## 접근 제어자 (Access Modifier)

- 타입스크립트의 클래스에서만 제공하는 기능

- 필드나 메소드에 접근할 수 있는 범위를 설정하는 문법

- public, private, protected

```ts
class Empolyee {
  // 필드
  private name: string;
  protected age: number;
  public position: string;

  // 생성자
  constructor(name: string, age: number, position: string) {
    this.name = name;
    this.age = age;
    this.position = position;
  }

  // 메서드
  work() {
    console.log("일함");
  }
}

const employee = new Empolyee("이상윤", 27, "developer");

// employee.name = "홍길동"; // private
// employee.age = 30; // protected
employee.position = "디자이너";

// private: 클래스 내부에서만 접근이 가능

class ExecutiveOfficer extends Empolyee {
  // 필드
  officeNumber: number;

  // 생성자
  constructor(
    name: string,
    age: number,
    position: string,
    officeNumber: number
  ) {
    super(name, age, position);
    this.officeNumber = officeNumber;
  }

  // 매서드
  func() {
    // this.name = ""; // name이 private이므로 접근 금지
    this.age = 30;
  }
}

// protected: 파생 클래스까진 접근 가능
```

<br/>

- 참고

  - 생성자에도 접근 제어자를 달아줄 수 있는데, 만일 필드에도 선언되어 있다면 이는 중복이 되어 오류가 발생한다.
  - 생성자의 매개변수에 접근 제어자를 쓰면 초기화가 자동으로 이루어지며 필드 선언도 생략할 수 있다.

<br/><br/>

## 인터페이스와 클래스

```ts
interface CharacterInterface {
  name: string;
  moveSpeed: number;
  move(): void;
} // 여기서 인테페이스는 클래스의 설계도 역할을 한다.

class Character implements CharacterInterface {
  constructor(public name: string, public moveSpeed: number) {}

  move(): void {
    console.log(`${this.moveSpeed} 속도로 이동`);
  }
}
```

- 인터페이스로 정의하는 필드들은 무조건 public이다.

- 인터페이스를 이용해서 이렇게 설계도를 구현하는 일은, 어떤 라이브러리 구현이나 굉장히 복잡하고 정교한 프로그래밍을 할 때 필요할 수 있다.

<br/><br/>
