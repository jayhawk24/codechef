for _ in range(int(input())):
    nums=list(map(int,input().split()))
    res = nums[0]+nums[1]
    ans=str(res)
    total=0
    for char in ans:
        if char == '0' or char == '6' or char == '9':
            total+=6
        elif char == '1':
            total+=2
        elif char == '2' or char == '3' or char == '5':
            total+=5
        elif char == '4':
            total+=4
        elif char == '8':
            total+=7
        elif char == '7':
            total+=3
    print(total)