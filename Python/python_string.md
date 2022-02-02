# Python - 문자열 입출력

<br/>

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree - Novice Low</a>

<br/>

## 문자열 입력받아 출력하는 기본적인 방법

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