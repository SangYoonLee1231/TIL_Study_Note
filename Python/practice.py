def func(a, b):
    global n1, n2

    point = 0
    cnt = 0
    for elem in a:
        for i in range(point, n2):
            if elem == b[i]:
                cnt += 1
                point = i + 1
                break
    if cnt == n2:
        return True
    return False


n1, n2 = tuple(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if func(a, b):
    print("Yes")
else:
    print("No")