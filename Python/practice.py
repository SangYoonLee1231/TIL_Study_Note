# 변수 선언, 입력
n = int(input())
matrix = [
    list(input())
    for _ in range(n)
]
razer_point = int(input())
count = 1

#      D. L. U.  R.
drs = [1, 0, -1, 0]
dcs = [0, -1, 0, 1]

dir_num = (razer_point - 1) // n


# 처리 Step 1 - 레이저 시작 포인트 설정
if (dir_num == 0):
    start_point = [0, razer_point - 1]
elif (dir_num == 1):
    start_point = [(razer_point - 1) % n, n-1]
elif (dir_num == 2):
    start_point = [n-1, (n-1) - ((razer_point - 1) % n)]
elif (dir_num == 3):
    start_point = [(n-1) - ((razer_point - 1) % n), 0]
else:
    pass


# 처리 Step 2 - 레이저 꺾기 관련 함수 정의

# 범위
def in_range(r, c, n):
    return r >= 0 and r < n and c >= 0 and c < n

# '\' 처리 과정
def left_slice_process(r, c, dir_num):
    if (dir_num == 0 or dir_num == 2):
        # 왼쪽으로 꺾기
        return move_counter_clockwise(r, c, dir_num)
    elif (dir_num == 1 or dir_num == 3):
        # 오른쪽으로 꺾기
        return move_clockwise(r, c, dir_num)
    else: pass

# '/' 처리 과정
def right_slice_process(r, c, dir_num):
    if (dir_num == 0 or dir_num == 2):
        # 오른쪽으로 꺾기
        return move_clockwise(r, c, dir_num)
    elif (dir_num == 1 or dir_num == 3):
        # 왼쪽으로 꺾기
        return move_counter_clockwise(r, c, dir_num)
    else: pass


# 왼쪽으로 꺾기
def move_counter_clockwise(r, c, dir_num):
    dir_num = (dir_num - 1 + 4) % 4
    return r + drs[dir_num], c + dcs[dir_num]

# 오른쪽으로 꺾기
def move_clockwise(r, c, dir_num):
    dir_num = (dir_num + 1) % 4
    return r + drs[dir_num], c + dcs[dir_num]


# 처리 Step 3 - 레이저 이동
r, c = start_point

while True:
    if (matrix[r][c] == '\\'):
        nr, nc = left_slice_process(r, c, dir_num)
    elif (matrix[r][c] == '/'):
        nr, nc = right_slice_process(r, c, dir_num)
    else:
        pass

    if in_range(nr, nc, n):
        r, c = nr, nc
        count += 1
    else:
        break


# 결과 출력
print(count)