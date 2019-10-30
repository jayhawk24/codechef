def main():
    for _ in range(int(input())):
        g=int(input())
        foo=list(map(int,input().split()))
        init = foo[2]*foo[1]
        for n in range(foo[1]) :
            for j in range(n) :
                if (init[j]==1) :
                    init[j]=2
                else:
                    init[j]=1
        print(init.count(foo[2]))

if __name__=='__main__':
    main()