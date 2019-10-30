def main():
    for _ in range(int(input())):
        foo = [int(n) for n in input().split()]
        row,col,q=foo[0],foo[1],foo[2]
        query=[]
        ____=0
        arr = [[0]*col]*row
        for i in range(q):
            subq=[int(m) for m in input().split()]
            query.append(subq)

        for que in query:
            x,y=que[0],que[1]
            for n in range(x-1,row):
                arr[n][y-1]+=1
            for m in range(y-1,col):
                arr[x-1][m]+=1

        print(arr)

        for __ in arr:
            for ___ in __:
                if ___%2==1:
                    ____+=1
        print(____)

if __name__=='__main__':
    main()