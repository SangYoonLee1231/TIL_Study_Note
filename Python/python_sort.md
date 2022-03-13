# Python - 정렬 내장 함수 <code>sort</code>, <code>sorted</code>

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_sort.md#%EC%88%AB%EC%9E%90-%EC%A0%95%EB%A0%AC">숫자 정렬</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_sort.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%82%B4-%EB%AC%B8%EC%9E%90-%EC%A0%95%EB%A0%AC">문자열 내 문자 정렬</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_sort.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%A0%95%EB%A0%AC">문자열 리스트 정렬</a>
- <a href="">객체 정렬</a>
  - <a href="">class를 이용한 객체 정렬</a>
  - <a href="">tuple을 이용한 객체 정렬</a>
- <a href="">객체 정렬 응용</a>
  - <a href="">여러 우선순위를 갖는 객체 정렬</a>
  - <a href="">정렬 기준이 복잡한 객체 정렬</a>
  - <a href="">객체 정렬시 index 맴버 변수의 필요성</a>

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

<br/><br/>

## 객체 정렬

### 객체 정렬의 중요성

- ✨ 정렬를 하려고 하는데 각 특징 별로 리스트를 만들어 관리하면, 이 중 하나의 특징을 기준으로 정렬하려고 할 때 다른 리스트는 값의 위치는 함께 변하지 않으므로 정보를 객체로 관리하는 것이다.

<br/>

### lambda 함수

- 이름 없이 사용할 수 있는 일회성 함수

  ```
  lambda 입력값: 반환값(계산식)
  ```

<br/>

- 아래의 함수 코드를 예시로 보자.

  ```python
  def f(x):
      return x * 2

  print(f(3))
  ```

  ```
  6
  ```

<br/>

- 위의 f(x) 함수를 lambda 함수로 선언하면 아래과 같다.

  ```python
  f = lambda x: x + 2

  print(f(3))
  ```

  ```
  6
  ```

<br/>

- lambda 함수는 객체 정렬에 유용하게 쓰인다.

<br/>

### class를 이용한 객체 정렬

- 국어, 영어, 수학 점수를 포함한 학생 5명의 정보가 주어졌을 때, 국어 점수를 기준으로 오름차순 정렬하는 프로그램을 작성하고자 한다.

<br/>

- 먼저 각각의 학생 정보를 객체로 선언한 후, <code>sort</code> 함수에 <code>key</code>라는 정렬 기준 정의 함수를 넘겨주어 객체들을 정렬한다.

* 이 때, 익명 함수 <code>lambda</code>를 이용한다.

  ```python
  class Student:
      def __init__(self, kor, eng, math):
      self.k = kor
      self.e = eng
      self.m = math

  students = [
      Student(90, 80, 90), # 첫 번째 학생
      Student(20, 80, 80), # 두 번째 학생
      Student(90, 30, 60), # 세 번째 학생
      Student(60, 10, 50), # 네 번째 학생
      Student(80, 20, 10) # 다섯 번째 학생
  ]

  # 국어 점수 기준 오름차순 정렬
  students.sort(key=lambda x: x.kor)

  # 정렬 이후의 결과 출력
  for student in students:
      print(student.kor, student.eng, student.math)
  ```

  ```
  20 80 80
  60 10 50
  80 20 10
  90 80 90
  90 30 60
  ```

* 이 때 국어 점수가 90점으로 동일한 두 학생의 경우에는, 어떤 학생이 더 앞서서 나오게 되는지는 모호하게 된다.

* 이런 경우에는 보다 더 명확한 기준이 필요할 수 있다.

<br/>

#### <code>students.sort(key=lambda x: x.kor)</code> 동작 원리

- ✨ 그럼 여기서 다음 코드의 동작 원리를 알아보자.

  ```python
  students.sort(key=lambda x: x.kor)
  ```

- 우선, 숫자 리스트 정렬을 위해 <code>sort()</code> 함수를 이용하는 경우부터 살펴본다.

* <code>sort()</code> 함수가 실행되면, 아래처럼 리스트의 값들을 서로 비교하며 값들의 위치를 바꾸는 (정렬하는) 과정이 일어난다.

  ```python
  numbers = [1, 34, 2, 1, 4 , 34, 34]
                    n1, n2
                    if n1 < n2:
  ```

- 그럼 객체 리스트를 정렬하는 경우를 보자.

* 위의 <code>students.sort(key=lambda x: x.kor)</code> 코드를 해석하면, <code>lambda</code> 함수의 입력값 x으로 리스트의 각 객체가 들어가면서 각각의 x.kor 값(국어 점수)들이 반환되고, 이는 오름차순 정렬을 위한 비교에 쓰일 대표값들이 된다.

  ```python
  students = [Student(90, 80, 90), Student(20, 80, 80), Student(90, 30, 60), ... ]
                      x1                   x2
                        if key(x1) < key(x2):
  ```

- 이제 <code>sort</code> 함수는 각 객체들의 x.kor 값들을 비교하며 객체들을 정렬한다.

<br/>

- 반대로 객체들을 내림차순으로 정렬하려면, <code>lambda</code> 함수의 반환값인 x.kor을 음수로 바꿔주면 된다.

  ```python
  students.sort(key=lambda x: -x.kor)
  ```

<br/>

### tuple을 이용한 객체 정렬

- tuple로 각 학생의 정보를 나타났을 때의 정렬 또한 <code>sort</code> 함수와 <code>lambda</code> 함수를 이용하면 된다.

* 다만, 이 경우엔 x값이 하나의 학생에 해당하는 tuple 값을 갖고 있기 때문에, x 학생의 국어 점수에 해당하는 <code>x[0]</code>을 lambda 함수의 반환 값으로 적어줘야 한다.

  ```python
  students = [
      (90, 80, 90), # 첫 번째 학생
      (20, 80, 80), # 두 번째 학생
      (90, 30, 60), # 세 번째 학생
      (60, 10, 50), # 네 번째 학생
      (80, 20, 10), # 다섯 번째 학생
  ]

  # 국어 점수 기준 오름차순 정렬
  students.sort(key=lambda x: x[0])

  # 정렬 이후의 결과 출력
  for student in students:
      kor, eng, math = student
      print(kor, eng, math)
  ```

  ```
  20 80 80
  60 10 50
  80 20 10
  90 80 90
  90 30 60
  ```

<br/>

- 이 때 tuple을 원소로 하는 students 리스트를 순회할 때, 다음과 같이 for loop와 함께 unpacking을 진행하면 더 깔끔한 코드를 작성할 수 있다.

  ```python
  for kor, eng, math in students:
      print(kor, eng, math)
  ```

  <br/>

* 사람 이름과 같이 문자열을 맴버 변수로 갖는 객체에 대해 해당 문자열을 기준으로 정렬할 때도 <code>sort</code> 함수와 <code>lambda</code> 함수를 이용하면 된다.

* 이 떄는 사전순으로 정렬이 이루어진다.

```python
students = [
    ("lee", 80, 90), # 첫 번째 학생
    ("kim", 80, 80), # 두 번째 학생
    ("park", 30, 60), # 세 번째 학생
]

students.sort(key=lambda x : x[0])

for name, eng, math in students:
    print(name, eng, math)
```

```
kim 80 80
lee 80 90
park 30 60
```

<br/><br/>

## 객체 정렬 응용

- 코딩테스트에선 class보단 주로 tuple을 쓰므로, 지금부터는 편의상 tuple을 이용한 객체 정렬만을 다룬다.

<br/>

### 여러 우선순위를 갖는 객체 정렬

- 국어, 영어, 수학 점수를 포함한 학생 5명의 정보가 주어졌을 때, 국어 점수를 기준으로 오름차순 정렬하되, 국어 점수가 같으면 영어 점수를 기준 <strong>내림차순</strong>으로, 영어 점수도 같으면 수학 점수를 기준 <strong>내림차순</strong>으로 정렬하는 프로그램을 작성하고자 한다.

- 이처럼 <strong>여러 우선순위</strong>를 갖는 경우면, <strong>lambda 함수의 반환값을 단일 값이 아닌 tuple값으로 정의</strong>해주면 된다.

- tuple끼리 비교연산을 할 때, 첫 원소를 기준으로 우선 비교하고, 동일하면 다음 원소를 기준으로 비교하는 식으로 진행하기 때문이다.

  ```python
  print((2, 3) > (1, 9))

  print((2, 3) > (2, 8))
  ```

  ```
  True
  False
  ```

  <br/>

  - 그럼 주어진 문제의 코드를 작성해보자.

  ```python
  students = [
      (90, 80, 90), # 첫 번째 학생
      (20, 80, 80), # 두 번째 학생
      (90, 30, 60), # 세 번째 학생
      (60, 10, 50), # 네 번째 학생
      (80, 20, 10), # 다섯 번째 학생
  ]

  students.sort(key=lambda x: (x[0], -x[1], -x[2])

  for student in students:
      kor, eng, math = student
      print(kor, eng, math)

  '''
  # 언팩킹의 성질을 이용하여 출력 코드를 더욱 단순화 할 수 있다.
  for kor, eng, math in students:
      print(kor, eng, math)
  '''
  ```

  ```
  20 80 80
  60 10 50
  80 20 10
  90 80 90
  90 30 60
  ```

<br/>

### 정렬 기준이 복잡한 객체 정렬

- 국어, 영어, 수학 점수를 포함한 학생 5명의 정보가 주어졌을 때, 이번엔 점수의 <strong>총합</strong>을 기준으로 오름차순 정렬하는 프로그램을 작성해보려 한다.

- 이렇게 정렬 기준의 맴버 변수가 이닐 땐, <strong>원하는 기준에 맞게 lambda 함수의 반환값을 설정</strong>해주면 된다.

- 이 문제에선 '점수의 총합'을 기준으로 정렿해야 하므로, lambda 함수의 반환값을 각 학생 객체의 모든 요소의 합으로 설정한다.

  ```python
  students = [
      (90, 80, 90), # 첫 번째 학생
      (20, 80, 80), # 두 번째 학생
      (90, 30, 60), # 세 번째 학생
      (60, 10, 50), # 네 번째 학생
      (80, 20, 10), # 다섯 번째 학생
  ]

  student.sort(key=lambda x: x[0] + x[1] + x[2])

  # 언팩킹 성질을 이용해 단순화
  for kor, eng, math in students:
      print(kor, eng, math)
  ```

  ```
  80 20 10
  60 10 50
  20 80 80
  90 30 60
  90 80 90
  ```

<br/>

- (참고)

  <img src="img/class_sort1.png">

  ```python
  from functools import cmp_to_key

  students = [
      Student(90, 80, 90), # 첫 번째 학생
      Student(20, 80, 80), # 두 번째 학생
      Student(90, 30, 60), # 세 번째 학생
      Student(60, 10, 50), # 네 번째 학생
      Student(80, 20, 10), # 다섯 번째 학생
  ]

  # custom comparator를 직접 정의
  # x가 앞에 있는 학생, y가 뒤에 있는 학생이라 가정했을 때
  # 이 순서가 우리가 원하는 순서라면 0보다 작은 값을,
  # 반대라면 0보다 큰 값을
  # 둘의 우선순위가 동일하다면 0을 반환하면 됩니다.
  # 보통 반환값에 1, -1, 0을 사용합니다.
  def compare(x, y):
      # x만 30의 배수라면 x가 더 앞에 있어야 하므로
      # 현재 순서가 옳습니다.
      if x.kor % 30 == 0 and y.kor % 30 != 0:
          return -1
      # y만 30의 배수라면 y가 더 앞에 있어야 하므로
      # 현재 순서는 틀렸습니다.
      if x.kor % 30 != 0 and y.kor % 30 == 0:
          return 1
      # 우선 순위가 동일한 경우입니다.
      return 0

  # 점수의 총합 기준 오름차순
  students.sort(key=cmp_to_key(compare))

  for student in students: # 정렬 이후의 결과 출력
      print(student.kor, student.eng, student.math)

  >> 90 80 90
     90 30 60
     60 10 50
     20 80 80
     80 20 10
  ```

<br/>

### 객체 정렬시 index 맴버 변수의 필요성

- 국어, 영어, 수학 점수를 포함한 학생 5명의 정보가 주어졌을 때, 국어 점수를 기준으로 내림차순으로 정렬하고, 1등부터 5등까지 <strong>각 등수에 해당하는 학생의 번호를 출력</strong>하는 프로그램을 작성하려 한다.

- 이런 경우라면, 학생의 정보에 학생 번호에 해당하는 맴버 변수를 같이 저장해 두어야 정렬하는 과정에 번호가 함께 이동하여 원하는 결과를 출력해낼 수 있다.

- 참고로 등수별 학생의 번호를 깔끔하게 출력하기 위해 for loop 진행시 각 원소와 동시에 index를 뽑아주는 <code>enumerate</code> 함수를 사용하면 좋다.

  - <code>enumerate</code> 함수에 대한 설명 및 사용법은 아래 링크에 정리해두었다.

  - <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_enumerate.md">Python - <code>enumerate</code> 함수</a>

<br/>

- 그럼 주어진 문제의 코드를 작성해보자.

  ```python
  students = [
      (90, 80, 90, 1), # 첫 번째 학생
      (20, 80, 80, 2), # 두 번째 학생
      (90, 30, 60, 3), # 세 번째 학생
      (60, 10, 50, 4), # 네 번째 학생
      (80, 20, 10, 5), # 다섯 번째 학생
  ]

  students.sort(key=lambda x: -x[0])

  for idx, (_, _, _, number) in enumerate(students, start=1):
      print(f"{idx}등: {number}번")
  ```

  ```
  1등 : 1번
  2등 : 3번
  3등 : 5번
  4등 : 4번
  5등 : 2번
  ```

<br/>

- 만일 1등부터 5등까지 각 등수에 해당하는 번호를 차례대로 출력하는 것이 아니라 <strong>1번부터 5번까지 각 번호의 학생의 등수를 순서대로 출력하는 문제</strong>라면 어떻게 해야 할까.

* 그런 경우엔 우선 학생을 등수대로 정렬하고, 새로운 배열을 생성한 다음 'index값 = 학생 번호'에 맞춰 값을 넣어주는 식으로 코드를 작성하면 된다.

  - 예를 들어 1등이 4번이라면, 새로운 배열의 인덱스 4인 공간에 값 1(등)을 넣어준다.

```python
  students = [
      (90, 80, 90, 1), # 첫 번째 학생
      (20, 80, 80, 2), # 두 번째 학생
      (90, 30, 60, 3), # 세 번째 학생
      (60, 10, 50, 4), # 네 번째 학생
      (80, 20, 10, 5), # 다섯 번째 학생
  ]

  students.sort(key=lambda x: -x[0])

  num_to_rank = [0] * 5

  for rank, student in enumerate(students, start=1):
      num_to_rank[student[3]-1] = rank

  for idx, elem in enumerate(num_to_rank, start=1):
      print(f"{idx}번: {elem}등")
```
