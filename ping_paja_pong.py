for _ in range(int(input())):
    foo=[int(n) for n in input().split()]
    if ((foo[0]+foo[1])%foo[2])%2==0:
        print("Chef")
    else:print("Paja")