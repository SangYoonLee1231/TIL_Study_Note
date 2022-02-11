n, r, c = list(map(int, input().split()))

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [-1, 1, 0, 0]
dys = [0, 0 ,-1, 1]

continue_move = True

def in_range(x, y):
    return x >= 0 and x <= n-1 and y >= 0 and y <= n-1

def move(x, y):
    global continue_move

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if arr[x][y] < arr[nx][ny] and in_range(nx, ny):
            print(arr[x][y], end=" ")
            return nx, ny
    print(arr[x][y], end=" ")
    continue_move = False
    return x, y


x, y = r-1, c-1
while continue_move:
    x, y = move(x, y)