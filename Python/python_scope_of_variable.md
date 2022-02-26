# Python - 변수 Scope (전역 변수와 지역 변수)

<br/>

> 참고 자료 : Code Tree

<br/>

- 이 글은 『<a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_call_by_assignment.md">Python - Call By Assignment</a>』의 내용을 전제로 기록하였습니다.

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_scope_of_variable.md#%EC%98%88%EC%8B%9C-1">예시 1.</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_scope_of_variable.md#%EC%97%90%EC%8B%9C-2">에시 2</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_scope_of_variable.md#%EC%98%88%EC%8B%9C-3">예시 3.</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_scope_of_variable.md#-%EC%A0%95%EB%A6%AC">✨ 정리</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_scope_of_variable.md#-%EC%B0%B8%EC%A1%B0-%EA%B0%80%EB%8A%A5%ED%95%9C-%EA%B0%92%EC%9D%B4-%EC%97%AC%EB%9F%AC-%EA%B0%80%EC%A7%80%EC%9D%BC-%EB%95%8C">(+) 참조 가능한 값이 여러 가지일 때</a>

<br/>

### 예시 1.

- 코드

  ```python
  _list = [1, 2, 3, 4]


  def sum_all():
      sum_val = 0
      for elem in _list:
          sum_val += elem

      return sum_val


  total_sum = sum_all()
  print(total_sum)
  print(sum_val)
  ```

  ```
  10
  NameError: name 'sum_val' is not defined
  ```

* 전역 변수는 굳이 인자로 넘기지 않아도 함수 내에서 잘 작동한다. 즉, 전역 변수는 어디에서나 쓸 수 있다.

- 지역 변수는 내부 Scope를 벗어나면 증발하여 더 이상 접근할 수 없다. 즉, 지역 변수는 어디에서나 쓸 수 없다.

<br/>

### 에시 2

- 코드 1

  ```python
  _list = [1, 2, 3, 4]


  def modify():
      _list[0] = 10


  modify()
  for elem in _list:
      print(elem, end=" ")
  ```

  ```
  10 2 3 4
  ```

* list는 mutable한 객체이므로, 전역 변수로 선언되었을 때 함수 내부에서 값을 참조하고 수정해도 원본에 반영된다.

* 위의 코드에서 <code>modify()</code> 함수 내부의 <code>\_list</code> 변수는 외부에 선언된 전역 변수 <code>\_list</code>로 인식된다.

<br/>

- 코드 2.

  ```python
  _list = [1, 2, 3, 4]


  def modify():
      _list = [5, 6, 7, 8]


  modify()
  for elem in _list:
      print(elem, end=" ")
  ```

  ```
  1 2 3 4
  ```

- 반면, 위의 코드에선 <code>modify()</code> 함수 내부의 <code>\_list</code>가 재정의 되었으므로, python에선 이를 새로운 지역 변수로 인식한다.

* 따라서 <code>modify()</code> 함수가 끝나는 순간 (새로 생성됐던) 함수 내부의 <code>\_list</code> 객체는 소멸하고, 외부에 선언된 전역 변수 <code>\_list</code>만 남게 된다.

<br/>

- 만일 <code>modify()</code> 함수 내부의 <code>\_list</code>를 전역 변수로 인식하도록 하려면, 다음처럼 함수 안에 global 표식을 해주어야 한다.

  ```python
  _list = [1, 2, 3, 4]


  def modify():
      global _list
      _list = [5, 6, 7, 8]


  modify()
  for elem in _list:
      print(elem, end=" ")
  ```

  ```
  5 6 7 8
  ```

- 원래 원칙은, 전역 변수를 함수 내에서 쓰려면 함수 안에 global 표식을 해줘야 한다.

* 하지만 모르거나 귀찮아서 보통 잘 쓰지 않는다. 평소에 안 써도 무방하다.

<br/>

### 예시 3.

- 코드 1.

  ```python
  num = 10


  def modify():
      print(num)


  modify()
  ```

  ```
  10
  ```

* 전역 변수를 함수 내부에서 값을 끌어다 쓰는 것은 모두 허용된다.

<br/>

- 코드 2.

  ```python
  num = 10


  def modify():
      num = 5


  modify()
  print(num)
  ```

  ```
  10
  ```

- 10, 5는 immutable한 객체이다. 따라서 <code>modify()</code> 함수 내부에 선언된 <code>num</code>은 지역 변수이다.

* 따라서 5의 값에 <code>num</code>을 연결해도 전역 변수의 <code>num</code> 값은 그대로인 것이다.

<br/>

- 코드 3.

  ```python
  num = 10


  def modify():
      num += 5


  modify()
  print(num)
  ```

  ```
  UnboundLocalError: local variable 'num' referenced before assignment
  ```

* 이 코드에선 왜 이러한 에러가 발생하는지 이해해보자.

- <code>num += 5</code> 는 <code>num = num + 5</code>와 동일한 코드이다.

* 이를 반영하여 코드를 다시 작성하면 아래와 같다.

  ```python
  num = 10


  def modify():
      num = num + 5
     (1번)  (2번)


  modify()
  print(num)
  ```

* <code>modify()</code> 함수 내의 (1번) <code>num</code>이 새롭게 정의되었으므로 이는 New 지역 변수로 인식된다.

* 따라서 (2번) <code>num</code>도, 전역 변수의 <code>num</code>이 아닌, 새로운 지역 변수로 인식된다.

* 이 지역 변수 (2번) <code>num</code>은 값이 아직 할당이 되지 않았기 때문에 위와 같은 에러가 발생하는 것이다.

<br/>

- 이를 해결하고자 한다면, 함수 내에 global 표식을 붙여 <code>modify()</code> 함수 내 <code>num</code>을 전역 변수 <code>num</code>으로 인식되도록 해주면 된다.

  ```python
  num = 10


  def modify():
      global num
      num += 5


  modify()
  print(num)
  ```

  ```
  15
  ```

<br/>

### ✨ 정리

- 전역 변수로 선언된 immutable 객체를 함수 내에서 바꾸고 더하는 작업을 하려면, global 표식을 해주어야 한다.

- 전역 변수로 선언된 mutable 객체를 함수 내에서 바꾸고 더하는 작업을 하려면, 객체 특성 상 그냥 갖다 써도 상관 없다.

* 대신 함수 내에서 전역 변수와 같은 이름으로 변수를 재정의 한다면, immutable 객체든 mutable 객체든 재정의된 변수는 새로운 지역 변수로 인식된다. 이렇게 되기 싫으면 global 표식을 해주면 된다.

<br/>

### (+) 참조 가능한 값이 여러 가지일 때

```python
a, b = 10, 20


def modify(a, b):
    print(a, b)  # (1번)
    print_a_and_b()
    a, b = b, a
    print(a, b)


def print_a_and_b():
    print(a, b) # (2번)


modify(50, 60)
print_a_and_b()
```

```
50 60
10 20
60 50
10 20
```

- (1번)에서의 <code>a</code>, <code>b</code>는 전역 변수의 <code>a</code>, <code>b</code> (10, 20)를 참조하는 것도 가능하고 인자 값 (50, 60)을 참조하는 것도 가능하다.

* 이렇게 참조할 수 있는 값이 여러 가지일 땐, <strong>가장 가까이에 있는 값을 참조한다.</strong>

* 즉, (1번)에서 <code>a</code>는 50을 가리키고, <code>b</code>는 60을 가리킨다.

* (2번)의 경우, <code>a</code>, <code>b</code>는 전역 변수 <code>a</code>, <code>b</code>밖에 참조할 값이 없으므로 각각 10, 20을 가리킨다.
