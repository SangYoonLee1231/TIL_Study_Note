## enumerate 함수

* <code>enumerate</code> 함수는 for문을 돌 때, 각 원소와 동시에 index를 뽑아주는 역할을 하는 함수이다.

    ```python
    arr = [10, 20, 30, 40, 50]

    for i, elem in enumerate(arr):
        print(i, elem)
    ```
    ```
    0 10
    1 20
    2 30
    3 40
    4 50
    ```

<br/>

* <code>enumerate</code> 함수에 start값을 인자로 넘기면 시작 index값을 설정할 수 있다.

```python
arr = [10, 20, 30, 40, 50]

for i, elem in enumerate(arr, start=1):
    print(i, elem)
```
```
1 10
2 20
3 30
4 40
5 50
```