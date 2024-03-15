n = int(input())

grid = [
    [0] * n
    for _ in range(n)
]

flag = True
num = 1

for i in range(n - 1, -1, -1):
    if flag:
        for j in range(n - 1, -1, -1):
            grid[j][i] = num
    else:
        for j in range(n):
            grid[j][i] = num

    num += 1
    flag = not flag

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()
