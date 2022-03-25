# Python - 사칙연산을 위한 연산자

<br/>

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree - Novice Low</a>

<br/>

### 목차

* <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_operator.md#%EC%82%AC%EC%B9%99%EC%97%B0%EC%82%B0">사칙연산</a>
* <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_operator.md#%EC%97%B0%EC%82%B0%EC%9E%90-%EC%9A%B0%EC%84%A0-%EC%88%9C%EC%9C%84">연산자 우선 순위</a>

<br/>

## 사칙연산

* 수학처럼 프로그래밍에서도 사칙연산이 자주 쓰인다.

    * <code>+</code> : 더하기 연산

    * <code>-</code> : 빼기 연산

    * <code>*</code> : 곱하기 연산

    * <code>/</code> : 나누기 연산
    
        * <code>/</code> 연산의 계산 결과는 항상 실수값이다.

        ```python
        a = 3 / 1
        print(a)
        ```

        ▼ 출력 결과

        ```
        3.0
        ```

    * <code>//</code> : 나누기 - 몫 연산

    * <code>%</code> : 나누기 - 나머지 연산

    * <code>**</code> : 제곱 연산

        ```python
        a, b = 3 , 2
        print(a**b)    # a^b
        ```

        ▼ 출력 결과

        ```
        9
        ```

<br/>

* 정수와 실수가 만나면 결과값은 실수가 된다.

* 사칙연산 계산 시 type은 더 큰 범위를 따라가기 때문이다.

```python
a = 1 + 1.0
print(a)
```

▼ 출력 결과

```
2.0
```


<br/>

### 사칙연산 간략하게 표현하기

<code>a = a + 5</code>

* 위와 같이 동일한 값에 변화를 주는 사칙연산은 아래처럼 간략하게 표현할 수 있다.

<code>a += 5</code>

<br/>

```python
a, b = 10, 4

a += 5    # a = a + 5
print(a)

a -= 5    # a = a - 5
print(a)

a %= b    # a = a % b
print(a)

a *= b    # a = a * b
print(a)
```

▼ 출력 결과

```
15
10
2
8
```

<br/>

## 연산자 우선 순위

* python을 비롯한 프로그래밍 언어에선 연산자의 우선 순위가 존재한다.

* 연산자의 우선 순위에 따라 연산자의 계산 순서가 결정된다.

* 하지만 이 순위를 외울 필요는 없다.

* 내가 의도하고자 하는 연산에 소괄호<code>()</code>를 적절히 잘 쓰면 된다.

    * 안쪽 소괄호부터 우선적으로 연산하므로

