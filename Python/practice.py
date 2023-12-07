def solution(arr):
    exist = []
    for i in range(len(arr)):
        for elem in exist:
            if arr[i] == elem:
                print(str(i) + "break")
                break
        print(str(i) + "append")
        exist.append(arr[i])

    return exist


print(solution([1, 1, 3, 3, 0, 1, 1]))
