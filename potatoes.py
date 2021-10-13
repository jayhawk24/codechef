from math import sqrt, ceil

def isPrime(n):
    for i in range(2, ceil(n)):
        if n%i == 0:
            return False
    return True

def gtPrime(total):
    total += 1
    while isPrime(total) == False:
        total += 1
    return total
        
for _ in range(int(input())):
    x, y = map(int, input().split())
    optimal = gtPrime(x+y)
    print(optimal-(x+y))
