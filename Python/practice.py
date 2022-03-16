def add(*args, a=0):
    s = 0
    for x in args:
        s = s + x
    s += a

    return s

print(add(3,4,5,6))
print(add(3,4,5,6), 20)