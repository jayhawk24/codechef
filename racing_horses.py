for _ in range(int(input())):
    n = int(input())
    sor=[]
    dif=[]
    s= list(map(int,input().split()))
    sor=sorted(s)
    for i in range(n-1):
        dif.append(sor[i+1]-sor[i])

    print(min(dif))