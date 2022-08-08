k, n = tuple(map(int, input().split()))
answer = []


def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()


def choose(curr_num, k_num):
    if n > curr_num:
        print_answer()
        return
    
    for i in range(1, k+1):
        answer.append(i)
        choose(curr_num + 1, i)
        answer.pop()


choose(1, 1)