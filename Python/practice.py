n = int(input())
a = [
    list(map(int, input().split()))
    for _ in range(n)
]
x, y = 0, 0


def in_range(x, y):
    return x >= 0 and x < 4 and y >= 0 and y < 4

def ones_cnt(x, y):
    cnt = 0
    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        if in_range(nx, ny) and a[nx][ny] == 1:
            cnt += 1

    return cnt

ans = 0
for i in range(n):
    for j in range(n):
        if ones_cnt(i, j) >= 3:
            ans += 1

print(ans)