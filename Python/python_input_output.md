# Python : 입력 함수 <code>input()</code> 사용법

<br/>

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree - Novice Low</a>

<br/>

### 목차

* <a href="">기본 입력 방법</a>
* <a href="">문자열을 나눠서 입력 받기</a>

<br/>

## 기본 입력 방법

* python에선 <code>input()</code>함수를 통해 한 줄 단위로 문자열을 입력 받을 수 있다.


```python
a = input()

print(f"a = {a}")
```

▼ 입력 및 출력 결과

```
>> Hello World

a = Hello World
```
```
>> 4

a = 4    (이때 4는 문자열 "4"이다.)
```

<br/>

### 문자열이 아닌 다른 자료형으로 입력 받기

* 이 때, 입력값의 자료형이 정수나 실수여도 문자열로 인식된다.


```python
b = input()

print(b + 1)
```

▼ 입력 및 출력 결과

```
>> 4

----> 4 print(b + 1)

TypeError: can only concatenate str (not "int") to str
```

* 문자열에 숫자를 더할 순 없으므로 에러가 발생하는 것이다.

* 숫자로만 이루어진 문자열을 다른 자료형으로 바꾸기 위해선, 아래와 같이 형변환을 해주어야 한다.

```python
b = int(input())

print(b + 1)
```

```
>> 4

5
```

* 또는 아래와 같이 값을 우선 입력 받고 형변환을 해줘도 된다.

```python
b = input()
b = int(b)

print(b + 1)
```

```
>> 4

5
```

<br/>

* 실수형이라면 <code>float()</code>로 감싸주면 된다.

```python
c = float(input())

print(c + 0.32)
```

```
>> 2.23

2.55
```

<br/>

## 문자열을 나눠서 입력 받기