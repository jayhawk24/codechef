for _ in range(int(input())):
    n=int(input())
    foo = [int(num) for num in input().split()]
    count=0
    mn=foo[n-1]
    for i in range(n):
        init=0
        if i<5:
            for j in range(i):
                if foo[i]<foo[j]:
                    init+=1
                    if init==i:
                        count+=1
        else:
            for j in range(i-5,i):
                if foo[i]<foo[j]:
                    init+=1
                    if init==5:
                        count+=1
    print(count)