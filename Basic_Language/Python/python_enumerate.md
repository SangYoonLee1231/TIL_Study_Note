# <code>enumerate</code>, <code>zip</code> 함수

## <code>enumerate</code> 함수

- <code>enumerate</code> 함수는 for문을 돌 때 각 원소와 동시에 index를 뽑아주는 역할을 하는 함수이다.

  ```python
  arr = [10, 20, 30, 40, 50]

  for i, elem in enumerate(arr):
      print(i, elem)
  ```

  ```
  0 10
  1 20
  2 30
  3 40
  4 50
  ```

<br/>

- <code>enumerate</code> 함수에 start값을 인자로 넘기면 시작 index값을 설정할 수 있다.

  ```python
  arr = [10, 20, 30, 40, 50]

  for i, elem in enumerate(arr, start=1):
      print(i, elem)
  ```

  ```
  1 10
  2 20
  3 30
  4 40
  5 50
  ```

<br/>

## <code>zip</code> 함수

- <code>zip</code> 함수는 for문을 돌 때 2개의 리스트를 동시에 순회하여, 각 원소를 함께 뽑아주는 함수이다.

  ```python
  arr1 = [1, 2, 3, 4, 5]
  arr2 = [6, 7, 8, 9, 10]

  for elem1, elem2 in zip(arr1, arr2):
    print(elem1, elem2)
  ```

  ```
  1 6
  2 7
  3 8
  4 9
  5 10
  ```

<br/>

- 만일 <code>zip</code> 함수의 인자로 들어간 두 리스트의 길이가 다르다면, 더 짧은 리스트의 길이만큼만 원소를 추출하고 나머지는 무시된다.

  ```python
  arr1 = [1, 2, 3, 4, 5, 6, 7]
  arr2 = [8, 9, 10, 11, 12]

  for elem1, elem2 in zip(arr1, arr2):
    print(elem1, elem2)
  ```

  ```
  1 8
  2 9
  3 10
  4 11
  5 12
  ```
