# Python - 

<br/>

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree - Novice Low</a>

<br/>

### 목차

<br/>

## 사칙연산

* 수학처럼 프로그래밍에서도 사칙연산이 자주 쓰인다.

    * <code>+</code> :

    * <code>-</code> :

    * <code>*</code> :

    * <code>*</code> :

    * <code>//</code> :

    * <code>%</code> :

    * <code>**</code> :

### 사칙연산 간략하게 표현하기

<code>a = a + 5</code>

* 위와 같이 동일한 값에 변화를 주는 사칙연산은 아래처럼 간략하게 표현할 수 있다.

<code>a += 5</code>

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