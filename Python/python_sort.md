# Python - 정렬 내장 함수 <code>sort</code>, <code>sorted</code>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_sort.md#%EC%88%AB%EC%9E%90-%EC%A0%95%EB%A0%AC">숫자 정렬</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_sort.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%82%B4-%EB%AC%B8%EC%9E%90-%EC%A0%95%EB%A0%AC">문자열 내 문자 정렬</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_sort.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A0%95%EB%A0%AC">문자열 리스트 정렬</a>

<br/>

## 숫자 정렬

- python3에서 n개의 숫자를 오름차순으로 정렬하는 가장 쉽고 빠른 방법은 <code>sort()</code> 내장 함수를 사용하는 것이다.

  ```python
  arr = [12, 41, 37, 81, 19, 25, 60, 20]

  arr.sort()

  print(arr)
  ```

  ```
  [12, 19, 20, 25, 37, 41, 60, 81]
  ```

<br/>

- <code>sort()</code> 함수는 기본적으로 <strong>오름차순</strong>으로 정렬한다.

* 반대로 <code>sort()</code> 함수를 통해 n개의 숫자를 내림차순으로 정렬하는 방법은, <code>sort()</code> 함수에 <code>reverse=True</code> 옵션을 붙여주는 것이다.

  ```python
  arr = [12, 41, 37, 81, 19, 25, 60, 20]

  arr.sort(reverse=True)

  print(arr)
  ```

  ```
  [81, 60, 41, 37, 25, 20, 19, 12]
  ```

* 또는 리스트 슬라이싱을 통해 오름차순으로 정렬된 리스트를 뒤집는 방식으로 내림차순 정렬을 구현할 수도 있다.

  ```python
  arr = [12, 41, 37, 81, 19, 25, 60, 20]

  arr.sort()
  arr_new = arr[::-1]

  print(arr_new)
  ```

  ```
  [81, 60, 41, 37, 25, 20, 19, 12]
  ```

<br/>

- 정렬에 이용할 수 있는 함수는 sort()와 비슷한 <code>sorted()</code> 함수도 있다.

- 단. <code>sorted()</code> 함수는 정렬된 리스트를 반환하는 함수이므로, 정렬 이후의 리스트를 변수에 할당해줘야 한다.

  ```python
  arr = [12, 41, 37, 81, 19, 25, 60, 20]

  arr_new = sorted(arr)

  print(arr_new)
  ```

  ```
  [12, 19, 20, 25, 37, 41, 60, 81]
  ```

<br/>

- 또한 반대로 <code>sorted()</code> 함수를 통해 n개의 숫자를 내림차순으로 정렬하는 방법은, 리스트를 뒤집어주는 <code>reversed()</code> 함수로 감싸주는 것이다.

* 다만, <code>reversed()</code> 함수를 사용 시 다시 list로 감싸주어야 뒤집어진 list를 얻을 수 있다.

  ```python
  arr = [12, 41, 37, 81, 19, 25, 60, 20]

  arr_new = sorted(arr)
  arr_new = list(reversed(arr_new))

  print(arr_new)
  ```

  ```
  [12, 19, 20, 25, 37, 41, 60, 81]
  ```

<br/><br/>

## 문자열 내 문자 정렬

- 문자열 내 문자를 알파벳 순으로 정렬하려 한다.

<br/>

- 하지만 숫자 정렬에 사용했던 <code>sort()</code> 함수는 문자열에 사용할 수 없다.

* 대신, 문자열을 리스트로 변환 후 <code>sort()</code> 함수를 사용하면 정렬이 가능하다.

* 정렬 이후엔 list를 다시 문자열로 만들어준다. 이 때는 <code>join()</code> 함수를 이용하면 된다.

  ```python
  string = "banana"
  #string.sort()   # 에러 발생

  lst = list(string)
  lst.sort()
  print(lst)

  string = ''.join(lst)
  print(string)
  ```

  ```
  ['a', 'a', 'a', 'b', 'n', 'n']
  aaabnn
  ```

- 참고로, <code>join()</code>도, <code>list()</code>도 결과값을 반환하는 함수이므로 변수에 할당해서 선언해야 한다.

<br/>

- <code>sorted()</code> 함수는, sort() 함수와 달리 문자열을 함수 인자로 넣더라도 이를 성공적으로 반환해준다.

* 단, sort() 함수처럼 리스트로 반환해주기 때문에, <code>join()</code> 함수를 통해 다시 문자열로 바꿔주어야 한다.

  ```python
  string = "banana"

  lst = sorted(string)
  print(lst)

  string = ''.join(lst)

  print(string)
  ```

  ```
  ['a', 'a', 'a', 'b', 'n', 'n']
  aaabnn
  ```

<br/><br/>

## 문자열 리스트 정렬

- 문자열들이 저장된 문자열 리스트의 문자열들을 사전순으로 정렬하려 한다.

<br/>

- 이 역시 리스트이므로, <code>sort()</code> 함수 또는 <code>sorted()</code> 함수를 통해 구현할 수 있다.

* 내림차순 정렬도 마찬가지로 <code>sort()</code> 함수에 <code>reverse=True</code> 옵션을 달거나 <code>sorted()</code> 함수에 <code>reversed()</code> 함수로 감싸서 구현하면 된다.

  ```python
  words = ["banana", "apple", "cat", "app"]


  sorted_words = sorted(words)
  print(sorted_words)

  words.sort()
  print(words)


  reverse_sorted_words = list(reversed(sorted(words)))
  print(reverse_sorted_words)

  words.sort(reverse=True)
  print(words)
  ```

  ```
  ['app', 'apple', 'banana', 'cat']
  ['app', 'apple', 'banana', 'cat']
  ['cat', 'banana', 'apple', 'app']
  ['cat', 'banana', 'apple', 'app']
  ```
