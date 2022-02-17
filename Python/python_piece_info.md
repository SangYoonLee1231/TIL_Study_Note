## Python - 조각 지식 모음

<br/>

* 파이썬과 관련된 공부 내용 중 하나의 목차로 분류하기 애매한 지식을 따로 모아 정리하는 곳입니다.

<br/>

### 목차

* <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_piece_info.md#%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EB%B3%80%EC%88%98%EC%9D%98-scope-%EB%B2%94%EC%9C%84">파이썬에서 변수의 scope 범위</a>
* <a href="https://github.com/SangYoonLee1231/TIL/blob/main/Python/python_piece_info.md#2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%EC%84%A0%EC%96%B8-%EC%8B%9C-%EC%9C%A0%EC%9D%98-%EC%82%AC%ED%95%AD">2차원 배열 선언 시 유의 사항</a>

<br/>

## 파이썬에서 변수의 scope 범위

* 파이썬에서 <code>for</code>문이나 <code>if</code>문, 또는 함수의 내부에 선언한 지역 변수는 놀랍개도 main 함수 영역(indent가 없는 코드 영역)에서도 전역 변수처럼 그대로 사용된다.


```python
sum_val = 0
for idx in range(1, 6):
    sum_val += idx

print(idx)
```
```
5
```

<br/>

```python
n = 10
if n % 2 == 0:
    k = 5
else:
    k = 6

print(k)
```
```
5
```

* 다만 이러한 지역 변수는 다른 함수(<code>for</code>문, <code>if</code>문도 표함)의 내부 영역에선 참조할 수 없다.

```python
def g(n):
    return n + t  # 이 g 함수 내부에선, f 함수 내부의 t에 접근할 수 없다.

def f(n, p1):
    t = 15
    return n + p1 + g(10)

p = 9
print(f(6, 10))
```
```
NameError: name 't' is not defined
```

* 그러나 코드는 되도록 이렇게 안 짜는 것이 좋다.

<br/>

## range 함수의 이해 (C++ 반복문과 python 반복문의 차이점)

* <code>range(1, 6)</code> == <code>[1, 2, 3, 4, 5]</code> 이렇게 이해하면 편한다. (틀린 설명이나)

<br/>

```c++
#include <iostream>
using namespace std;

int main() {
    int sum_val = 0;
    int i;

    for (i = 0; i < 6; i++) {
        sum_val += i;
    }

    cout << i;

    return 0;
}
```
```
6
```

* C++에서 for문은 변수 i 자체가 값이 1씩 증가하다 조건을 벗어나는 순간, 즉 위 코드에선 i가 6이 된 직후, 종료한다.

<br/>

```python
sum_val = 0
for i in range(1, 6):
    sum_val += i

print(i)
```
```
5
```

* 반면 파이썬에서 for문은 변수 i 자리에 1부터 5까지 값이 하나씩 대입되고 끝난다. 즉 i값은 5인 상태가 된다.

<br/>

## 2차원 배열 선언 시 유의 사항

* 다음과 같이 2차원 배열을 선언하면 안 된다.

```python
[ [0] * n ] * n
```