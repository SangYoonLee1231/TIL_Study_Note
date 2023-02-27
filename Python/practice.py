n, m = tuple(map(int, input().split()))
lst = []
used = [False for i in range(n + 1)]

print(used)


def print_lst():
    for elem in lst:
        print(elem, end=" ")
    print()


def choose(curr_num):
    # 종료 조건
    if curr_num == m + 1:
        print_lst()
    return

    # 재귀 호출
    for i in range(1, n + 1):
        if used[i] == True:
            continue

        lst.append(i)
        used[i] = True

        choose(curr_num + 1)

        used[i] = False
        lst.pop()


choose(1)