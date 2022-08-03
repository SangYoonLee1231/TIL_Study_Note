def is_on_origin():
    global x, y, total_time

    dir_num = 3
    for cmd in cmds:
        if cmd == 'L':
            dir_num = (dir_num - 1 + 4) % 4
        elif cmd == 'R':
            dir_num = (dir_num + 1) % 4
        else:
            nx = x + dxs[dir_num]
            ny = y + dys[dir_num]
            x, y = nx, ny

        total_time += 1

        if x == 0 and y == 0:
            return True
    
    return False


cmds = list(input().split())
x, y = 0, 0
total_time = 0

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

if is_on_origin():
    print(total_time)
else:
    print(-1)