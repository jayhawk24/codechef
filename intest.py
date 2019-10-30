def main():
    foo=[int(n) for n in input().split()]
    n=foo[0]
    k=foo[1]
    count = 0
    for _ in range(n):
        t = int(input())
        if t % k == 0:
            count+=1
    print(count)
if __name__=='__main__':
    main()