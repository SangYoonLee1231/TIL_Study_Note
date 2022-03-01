n, t = tuple(map(int, input().split()))
x, y, dir_num = tuple(input().split())
x, y = int(x), int(y)

dxs = [0, -1, 1, 0]
dys = [1, 0, 0, -1]

mapper = {
    'U' : 1,
    'D' : 2,
    'R' : 0,
    'L' : 3
}

dir_num = mapper[dir_num]

def in_range(x, y):
    return x >= 1 and x <= n and y >= 1 and y <= n

for _ in range(t):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny):
        dir_num = 3 - dir_num
    else:
        x, y = nx, ny

print(x, y)