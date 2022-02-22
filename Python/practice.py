_list = [1, 2, 3, 4]

def modify():
    global _list
    _list = [5, 6, 7, 8]


modify()
for elem in _list:
    print(elem, end=" ")