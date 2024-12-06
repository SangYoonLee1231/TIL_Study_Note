n = int(input())

inputs = [
    list(input().split())
    for _ in range(n)
]

trail = [0 for _ in range(2001)]

dl, dr = [1, -1]
mapper = {
    "R": 1,
    "L": -1
}


def move():
    global trail

    curr = 1000

    for i in range(n):
        x = int(inputs[i][0])
        dir_x = inputs[i][1]

        if i == 0:
            curr += mapper[dir_x]
        for _ in range(x):
            trail[curr] += 1
            curr += mapper[dir_x]
    

def check_answer():
    global trail
    
    count = 0

    for elem in trail:
        if elem >= 2:
            count += 1
    
    return count


move()
print(check_answer())
