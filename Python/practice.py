n = int(input())

isPrime = True
i = 2

while i*i < n:
    if n % i == 0:
        isPrime = False
        break
    else:
        i += 1

if isPrime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")