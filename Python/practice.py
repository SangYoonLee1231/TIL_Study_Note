from collections import deque

n, m = tuple(map(int, input().split()))

snake = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * (m)
    for _ in range(n)
]

q = deque()


def can_move(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if not snake[x][y]:
        return False
    
    return True


def bfs():
    x, y = q.popleft()

    while q:
        dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if can_move(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

                if nx == (n-1) and ny == (m-1):
                    return


visited[0][0] = True
q.append((0, 0))
bfs()

print(1 if visited[n-1][m-1] else 0)

