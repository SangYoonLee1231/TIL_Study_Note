# Python - 2차원 리스트(배열)

<br/>

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree - Novice Low</a>

<br/>

## 목차

* <a href=""></a>
* <a href=""></a>
* <a href=""></a>
* <a href=""></a>
* <a href=""></a>
* <a href=""></a>

<br/>

## 2차원 리스트 선언과 활용

### 2차원 리스트 개념

* 리스트를 원소로 갖는 리스트를 2차원 리스트(혹은 2중 리스트)라 한다.

    ```python
    arr_2d = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    ```

<br/>

### 2차원 리스트 입력

* n개의 줄에 걸쳐 n개의 숫자를 입력받을 때, 이 2차원 격자 모양의 입력값들을 그대로 담아야 할 필요가 있다.

* 이 때 2차원 리스트를 활용하면 좋다.

* 각 줄마다 입력을 받아 하나의 리스트로 만들고, 이를 2차원 리스트에 <code>append()</code> 함수를 이용하여 추가한다.

    ```python
    n = int(input())
    arr_2d = []

    for _ in range(n):
        arr_1d = list(map(int, input().split()))
        arr_2d.append(arr_1d)

    print(arr_2d)
    ```

<br/>

* 이 때 <code>list comprehension</code>을 이용하면 더 간단히 입력값을 처리할 수 있다.

* 단, for loop 안에 append만 사용하는 경우여야만 가능하다.

    ```python
    n = int(input())
    arr_2d = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    print(arr_2d)
    ```

<br/>

### 2차원 리스트 선언

* 위에서 설명한 <code>list comprehension</code>을 통해 전부 0으로 초기화 된 2차원 배열을 선언해보자.

```
```

<br/>