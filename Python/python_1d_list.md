# Python - 1차원 리스트(배열) 활용

<br/>

> 참고 자료 : <a href="https://www.codetree.ai/missions/4">Code Tree - Novice Low</a>

<br/>

## 목차

<br/>

## <code>input().split()</code> 활용법

* <code>input().split()</code>으로 공백을 사이에 두고 주어지는 입력값을 나눠 받을 수 있다.

```python
arr = input().split()

print(arr)
```
```
>> 1 3 5

['1', '3', '5']
```

<br/>

* 여기서 <code>map</code>을 활용하면, 입력받는 모든 값에 원하는 함수를 적용시킬 수 있다.

```python
arr = list(map(int, input().split()))

print(arr)
```
```
>> 1 3 5

[1, 3, 5]
```

<br/>

* 이 때, 입력받을 값의 개수가 고정되어 있으면, <code>list()</code>함수 대신 <code>tuple()</code>함수를 쓰는 것이 좋다. (unpacking 활용)

```python
n, m = tuple(map(int, input().split()))

print(n, m)
```
```
>> 1 3

1 3
```

<br/>

## 리스트 슬라이싱 (Slicing)

* 리스트에 대해 slice를 활용하면 일부 범위, 조건에 해당하는 원소들을 가져올 수 있다.

```
배열 이름[start값:end값:step]
```

```python
arr = [1, 2, 3, 4, 5]

print(arr[1:3])     # [2, 3]
print(arr[1:3:1])   # [2, 3]
print(arr[2:])      # [3, 4, 5]
print(arr[:3])      # [1, 2, 3]
print(arr[3:0:-1])  # [4, 3, 2]
print(arr[::-1])    # [5, 4, 3, 2, 1]
```

<br/>

## 자주 쓰이는 리스트 함수

* <code>append</code> 함수 : 리스트 맨 끝에 원소를 추가한다.

* <code>pop</code> 함수 : 리스트 맨 뒤에 있는 원소를 지우고 그 값을 반환한다.

* <code>len</code> 힘수 : 리스트의 원소 개수를 반환한다.

* <code>sum</code> 함수 : 리스트 안의 모든 원소의 합을 반환한다.

```python
# 비어있는 리스트 선언
arr = []    # 또는 arr = list()

arr.append(1)    # arr = [1]
arr.append(3)    # arr = [1, 3]
arr.append(5)    # arr = [1. 3, 5]

print(len(arr))  # 3
print(sum(arr))  # 9

a = arr.pop()
print(f"a = {a}, arr = {arr}")     # a = 5, arr = [1, 3]

print(len(arr))         # 2
print(sum(arr[1:]))     # 3
```
```
3
9
a = 5, arr = [1, 3]
2
3
```

<br/>

# 리스트 값 참조