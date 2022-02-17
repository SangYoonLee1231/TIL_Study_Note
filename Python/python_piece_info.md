## Python - 조각 지식 모음

<br/>

- 파이썬과 관련된 공부 내용 중 하나의 목차로 분류하기 애매한 지식을 따로 모아 정리하는 곳입니다.

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_piece_info.md#%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EB%B3%80%EC%88%98%EC%9D%98-scope-%EB%B2%94%EC%9C%84">파이썬에서 변수의 scope 범위</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_piece_info.md#2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%84%A0%EC%96%B8-%EC%8B%9C-%EC%9C%A0%EC%9D%98-%EC%82%AC%ED%95%AD">2차원 배열 선언 시 유의 사항</a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>
- <a href=""></a>

<br/>

## 파이썬에서 변수의 scope 범위

- 파이썬에서 <code>for</code>문이나 <code>if</code>문, 또는 함수의 내부에 선언한 지역 변수는 놀랍개도 main 함수 영역(indent가 없는 코드 영역)에서도 그대로 사용할 수 있다.

  ```python
  sum_val = 0
  for idx in range(1, 6):
      sum_val += idx

  print(idx)
  ```

  ```
  5
  ```

    <br/>

  ```python
  n = 10
  if n % 2 == 0:
      k = 5
  else:
      k = 6

  print(k)
  ```

  ```
  5
  ```

<br/>

- 다만 이러한 지역 변수는 다른 함수(<code>for</code>문, <code>if</code>문도 포함)의 내부 영역에선 참조할 수 없다.

  ```python
  def g(n):
      return n + t    # 이 g함수 내부에선, f함수 내부의 t에 접근할 수 없다.

  def f(n, p1):
      t = 15
      return n + p1 + g(10)

  p = 9
  print(f(6, 10))
  ```

  ```
  NameError: name 't' is not defined
  ```

<br/>

- 그러나 코드는 되도록 이렇게 안 짜는 것이 좋다.

<br/><br/>

## range 함수의 이해 (C++ 반복문과 python 반복문의 차이점)

- <code>range(1, 6)</code> == <code>[1, 2, 3, 4, 5]</code> 이렇게 이해하면 편한다. (틀린 설명이나)

    <br/>

  ```c++
  #include <iostream>
  using namespace std;

  int main() {
      int sum_val = 0;
      int i;

      for (i = 0; i < 6; i++) {
          sum_val += i;
      }

      cout << i;

      return 0;
  }
  ```

  ```
  6
  ```

- C++에서 for문은 변수 i 자체가 값이 1씩 증가하다 조건을 벗어나는 순간, 즉 위 코드에선 i가 6이 된 직후, 종료한다.

    <br/>

  ```python
  sum_val = 0
  for i in range(1, 6):
      sum_val += i

  print(i)
  ```

  ```
  5
  ```

- 반면 파이썬에서 for문은 변수 i 자리에 1부터 5까지 값이 하나씩 대입되고 끝난다. 즉 i값은 5인 상태가 된다.

<br/><br/>

## 2차원 배열 선언 시 유의 사항

- 다음과 같이 2차원 배열을 선언하면 안 된다.

  ```python
  [[0] * n ] * n
  ```

<br/>

- 그 이유를 이해하기 위해 우선 다음 코드를 살펴보자.

  ```python
  a = [0, 0, 0]
  b = a

  b[0] = 1
  print(a[0])
  ```

  ```
  1
  ```

- 놀랍게도, <code>b[0]</code>의 값을 바꾸었는데 <code>a[0]</code>의 값이 바뀌었다.

- 하나의 리스트를 <code>=</code>연산을 통해 다른 리스트로 넣어주면 둘이 같은 주소를 가리키기 때문이다. 즉, 이 둘은 같은 리스트다.  
  이러한 현상은 리스트 복제 연산에서도 마찬가지로 일어난다.

- 따라서 리스트 b의 변화는 그대로 리스트 a에 반영된다.

<br/>

- 이제 다시 2차원 배열 선언 코드로 돌아오자.

  ```python
  [0] * n
  ```

- 위의 코드처럼 1차원 리스트를 선언해주는 것은, 그저 숫자를 복사하는 것이기 때문에 아무런 상관이 없다.

  ```python
  [0, 0, 0, ... , 0] * n
  ```

- 그러나 위처럼 1차원 리스트를 복사하여 2차원 리스트를 선언해주면, 복제된 모든 리스트가 같은 주소를 가리키게 된다.

- 즉, 이 상태에서 2차원 리스트 내부의 하나의 리스트에 변화를 주면, 다른 모든 리스트에도 반영이 된다.

  ```python
  a = [[0] * 10] * 10

  a[0][1] = 17

  print(a[1][1])
  ```

  ```
  17
  ```

<br/>

- 그러므로 2차원 리스트를 선언할 땐, <code>list comprehension</code>을 쓰거나 <code>for</code>문을 통해 값을 추가하는 방법으로 해야 한다.

  ```python
  lst1 = [
      [0] * n
      for _ in range(n)
  ]

  lst2 = []
  for _ in range(n):
      lst_1d = [0] * n
      lst2.append(lst_1d)
  ```

<br/><br/>

## python의 최대, 최소 정수값 찾아 활용하기

- 어떤 리스트 내 정수 원소들의 최댓값 혹은 최솟값을 내장 함수를 쓰지 않고 직접 구현할 때, 초깃값을 잘 잡아주어야 한다.

* 이 떄, 첫 번째 원소를 초갓값으로 잡아주어도 되지만, python의 <code>int</code>의 최댓값인 <code>sys.maxsize</code>를 사용하는 것이 좋다.

* 더불어 python의 <code>int</code>의 최솟값은 여기에 마이너스를 붙여 <code>-sys.maxsize</code>로 구할 수 있다.

```python
import sys

INT_MAX = sys.maxsize

lst = [34, 5, 67, 4, 8, 15, 2]
max_sum = -sys.minsize

for elem in lst:
    if elem > max_sum:
        max_sum = elem
    #max_sum = max(elem, max_sum)

print(max_sum)
```

```
67
```

- 위 코드처럼 리스트 내 원소들의 최댓값 찾을 땐, 초기값을 가장 작은 수인 <code>-sys.maxsize</code>로 두어야 한다. (for문을 돌면서 더 큰 값으로 업데이트 할 수 있도록)

  - 반대로 최솟값을 찾을 땐, 가장 큰 수 <code>sys.maxsize</code>로 초기값을 잡아주면 된다.
