for _ in range(int(input())):
    arr=list(map(int,input().split()))
    age=[0,0,0]
    money=[0,0,0]
    for i in range(3):
        age[i]=arr[i]
        money[i]=arr[i+3]
    if max(age)