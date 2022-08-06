n, t = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

lst = []
N = n * 3

for elems in grid:
    for elem in elems:
        lst.append(elem)


for _ in range(t):
    temp = lst[N-1]

    for i in range(N-1, 0, -1):
        lst[i] = lst[i-1]

    lst[0] = temp


for i in range(N):
    print(lst[i], end=" ")
    
    if i % n == (n-1):
        print()