n = int(input())

lst = []
'''
for _ in range(n):
    command = input()
    
    if command[:9] == 'push_back':
        lst.append(int(command[10:]))
    elif command == 'pop_back':
        lst.pop()
    elif command == 'size':
        print(len(lst))
    elif command[:3] == 'get':
        k = int(command[4:])
        print(lst[k-1])
    else:
        pass
'''

for _ in range(n):
    command = input()

    if command.startswith == 'push_back':
        _, num = command.split()
        lst.append(int(num))
    elif command == 'pop_back':
        lst.pop()
    elif command == 'size':
        print(len(lst))
    elif command.startswith == 'get':
        _, k = command.split()
        print(lst[k-1])
    else:
        pass