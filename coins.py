def main():
    for _ in range(int(input())):
        n=int(input())
        total = n//2 + n//3 + n//4
        if total>n:
            print(total)
        else:
            print(n)
if __name__=='__main__':
    main()