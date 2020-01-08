def main():
    for _ in range(int(input())):
        for _ in range(int(input())):
            arr = [int(n) for n in input().split()]
            i = arr[0]
            n = arr[1]
            q = arr[2]
            foo=[i]*n
            for flip in range(n):
                for num in range(flip+1):
                    if foo[num]==1:
                        foo[num]=2
                    else:
                        foo[num]=1
            print(foo.count(q))
            
if __name__=='__main__':
    main()