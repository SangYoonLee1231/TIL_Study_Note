import sys

n = int(input())

x_lst = []; y_lst = []
min_area = sys.maxsize

for _ in range(n):
    x, y = list(map(int, input().split()))
    x_lst.append(x)
    y_lst.append(y)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        x_new_lst = []; y_new_lst = []
        x_new_lst.append(x_lst[j])
        y_new_lst.append(y_lst[j])

    x_new_lst.sort()
    y_new_lst.sort()

    x_min = x_new_lst[0]
    y_min = y_new_lst[0]
    x_max = x_new_lst[n-2]
    y_max = y_new_lst[n-2]

    area = (x_max - x_min) * (y_max - y_min)

    if min_area > area:
        min_area = area

print(min_area)
