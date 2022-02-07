arr = [1, 2, 3, 4, 5]

print(arr[1:3])     # [2, 3]
print(arr[1:3:1])   # [2, 3]
print(arr[2:])      # [3, 4, 5]
print(arr[:3])      # [1, 2, 3]
print(arr[3:0:-1])  # [4, 3, 2]
print(arr[::-1])    # [5, 4, 3, 2, 1]
print(arr[::2])     # [1, 3, 5]