arr = []    # 또는 arr = list()

arr.append(1)    # arr = [1]
arr.append(3)    # arr = [1, 3]
arr.append(5)    # arr = [1. 3, 5]

print(len(arr))  # 3
print(sum(arr))  # 9

a = arr.pop()
print(f"a = {a}, arr = {arr}")     # a = 5, arr = [1, 3]

print(len(arr))     # 2
print(sum(arr[1:]))     # 3