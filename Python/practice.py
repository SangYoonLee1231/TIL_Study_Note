def func(c):
    print(id(c))
    c = 2;  print(id(c))

a = 1;  print(id(a))
b = 2;  print(id(b))
func(a)