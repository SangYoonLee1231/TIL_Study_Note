# Python - 1차원 리스트(배열) 활용

<br/>

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree - Novice Low</a>

<br/>

## 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_1d_list.md#1%EC%B0%A8%EC%9B%90-%EB%A6%AC%EC%8A%A4%ED%8A%B8">1차원 리스트</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_1d_list.md#1%EC%B0%A8%EC%9B%90-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%9E%85%EB%A0%A5-inputsplit-%ED%99%9C%EC%9A%A9%EB%B2%95">1차원 리스트 입력 (<code>input().split()</code>) 활용법</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_1d_list.md#%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1-slicing">리스트 슬라이싱 (Slicing)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_1d_list.md#%EC%9E%90%EC%A3%BC-%EC%93%B0%EC%9D%B4%EB%8A%94-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%ED%95%A8%EC%88%98-append-pop-len-sum-%ED%95%A8%EC%88%98">자주 쓰이는 리스트 함수 (append, pop, len, sum 함수)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_1d_list.md#%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EA%B0%92-%EC%B0%B8%EC%A1%B0">리스트 값 참조</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_1d_list.md#list-comprehension">List Comprehension</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_1d_list.md#%EC%9E%90%EC%A3%BC-%EC%93%B0%EC%9D%B4%EB%8A%94-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%ED%95%A8%EC%88%98-2-index-count-max-min-%ED%95%A8%EC%88%98">자주 쓰이는 리스트 함수 2 (index, count, max, min 함수)</a>

<br/>

## 1차원 리스트

- python에서 배열은 리스트를 사용한다.

- 리스트는 정보 여러 개를 하나의 변수처럼 사용하는 자료구조이다.

  ('자료구조' 카테고리의 『<a href="https://github.com/SangYoonLee1231/TIL/blob/main/DataStructure/array_and_list.md">순차적 자료구조 : 배열 vs 리스트</a>』 참고)

  ```python
  arr = [1, 2, 3, 4, 'Life', 'is', 'too', 'short']
  ```

<br/>

## 1차원 리스트 입력 (<code>input().split()</code> 활용법)

- <code>input().split()</code>으로 공백을 사이에 두고 주어지는 입력값을 나눠 받을 수 있다.

  ```python
  arr = input().split()

  print(arr)
  ```

  ```
  >> 1 3 5

  ['1', '3', '5']
  ```

<br/>

- 여기서 <code>map</code>을 활용하면, 입력받는 모든 값에 원하는 함수를 적용시킬 수 있다.

  ```python
  arr = list(map(int, input().split()))

  print(arr)
  ```

  ```
  >> 1 3 5

  [1, 3, 5]
  ```

<br/>

- 이 때, 입력받을 값의 개수가 고정되어 있으면, <code>list()</code>함수 대신 <code>tuple()</code>함수를 쓰는 것이 좋다. (unpacking 활용)

  ```python
  n, m = tuple(map(int, input().split()))

  print(n, m)
  ```

  ```
  >> 1 3

  1 3
  ```

<br/>

## 리스트 슬라이싱 (Slicing)

- 리스트에 대해 slice를 활용하면 일부 범위, 조건에 해당하는 원소들을 가져올 수 있다.

  ```
  배열 이름[start값:end값:step]
  ```

  ```python
  arr = [1, 2, 3, 4, 5]

  print(arr[1:3])     # [2, 3]
  print(arr[1:3:1])   # [2, 3]

  print(arr[2:])      # [3, 4, 5]
  print(arr[:3])      # [1, 2, 3]

  print(arr[3:0:-1])  # [4, 3, 2]
  print(arr[::-1])    # [5, 4, 3, 2, 1]
  print(arr[::2])     # [1, 3, 5]
  ```

<br/>

## 자주 쓰이는 리스트 함수 (append, pop, len, sum 함수)

- <code>append</code> 함수 : 리스트 맨 끝에 원소를 추가한다.

- <code>pop</code> 함수 : 리스트 맨 뒤에 있는 원소를 지우고 그 값을 반환한다.

- <code>len</code> 힘수 : 리스트의 원소 개수를 반환한다.

- <code>sum</code> 함수 : 리스트 안의 모든 원소의 합을 반환한다.

  ```python
  # 비어있는 리스트 선언
  arr = []    # 또는 arr = list()

  arr.append(1)    # arr = [1]
  arr.append(3)    # arr = [1, 3]
  arr.append(5)    # arr = [1. 3, 5]

  print(len(arr))  # 3
  print(sum(arr))  # 9

  a = arr.pop()
  print(f"a = {a}, arr = {arr}")     # a = 5, arr = [1, 3]

  print(len(arr))         # 2
  print(sum(arr[1:]))     # 3
  ```

  ```
  3
  9
  a = 5, arr = [1, 3]
  2
  3
  ```

<br/>

## 리스트 값 참조

- 리스트의 첫 번째 원소는 0번 index, 두 번째 원소는 1번 index, ... 와 같이 0번 index를 시작으로 리스트 원소 값을 조회할 수 있다.

- 다시 말해, 리스트에서 i번째 원소의 값을 얻으려면, <code>arr[i-1]</code>을 참조해야 한다.

  ```python
  arr = [1, 2, 3, 4, 5]

  print(arr[2])   # 3번째 원소
  print(arr[3])   # 4번째 원소
  ```

  ```
  3
  4
  ```

<br/>

- python에선 음수 index를 지원한다.

- arr[-1] == 끝에서 첫 번째 원소, arr[-2] == 끝에서 두 번째 원소, ...

  ```python
  arr = [1, 2, 3, 4, 5]

  print(arr[-1])
  print(arr[-2])
  ```

  ```
  5
  4
  ```

<br/>

## ✨List Comprehension

- 아래처럼 리스트를 선언하고 for문을 통해 입력값을 넣어주는 과정을, list comprehension을 통해 한 줄로 표현할 수 있다.

- 표현 방식이 삼항 연산자 표현 방식과 비슷하다.

  ```python
  arr = []
  for i in range(10):
      arr.append(i)
  ```

  ```python
  arr = [i for _ in range(10)]
  ```

  ```python
  arr = [1, 2, 3, 4]

  new_arr = []
  for elem in arr:
      new_arr.append(elem * elem)
  ```

  ```python
  arr = [1, 2, 3, 4]

  new_arr = [
      elem * elem
      for elem in arr
  ]
  ```

<br/>

### 조건문을 포함하는 list comprehension

    ```python
    arr = [1, 2, 3, 4]

    new_arr = []
    for elem in arr:
        if elem % 2 == 1:
            new_arr.append(elem)
    ```

    ```python
    arr = [1, 2, 3, 4]

    new_arr = [
        elem
        for elem in arr
        if elem % 2 == 1
    ]
    ```

<br/>

## 자주 쓰이는 리스트 함수 2 (index, count, max, min 함수)

### index 함수

- <code>index()</code> 함수는 어떤 값이 리스트의 몇 번째 index에 있는지를 알려주는 함수이다.

  ```python
  word = ['A', 'P', 'P', 'L', 'E']

  print(word.index('L'))
  ```

  ```
  3
  ```

<br/>

- 단, 존재하지 않는 원소에 대해 index 함수를 이용하면 Value Error가 발생한다

  ```python
  word = ['A', 'P', 'P', 'L', 'E']

  print(word.index('M'))
  ```

  ```
  ValueError: 'M' is not in list
  ```

<br/>

- 따라서 <code>in</code> 키워드를 통해 찾고자 하는 원소가 리스트에 있는지 먼저 확인하는 것이 좋다.

  ```python
  word = ['A', 'P', 'P', 'L', 'E']

  if 'M' in word:
      print(word.index('M'))
  else:
      print("There is no 'M'")
  ```

  ```
  There is no 'M'
  ```

<br/>

### count 함수

- 리스트에 어떤 원소가 몇 번 들어있는지는 <code>count</code> 함수를 통해 알 수 있다.

  ```python
  word = ['A', 'P', 'P', 'L', 'E']

  cnt = word.count('P')
  print(cnt)
  ```

  ```
  2
  ```

<br/>

- 물론 <code>count</code> 함수를 쓰지 않고도 구현할 수 있다.

  ```python
  word = ['A', 'P', 'P', 'L', 'E']

  cnt = 0
  for elem in word:
      if elem = 'P':
          cnt += 1

  print(cnt)
  ```

  ```
  2
  ```

<br/>

### max, min 함수

- python에서 리스트 내의 숫자들 중 최댓값 혹은 최솟값을 쉽고 간단히 구하는 방법은 <code>max</code> 함수 혹은 <code>min</code> 함수를 쓰는 것이다.

  ```python
  arr = [1, 5, 2, 5, 3, 9]

  print(max(arr))
  print(min(arr))
  ```

  ```
  9
  1
  ```

<br/>

- 위 함수들을 쓰지 않고 직접 구현하는 것도 가능하다.

  ```python
  import sys

  arr= [1, 5, 2, 5, 3, 9]


  # 최댓값 구하기
  max_val = -sys.maxsize
  for elem in arr:
      if elem > max_val:
          max_val = elem

  print(max_val)


  # 최솟값 구하기
  min_val = sys.maxsize
  for elem in arr:
      if elem < min_val:
          min_val = elem

  print(min_val)
  ```

  ```
  9
  1
  ```
