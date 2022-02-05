# Python - 문자열 다루기

<br/>

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree - Novice Low</a>

<br/>

## 문자열 입출력 기본 방법

* <code>input()</code>함수를 통해 입력 받고, <code>print()</code>함수를 통해 출력한다.

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

* 문자열은 마치 1차원 배열과 같아, 문자열의 n번째 문자를 참조하기 위해선 n-1번지를 참조하면 된다.

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

* 문자열 출력 시 번지를 <strong>음수</strong>로 주면, 문자열의 뒤에서부터 출력할 수 있다.

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

* <code>len()</code>함수를 이용하면 된다.

* 이 때, 공백도 길이에 포함된다.

```python
sentence = input()

print(len(sentence))
```
```
hello world

11
```

<br/>

## 문자열 리스트

* 여러 문자열을 각각의 원소로 갖는 리스트를 정의하면 문자열을 목록으로 관리할 수 있다.

* 문자열의 리스트는 2차원 배열처럼 동작한다.

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

### 문자열 리스트 입력 받기

* 방법1. for문을 이용하여 문자열을 하나씩 리스트에 append 하기

```python
n = 5
arr = []

for _ in range(n):
    given_str = input()
    arr.append(given_str)
```

<br/>

* 방법2. <code>list comprehension</code>을 통해 구현

```python
n = 5
arr = [
    input()
    for _ in range(n)
]
```

<br/>

## 공백 단위로 문자열 입력받기

* <code>split()</code>함수룰 이용하면 입력받은 문자열이 공백 단위로 쪼개져 리스트로 만들어진다.

```python
arr = input().split()

print(arr)
```
```
>> hello world python

['hello', 'world', 'python']
```

<br/>

* 물론, list 힘수와 map 함수를 더 사용해도 된다.

```python
arr = list(map(str, input().split()))
```

<br/>

* tuple을 사용하면, 리스트 팔요 없이 두 변수에 문자열을 공백 단위로 잘라 받을 수 있다.

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

* for문을 통해 문자열의 길이를 구하지 않고 바로 원소에 접근할 수 있다.

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

* 문자열끼리 <code>+</code>연산을 통해 붙여줄 수 있다.

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

* <code>join()</code>함수는 지정한 구분값(<code>sep</code>)을 각 원소 사이에 삽입하여 하나의 문자열로 합쳐준다.

* <code>join()</code>함수를 이용하면 여러 문자열을 더 쉽게 연결할 수 있다.

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

* <code>in</code> 키워드를 통해 어떤 문자열에 특정 문자열이 포함되어 있는지 쉽게 알 수 있다.

```python
s = 'helloworld'

print('owo' in s)
```
```
True
```

<br/>

* 물론 이 키워드를 사용하지 않고 반복문과 조건문으로도 구현할 수 있다.

* slicing을 이용하면 좋다.

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

### 포함된 특정 문자열의 위치 구하기

<br/>

## 문자열 내 문자 다루기

### 문자열 내 문자 수정하기

### 문자열 내 문자 제거하기

* slicing을 통해 지워져야 할 문자의 양쪽 문자열만 따로 살려서 이어 붙인다.

```python
s = 'three'

s = s[:1] + s[2:]
print(s)
```
```
tree
```

<br/>

* 다른 방법으로, 문자열을 리스트로 변환한 후 <code>pop</code> 함수를 이용해 해당 문자를 제거한 후 다시 문자열로 변환한다.

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

### 문자열 밀기

<br/>

## 아스키 코드

### 아스키 코드로 문자 바꾸기

* 대소문자 변환

* 그 다음 알파벳 구하기

<br/>

## 문자열 형변환

<br/>

## 문자열 비교