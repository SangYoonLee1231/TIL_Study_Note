# Python - 문자열 다루기

<br/>

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree - Novice Low</a>

<br/>

## 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9E%85%EC%B6%9C%EB%A0%A5-%EA%B8%B0%EB%B3%B8-%EB%B0%A9%EB%B2%95">문자열 입출력 기본 방법</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%98-%EB%AC%B8%EC%9E%90-%EC%B0%B8%EC%A1%B0%ED%95%98%EA%B8%B0">문자열의 문자 참조하기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%98-%EA%B8%B8%EC%9D%B4">문자열의 길이</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%A6%AC%EC%8A%A4%ED%8A%B8">문자열 리스트 (+ 문자열 리스트로 입력 받기)</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EA%B3%B5%EB%B0%B1-%EB%8B%A8%EC%9C%84%EB%A1%9C-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9E%85%EB%A0%A5%EB%B0%9B%EA%B8%B0">공백 단위로 문자열 입력받기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%88%9C%ED%9A%8C%ED%95%98%EA%B8%B0">문자열 순회하기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B6%99%EC%9D%B4%EA%B8%B0">문자열 붙이기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%ED%8A%B9%EC%A0%95-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%B4-%ED%8F%AC%ED%95%A8%EB%90%9C-%EA%B2%BD%EC%9A%B0">특정 문자열이 포함된 경우</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%82%B4-%EB%AC%B8%EC%9E%90-%EC%88%98%EC%A0%95%ED%95%98%EA%B8%B0">문자열 내 문자 수정하기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%82%B4-%EB%AC%B8%EC%9E%90-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0">문자열 내 문자 제거하기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9A%B0%EC%B8%A1%EC%9C%BC%EB%A1%9C-%EB%B0%80%EA%B8%B0">문자열 우측으로 밀기</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EC%95%84%EC%8A%A4%ED%82%A4-%EC%BD%94%EB%93%9C">아스키 코드</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%ED%98%95%EB%B3%80%ED%99%98">문자열 형변환</a>
- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_string.md#%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B9%84%EA%B5%90">문자열 비교</a>

<br/>

## 문자열 입출력 기본 방법

- <code>input()</code>함수를 통해 입력 받고, <code>print()</code>함수를 통해 출력한다.

```python
sentence = input()
print(sentence)
```

```
>> hello

hello
```

<br/>

## 문자열의 문자 참조하기

- 문자열은 마치 1차원 배열과 같아, 문자열의 n번째 문자를 참조하기 위해선 n-1번지를 참조하면 된다.

```python
sentence = input()

print(sentence[0])
print(sentence[1])
print(sentence[-1])
```

```
>> hello

h
e
o
```

<br/>

- 문자열 출력 시 번지를 <strong>음수</strong>로 주면, 문자열의 뒤에서부터 출력할 수 있다.

```python
arr = "hello"

print(arr[-1])
print(arr[-3:])
```

```
o
llo
```

<br/>

## 문자열의 길이

- <code>len()</code>함수를 이용하면 된다.

- 이 때, 공백과 개행문자 <code>\n</code>도 길이에 포함된다.

```python
sentence = "hello world\n"

print(len(sentence))
```

```
12
```

<br/>

## 문자열 리스트

- 여러 문자열을 각각의 원소로 갖는 리스트를 정의하면 문자열을 목록으로 관리할 수 있다.

- 문자열의 리스트는 2차원 배열처럼 동작한다.

```python
arr = ["hello", "world", "python"]

print(arr[0])
print(len(arr[0]), end="\n\n")

print(arr[0][0])
print(arr[0][1])
print(arr[0][2])
```

```
hello
5

h
e
l
```

<br/>

### 여러 문자열을 입력 받아 문자열 리스트 만들기

- 방법1. for문을 이용하여 문자열을 하나씩 리스트에 append 하기

```python
n = 5
arr = []

for _ in range(n):
    given_str = input()
    arr.append(given_str)
```

<br/>

- 방법2. <code>list comprehension</code>을 통해 구현

```python
n = 5
arr = [
    input()
    for _ in range(n)
]
```

<br/>

## 공백 단위로 문자열 입력받기

- <code>split()</code>함수룰 이용하면 입력받은 문자열이 공백 단위로 쪼개져 리스트로 만들어진다.

  ```python
  arr = input().split()

  print(arr)
  ```

  ```
  >> hello world python

  ['hello', 'world', 'python']
  ```

<br/>

- list 힘수와 map 함수를 추가로 사용해도 된다.

  ```python
  arr = list(map(str, input().split()))
  ```

<br/>

- tuple을 사용하면, 리스트 필요 없이 두 변수에 문자열을 공백 단위로 잘라 받을 수 있다.

  ```python
  a, b = tuple(input().split())
  print(a)
  print(b)
  ```

  ```
  >> hello world

  hello
  world
  ```

<br/>

## 문자열 순회하기

- for문을 통해 문자열의 길이를 구하지 않고 바로 원소에 접근할 수 있다.

  ```python
  sentence = input()

  for i in sentence:
      print(i)
  ```

  ```
  >> hello

  h
  e
  l
  l
  o
  ```

<br/>

## 문자열 붙이기

- 문자열끼리 <code>+</code>연산을 통해 붙여줄 수 있다.

  ```python
  a, b = "hello", "world"

  print(a + b)
  ```

  ```
  helloworld
  ```

    <br/>

  ```python
  a, b, c = "hello", "world", "python"
  sentence = ""

  sentence += a
  sentence += b
  sentence += c

  print(sentence)
  ```

  ```
  helloworldpython
  ```

    <br/>

  ```python
  a, b, c = "hello", "world", "python"
  sentence = ""

  for target_str in [a, b, c]:
      sentence += target_str

  print(sentence)
  ```

  ```
  helloworldpython
  ```

<br/>

- <code>join()</code>함수는 지정한 구분값(<code>sep</code>)을 각 원소 사이에 삽입하여 하나의 문자열로 합쳐준다.

- <code>join()</code>함수를 이용하면 여러 문자열을 더 쉽게 연결할 수 있다.

  ```python
  a, b, c = "hello", "world", "python"
  sentence = "".join([a, b, c])

  print(sentence)
  ```

  ```
  helloworldpython
  ```

    <br/>

  ```python
  print(','.join(['hello', 'world', 'python']))
  print(':'.join(['hello', 'world', 'python']))
  print(''.join(['hello', 'world', 'python']))
  ```

  ```
  hello,world,python
  hello:world:python
  helloworldpython
  ```

<br/>

## 특정 문자열이 포함된 경우

### 특정 문자열 포함 여부 확인하기

- <code>in</code> 키워드를 통해 어떤 문자열에 특정 문자열이 포함되어 있는지 쉽게 알 수 있다.

  ```python
  s = 'helloworld'

  print('owo' in s)
  ```

  ```
  True
  ```

    <br/>

  - 물론 이 키워드를 사용하지 않고 반복문과 조건문으로도 구현할 수 있다.

  - slicing을 이용하면 좋다.

  ```python
  s = 'helloworld'

  length = len(s)
  exists = False

  for i in range(length - 2):
      if s[i:i+3] == 'owo':
          exists = True;

  print(exists)
  ```

<br/>

### 포함된 특정 부분 문자열의 위치 구하기

- <code>index</code> 함수를 이용하면 특정 부분 문자열이 등장하는 위치를 구할 수 있다.

- 단, 찾고자 하는 부분 문자열이 없으면 ValueError이 발샐하므로, 아래처럼 <code>in</code> 키워드를 함께 사용해야 한다.

  ```python
  s = 'helloworld'

  if 'owo' in s:
      print(s.index('owo'))
  else:
      print(-1)
  ```

  ```
  4
  ```

<br/>

- 사실, 파이썬에선 <code>find()</code> 함수를 통해 위의 문제를 더 간단히 해결할 수 있다.

- <code>find()</code> 함수는 해당 부분자열이 없을 경우 -1을, 있을 경우 가장 앞에 나오는 부분 문자열의 위치를 반환한다.

  ```python
  s = 'helloworld'

  print(s.find('owo'))
  print(s.find('ooo'))
  ```

  ```
  4
  -1
  ```

<br/>

## 문자열 내 문자 수정하기

- python에서 문자열은 <code>immutable</code>, 즉 변할 수 없는 타입이기 때문에 내부 문자를 변경하는 것이 불가능하다.

- 그러나,

1. 아예 새로운 문자열을 만들거나,
2. 문자열을 리스트로 변환하는 방법

   으로 내부 문자를 바꿀 수 있다.

<br/>

### 새로운 문자열을 만들어 해결하는 방법

- <code>slicing</code>을 통해 수정할 문자의 새 값과, 양 옆의 두 부분 문자열을 서로 합친다.

  ```python
  s = 'click'

  s = s[:2] + 'o' + s[3:]

  print(s)
  ```

  ```
  clock
  ```

<br/>

### 각 문자를 원소로 갖는 리스트로 변환하여 해결하는 방법

- 문자열을 <code>list()</code> 함수로 감싸 리스트로 만들고,

- 수정할 문자를 index로 접근, 새 문자를 대입 후,

- <code>join()</code> 함수를 통해 다시 문자열로 합친다.

  ```python
  s = 'click'

  arr = list(s)
  arr[2] = 'o'
  s = ''.join(arr)

  print(s)
  ```

  ```
  clock
  ```

<br/>

## 문자열 내 문자 제거하기

- 위의 '문자열 내 문자 수정하기'와 비슷한 방법으로 해결하면 된다.

<br/>

1. slicing을 통해 지워져야 할 문자의 양쪽 문자열만 따로 살려서 이어 붙인다.

   ```python
   s = 'three'

   s = s[:1] + s[2:]
   print(s)
   ```

   ```
   tree
   ```

<br/>

2. 다른 방법으로, 문자열을 리스트로 변환한 후 <code>pop</code> 함수를 이용해 해당 문자를 제거한 후 다시 문자열로 변환한다.

   ```python
   s = 'three'

   arr = list(s)
   arr.pop(1)
   s = ''.join(arr)

   print(s)
   ```

   ```
   tree
   ```

<br/>

## 문자열 우측으로 밀기

- <code>slicing</code>을 통해 다음과 같이 구현할 수 있다.

  ```python
  s = 'earth'

  s = s[-1] + s[:-1]

  print(s)
  ```

  ```
  heart
  ```

<br/>

## 아스키 코드

- python에서 사용할 수 있는 모든 문자들은 각각 하나의 숫자에 대응한다. 이를 아스키 코드라 한다.

- python에서 특정 문자의 아스키 코드 값은 <code>ord()</code> 함수를 통해 알 수 있다.

  ```python
  print(ord('A'))
  print(ord('B'))
  ```

  ```
  65
  66
  ```

<br/>

- 반대로, 아스키 코드 값이 어떤 문자에 대응하는 지도 <code>chr()</code> 함수를 통해 알 수 있다.

  ```python
  print(chr(65))
  print(chr(66))
  ```

  ```
  A
  B
  ```

<br/>

- 알파벳 대문자, 소문자 끼리는 연속된 숫자들로 아스키 코드 값이 매칭 되어있다.

<br/>

### 아스키 코드로 문자 바꾸기

- 아스키 코드를 통해 대소문자 변환을 쉽게 할 수 있다.

  ```python
  X = 'B'

  num_x = ord(X) - ord('A') + ord('a')    # 99

  print(chr(num_x))
  ```

  ```
  b
  ```

<br/>

- 물론, <code>upper()</code> 함수와 <code>lower</code> 함수를 통해 대소문자를 변환해도 된다.

  ```python
  x = 'B'

  print(x.lower())
  ```

  ```
  b
  ```

    <br/>

  ```python
  x = 'b'

  print(x.upper())
  ```

  ```
  B
  ```

<br/>

- 아스키 코드를 통해 그 다음 알파벳을 바로 구할수도 있다.

  ```python
  x = 'A'

  print(ord(x))
  print(ord(x) + 1)
  print(chr(ord(x) + 1))
  ```

  ```
  65
  66
  B
  ```

<br/>

- 문자열 끼리는 서로 비교가 가능하며, 아스키 코드 번호 순으로 비교된다.

  ```python
  # 문자 x가 대문자인지 확인하는 코드
  x = input()

  if 'A' <= x and x <= 'Z':
      print("Upper Case")
  ```

  ```
  >> B

  Upper Case
  ```

<br/>

- 문자열이 전부 알파벳인지 혹은 전부 숫자인지 확인하려면, <code>isalpha</code> 함수 혹은 <code>isdigit</code> 함수를 사용하면 된다.

  ```python
  print("abcg".isalpha())
  print("abc3".isalpha())

  print("1234".isdigit())
  print("123g".isdigit())
  ```

  ```
  True
  False

  True
  False
  ```

<br/>

## 문자열 형변환

- 숫자로 이루어진 문자열을 정수로 변환하기 위해선 <code>int()</code> 함수로 감싸주면 된다.

  ```python
  a = '123'

  a = int(a) + 1

  print(a)
  ```

  ```
  124
  ```

<br/>

- 반대로, 정수를 문자열로 변환하기 위해선 <code>str()</code> 함수로 감싸주면 된다.

  ```python
  a = 123

  a = str(a) + '456'

  print(a)
  ```

  ```
  123456
  ```

<br/>

## 문자열 비교

- python에선 두 문자열이 동일한 지 비교하기 위해 숫자 비교처럼 <code>==</code> 연산자를 사용하면 된다.

  ```python
  print('cat' == 'cat')
  print('dog' == 'cat')
  ```

  ```
  True
  False
  ```

<br/>

- <code><</code>,<code>></code> 연산을 통해 사전순으로 앞선 문자열이 무엇인지 알 수 있다. 값이 작을수록 사전순으로 앞서다는 것을 의미한다.

  ```python
  print('abc' < 'bc')
  print('abc' < 'd')
  ```

  ```
  True
  False
  ```
