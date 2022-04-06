n, m = tuple(map(int, input().split()))

lst = [
    list(map(int, input().split()))
    for _ in range(n)
]

for x in range(2):
    l, r = tuple(map(int, input().split()))

    for i in range(l-1, l+4):
        for j in range(m):
            if lst[i][j] == 1:
                lst[i][j] = 0
                break

ans = 0
for i in range(n):
    for j in range(m):
        ans += lst[i][j]

print(lst[i][j])