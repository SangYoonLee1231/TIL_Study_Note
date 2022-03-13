# Python - 출력 함수 <code>print()</code> 사용법

<br/>

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree - Novice Low</a>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_output.md#%EA%B8%B0%EB%B3%B8-%EC%B6%9C%EB%A0%A5-%EB%B0%A9%EB%B2%95">기본 출력 방법</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_output.md#%EB%B3%80%EC%88%98%EB%A5%BC-%ED%8F%AC%ED%95%A8%ED%95%98%EC%97%AC-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0">변수를 포함하여 출력하기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_output.md#%EB%B3%80%EC%88%98%EB%A5%BC-%EC%B6%9C%EB%A0%A5%ED%95%98%EB%8A%94-%EB%8B%A4%EC%96%91%ED%95%9C-%EB%B0%A9%EB%B2%95">변수를 출력하는 다양한 방법</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_output.md#%EC%8B%A4%EC%88%98%ED%98%95-%EB%B3%80%EC%88%98%EB%A5%BC-%EC%86%8C%EC%88%98%EC%A0%90-%EB%A7%9E%EC%B6%B0-%EC%B6%9C%EB%A0%A5%ED%95%98%EA%B8%B0">실수형 변수를 소수점 맞춰 출력하기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_output.md#%EB%B3%80%EC%88%98-%EA%B0%92-%EB%B0%94%EA%BE%B8%EA%B8%B0">변수 값 바꾸기</a>

<br/>

## 기본 출력 방법

### print 함수 통해 한 문장 출력하기

- python3에서 문장을 출력하기 위해 <code>print()</code>함수를 사용한다.

* 이때 괄호 내에 큰 따옴표나 작은 따옴표 둘 중 아무거나 사용해도 된다.

* python에선 작은 따옴표로 묶어도 문자가 아닌 문자열로 인식한다. (python에선 문자 개념이 없다.)

  ```python
  print("Hello World")
  print('Hello World')
  ```

  ```
  Hello World
  Hello World
  ```

<br/>

### 특수 문자를 포함시켜 출력하기

- 문자열 내에 있는 특수 문자 앞에 <code>\\</code>를 붙여주면, 이를 기호가 아닌 문자로 인식한다.

  (자주 사용하는 방법이므로 기억하자)

  ```python
  print("Let\'s do it")
  ```

<br/>

- <code>"</code>,<code>'</code>를 포함시킬 때, <code>"""</code> 또는 <code>'''</code>로 전체 문장을 감싸는 방법도 있다.

  ```python
  print('''Let's do it''')
  ```

  ▼ 출력 결과

  ```
  Let's do it
  ```

<br/>

### 2줄 출력하기 (print 함수 한 번만 사용)

- <code>\n</code>문자를 이용한다. (new line을 의미하는 특수 문자)

  ```python
  print("Hello World\nNice to meet you")
  ```

  ▼ 출력 결과

  ```
  Hello World
  Nice to meet you
  ```

<br/>

- <code>"""</code> 또는 <code>'''</code>을 사용해도 된다.

  ```python
  print("""Hello World
  Nice to meet you""")
  ```

  ▼ 출력 결과

  ```
  Hello World
  Nice to meet you
  ```

<br/>

### 두 값을 공백을 두고 출력하기

- print 함수에 2개의 값을 <code>,</code>를 사이에 두고 넣어준다.

  ```python
  print(1, 2)
  ```

  ▼ 출력 결과

  ```
  1 2
  ```

<br/>

- <code>,</code> 사용 시 구분자로 쓸 값을 <strong>sep</strong>를 이용하여 직접 설정할 수 있다.

  ```python
  print(1, 2, sep=" ")
  print(1, 2, sep=",")
  print(1, 2, sep="/")
  ```

  ▼ 출력 결과

  ```
  1 2
  1,2
  1/2
  ```

<br/>

- print 함수는 end라는 값에 <code>\n</code> 문자가 기본적으로 들어가 있기 때문에, 다음 줄로 알아서 넘어간다.

* 이 end값을 공백 <code>' '</code>으로 바꾸면 print 함수 2개로 공백을 두고 출력할 수 있다.

  ```python
  print(1, end=" ")
  print(2)
  ```

  ▼ 출력 결과

  ```
  1 2
  ```

<br/>

## 변수를 포함하여 출력하기

- 정수값을 넣어 선언한 변수도 <code>print()</code>함수를 통해 출력할 수 있다.

* 2개 이상의 변수를 한 줄에 동시에 선언할 수 있다.

* 변수끼리 사칙연산이 가능하다. (정수형, 실수형끼리만)

  ```python
  a = 1
  b, c = 2, 3
  d = b + c
  print("a =", a)
  print("d =", d)
  ```

  ▼ 출력 결과

  ```
  a = 1
  d = 5
  ```

<br/>

- 변수의 이름은 다르게 정할 수 있고, 문자열이나 실수도 담을 수 있다.

  ```python
  dummy = "toy"
  temp = 3.141592653
  ```

<br/>

- print() 함수에 type()을 사용하면 해당 변수의 자료형을 확인할 수 있다.

  ```python
  dummy = "toy"
  temp = 3.141592653
  print(type(dummy))  # <class 'str'>
  print(type(temp))  # <class 'float'>
  ```

<br/>

### 코딩 컨벤션

- 일반적으로 변수나 함수명은 소문자로 쓰는 것이 원칙이며, 띄어쓰기가 필요할 경우 언더바 (Underscore)를 사용한다.

- 이와 같은 일종의 코드 작성 규약을 <strong>"코딩 컨벤션 (Coding Convention)"</strong>이라 한다.

* 코딩 컨벤션은 협업을 위한 일종의 약속으로, 각 언어나 회사에 따라 정의해 놓은 코딩 컨벤션은 다양하다.

<br/>

## 변수를 출력하는 다양한 방법

### 1. 변수 포멧 (%d, %s, ...) 이용

- <code>%d</code>, <code>%s</code> 등의 변수 포멧을 사용하여 문자열에 변수 값을 삽입한다.

  ```python
  x = 10
  print("x is %d" % x)

  y = "code"
  print("y is %s" % y)

  print("x is %d and y is %s" % (x, y))
  ```

  ▼ 출력 결과

  ```
  x is 10
  y is code
  x is 10 and y is code
  ```

- 변수 포멧

  - <code>%s</code> : 문자열

  - <code>%c</code> : 문자

  - <code>%d</code> : 정수

  - <code>%f</code> : 실수

<br/>

### 2. format 함수 이용

- format 함수를 이용하면 변수의 타입을 명시하지 않아도 된다.

- 순서 또는 변수 이름을 통해 원하는 변수를 포멧에 맞춰 넣어줄 수 있다.

  ```python
  x, y = 10, "code"

  print("x is {0}" .format(x))
  print("x is {new_x}" .format(new_x=x))

  print("\n")

  print("x is {0} and y is {1}" .format(x, y))
  print("x is {new_x} and y is {new_y}" .format(new_x=x, new_y=y))
  print("y is {1} and x is {0}" .format(x, y))
  print("y is {new_y} and x is {new_x}" .format(new_x=x, new_y=y))

  #print("x is {x}" .format(x))  # 오류
  ```

  ▼ 출력 결과

  ```
  x is 10
  x is 10

  x is 10 and y is code
  x is 10 and y is code
  y is code and x is 10
  y is code and x is 10
  ```

<br/>

### 3. f 문자열 포멧 이용 (사용 권장)

- 문자열 앞에 f를 붙이면, 중괄호와 변수 이름만으로 문자열에 원하는 변수를 삽입할 수 있다.

  ```python
  x, y = 10, "code"

  print(f"x is {x}")
  print(f"y is {y}")
  print(f"x is {x} and y is {y}")
  ```

  ▼ 출력 결과

  ```
  x is 10
  y is code
  x is 10 and y is code
  ```

<br/>

## 실수형 변수를 소수점 맞춰 출력하기

- .4f == 소수 4째 자리까지 반올림 출력

### 1. 변수 포멧 (%d, %s, ...) 이용

- <code>%</code>를 이용한다.

  ```python
  x = 3.141592653
  print("%.4f" % x)
  ```

  ▼ 출력 결과

  ```
  3.1416
  ```

<br/>

### 2. format 함수 이용

- 기존 포멧 <code>{0}</code>에<code>:</code>를 붙여 사용한다.

  ```python
  x = 3.141592653
  print("{0:.4f}" .format(x))
  ```

  ▼ 출력 결과

  ```
  3.1416
  ```

<br/>

### 3. f 문자열 포멧 이용

- 마친가지로 기존 포멧에 <code>:</code>를 붙여 사용한다.

  ```python
  x = 3.141592653
  print(f"{x:.4f}")
  ```

  ▼ 출력 결과

  ```
  3.1416
  ```

<br/>

## 변수 값 바꾸기

### 변수 값 변경 및 복사

- 변수에 새 값을 대입하면, 기존 값은 사라지고 새로 대입한 값만 남는다.

- 변수에 다른 변수를 대입하면, 기존에 있던 값은 사라지고 대입한 변수의 값이 복사된다.

  ```python
  a, b = 1, 2

  a = b
  print(a)

  a = 5
  print(a)
  ```

  ▼ 출력 결과

  ```
  2
  5
  ```

<br/>

### 두 변수 값 교환

- <strong>[방법 1] temp 이용</strong>

  ```python
  a, b = 1, 2

  temp = b
  b = a
  a = temp

  print(f"a = {a}, b = {b}")
  ```

  ▼ 출력 결과

  ```
  a = 2, b = 1
  ```

<br/>

- <strong>[방법 2] <code>,</code> 이용하여 바로 교환</strong>

  ```python
  a, b = 1, 2

  a, b = b, a

  print(f"a = {a}, b = {b}")
  ```

  ▼ 출력 결과

  ```
  a = 2, b = 1
  ```

- (참고) 파이썬만 temp없이 a,b = b,a 교환할 수 있는 이유는 python만 tuple 자료형이 존재하고, 그 tuple이 unpacking을 지원하기 때문이다.

<br/>

#### (참고) Unpacking

- 언패킹(Unpacking)이란 여러 개의 데이터가 패킹된 것을 풀어서 각각의 다른 변수에 저장하는 것이다.

  ```python
  arr = [1, 2]
  tup = (1, 2)

  a, b = arr
  a, b = tup
  ```

  <br/>

- 다음과 같이 언패킹을 활용할 수 있다.

  ```python
  a, b = 3, (5, 6, 7, 4, 6)

  a, (b1, b2, b3, b4, b5) = 3, (5, 6, 7, 4, 6)
  b1, b2, b3, b4, b5 = b

  print(b1, b2, b3, b4, b5)
  ```

  ```
  5 6 7 4 6
  ```

<br/>

### 변수값 동시에 복사

- <code>=</code>을 연쇄적으로 사용하면, 한 변수의 값을 여러 변수에 복사할 수 있다.

  ```python
  a, b, c = 1, 2, 3

  a = b = c

  print(f"a = {a}, b = {b}, c = {c}")
  ```

  ▼ 출력 결과

  ```
  a = 3, b = 3, c = 3
  ```
