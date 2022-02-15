## enumerate 함수

```python
arr = [10, 20, 30, 40, 50]

for i, elem in enumerate(arr):
    print(i, elem)
```

```python
arr = [10, 20, 30, 40, 50]

for i, elem in enumerate(arr, start=1):
    print(i, elem)
```

```python
students = []

students.sort(key=lambda x: -x[0])

for idx, (_, _, _, number) in enumerate(students, start=1):
    print(f"{idx}등: {number}번")

a, b = 3, (5, 6, 7, 4, 6)

a, (b1, b2, b3, b4, b5) = 3, (5, 6, 7, 4, 6)

b1, b2, b3, b4, b5 = b
print(b5)
```