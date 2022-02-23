def swap(lst):
    lst[0], lst[1] = lst[1], lst[0]
    print(lst[0], lst[1])

lst = [10, 20]
swap(lst)
print(lst[0], lst[1])