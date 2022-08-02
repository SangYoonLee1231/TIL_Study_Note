n, m = tuple(map(int, input().split()))
x, y = 0, 0

grid = [
    [0] * m
    for i in range(n)
]

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

dir_num = 0

def is_range(x, y):
    return x >= 0 and x < m and y >= 0 and y < n

for i in range(1, n*m+1):
    grid[x][y] = i
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not is_range(nx, ny) or grid[nx][ny]:
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    x, y = nx, ny
    

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()