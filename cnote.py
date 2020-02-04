try:
    for t in range(int(input())):
        xykn = *(int(n) for n in input().split()),
        pages_req = xykn[0]
        pages_cur = xykn[1]
        money = xykn[2]
        notebooks = xykn[3]
        pici = []
        itr = 0
        for foo in range(0, notebooks):
            pici.append([int(n) for n in input().split()])

        if pages_req < pages_cur:
            print("LuckyChef")
        else:
            for cost in pici:
                if money >= cost[1] and (pages_req - pages_cur) <= cost[0]:
                    print("LuckyChef")
                    break
                itr += 1
            if itr == notebooks:
                print("UnluckyChef")
except:
    pass