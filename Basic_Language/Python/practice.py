k, n = tuple(map(int, input().split()))

lst = []


def choose(curr_n):
    if curr_n == n + 1:
        for elem in lst:
            print(elem, end=" ")
        print()

    for i in range(1, k + 1):
        lst.append(i)
        choose(curr_n + 1)
        lst.pop()


choose(1)
