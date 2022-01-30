# Python - 조건문

<br/>

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree - Novice Low</a>

<br/>

## 조건문 개념

* 특정 조건을 만족할 경우에만 코드를 수행하고 싶을 때 쓰는, 매우 중요한 문법이다.

<br/>

## if 조건문

* 조건식을 만족할 경우, <code>if</code>문의 내부 코드를 실행한다.

```
if 조건식:
    조건식이 참일 경우 수행되는 코드 영역
```

<br/>

* python에서 <code>if</code>문의 가장 중요한 점은 들여쓰기다.  

    indent를 정확히 맞춰주어야 한다.

```python
a = int(input())
b = int(input())

if a >= 1 and b >= 1:
    a += 3
    b += 5

print(f"a = {a}, b = {b}")
```

▼ 입력 및 출력 결과

```
>> 1
>> 2

a = 4, b = 6
```

<br/>

* <code>==</code>기호는 값과 데이터 type이 모두 동일하야 True이다.

    * <code>1 == '1'</code>은 False이다.

* 정수 a가 짝수인지 홀수인지 판별하려면, <code>%</code>를 연산을 통해 a를 2로 나눈 나머지 값이 0인지 아닌지 판별하면 된다.

    ```python
    a = int(input())

    if a % 2 == 0:
        print("even number")
    ```
<br/>

## if else 조건문

* 조건식을 만족하지 않을 경우, <code>else</code>문의 내부 코드를 실행한다.

* if문과 함께 사용한다.

```
if 조건식:
    조건식이 참일 경우 수행되는 코드 영역
else:
    조건식이 거짓일 경우 수행되는 코드 영역
```

<br/>

```python
a = int(input())
b = int(input())

if a >= 1 and b >= 1:
    a += 3
else:
    b += 5

print(f"a = {a}, b = {b}")
```

▼ 입력 및 출력 결과

```
>> 1
>> 2

a = 4, b = 1
```
```
>> 1
>> 0

a = 1, b = 5
```