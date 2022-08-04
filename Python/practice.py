n = int(input())
blocks = []

num = [
    int(input())
    for _ in range(n)
]   

del_st = list(map(int, input().split()))
del_nd = list(map(int, input().split()))


# 1st
temp = [0] * n

temp_idx = 0
for i in range(n):
    if (i+1) < del_st[0] or (i+1) > del_st[1]:
        temp[temp_idx] = blocks[i]
        temp_idx += 1

blocks = temp
n = temp_idx


# 2nd
temp = [0] * n

temp_idx = 0
for i in range(n):
    if (i+1) < del_nd[0] or (i+1) > del_nd[1]:
        temp[temp_idx] = blocks[i]
        temp_idx += 1

blocks = temp
n = temp_idx


# 출력
print(n)
for i in range(n):
    print(blocks[i])