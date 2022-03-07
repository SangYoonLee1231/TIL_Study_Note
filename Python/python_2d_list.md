# Python - 2차원 리스트(배열)

<br/>

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree - Novice Low</a>

<br/>

## 목차

- <a href="">2차원 리스트 개념</a>
- <a href="">2차원 리스트 입력</a>
- <a href="">2차원 리스트 선언</a>
- <a href="">2차원 배열 선언 시 유의 사항</a>
- <a href="">2차원 리스트 출력</a>
- <a href="">2차원 리스트 활용</a>

<br/>

## 2차원 리스트 개념

- 리스트를 원소로 갖는 리스트를 2차원 리스트(혹은 2중 리스트)라 한다.

  ```python
  arr_2d = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]
  ]
  ```

<br/><br/>

## 2차원 리스트 입력

- n개의 줄에 걸쳐 n개의 숫자를 입력받을 때, 이 2차원 격자 모양의 입력값들을 그대로 담아야 할 필요가 있다.

- 이 때 2차원 리스트를 활용하면 좋다.

- 각 줄마다 입력을 받아 하나의 리스트로 만들고, 이를 2차원 리스트에 <code>append()</code> 함수를 이용하여 추가한다.

  ```python
  n = int(input())
  arr_2d = []

  for _ in range(n):
      arr_1d = list(map(int, input().split()))
      arr_2d.append(arr_1d)

  print(arr_2d)
  ```

<br/>

- 이 때 <code>list comprehension</code>을 이용하면 더 간단히 입력값을 처리할 수 있다.

- 단, for loop 안에 append만 사용하는 경우여야만 가능하다.

  ```python
  n = int(input())
  arr_2d = [
      list(map(int, input().split()))
      for _ in range(n)
  ]

  print(arr_2d)
  ```

<br/><br/>

## 2차원 리스트 선언

- 위에서 설명한 <code>list comprehension</code>을 통해 전부 0으로 초기화 된 2차원 배열을 선언해보자.

- n행 n열 격자

  ```python
  n = int(input())
  arr_2d = [
      [0] * n    # [0 for _ in range(n)]
      for _ in range(n)
  ]
  ```

  - n행 m열 격자

  ```python
  n, m = tuple(map(int, input().split()))
  arr_2d = [
      [0] * m
      for _ in range(n)
  ]
  ```

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

- 그러나 위처럼 1차원 리스트를 복사하여 2차원 리스트를 만들어주면, 복제된 모든 리스트가 같은 주소를 가리키게 된다.

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

## 2차원 리스트 출력

- 2차원 리스트의 모든 요소를 격자 모양대로 출력하고자 할 때 (입력값 받을 때 상태 그대로)

- 중첩 반복문을 활용하여 range 함수를 사용한다.

  ```python
  n, m = 4, 3
  arr_2d = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      [10, 11, 12]
  ]

  for i in range(n):
      for j in range(m):
          print(arr_2d[i][j], end=" ")
      print()
  ```

  ```
  1 2 3
  4 5 6
  7 8 9
  10 11 12

  ```

<br/>

- range 함수를 사용하지 않고 리스트 내 각 원소를 바로 접근하는 식으로도 표현이 가능하다.

- 2차원 배열의 원소는 각 행이 되며, 각 행에 있는 원소들을 조회하여 값을 출력해준다.

  ```python
  n, m = 4, 3
  arr_2d = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      [10, 11, 12]
  ]

  for row in arr_2d:
      for elem in row:
          print(elem, end=" ")
      print()
  ```

  ```
  1 2 3
  4 5 6
  7 8 9
  10 11 12

  ```

<br/><br/>

## 2차원 리스트 활용

### 2차원 배열과 규칙

<img src="img/python_2d_list1.png">

<br/>

### 2차원 배열과 for문

<img src="img/python_2d_list2.png">

<br/>

### 순서대로 채우기

<img src="img/python_2d_list3.png">

<br/>

### 2차 격자점으로서의 배열

<img src="img/python_2d_list4.png">
