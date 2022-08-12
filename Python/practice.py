from collections import deque


n, k = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

start_list = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

visited = [
    [False] * n
    for _ in range(n)
]

q = deque()


def can_move(x, y):
    return not grid[x][y]

def in_range(x, y):
    return x >= 0 and y >= 0 and x < n and y < n

def bfs():
    while q:
        q.popleft()

        dxs = [0, 1, 0, -1]
        dys = [1, 0 , -1, 0]

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if in_range(nx, ny) and can_move(nx, ny) and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                


# 처리
for x, y in start_list:
    x, y = x-1, y-1
    q.append((x, y))
    visited[x][y] = True
    bfs()

# 출력
count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == True:
            count += 1

print(count)