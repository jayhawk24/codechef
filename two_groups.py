for _ in range(int(input())):
    nums=list(map(int,input().split()))
    total = nums[0] + nums[1]*2 + nums[2]*3
    if total % 2 == 0:
        if nums[0] == 0 or nums[1]==0 or nums[2]==0:
            if nums[0]%2==0 and nums[1]%2==0 and nums[2]%2==0:
                print("YES")
            else:print("NO")
        else:
            print("YES")
    else:
        print("NO")