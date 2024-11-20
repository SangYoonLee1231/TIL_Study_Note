case = int(input())


def check_all_same(lst):
    flag = lst[0]
    for elem in lst:
        if (elem != flag):
            return False
    return True


def test_case():
    n, k = tuple(map(int, input().split()))
    lst = list(map(int, input().split()))

    for count in range(1, n + 1):
        if check_all_same(lst):
            return count - 1
        # 작업 신행
        lst.append(lst[k - 1])
        lst.pop(0)

    return -1


for i in range(1, case + 1):
    print(f"#{i} {test_case()}")
