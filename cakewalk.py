def main():
    for _ in range(int(input())):
        n = int(input())
        ans=1
        exec=False
        while exec==False:
            while ans < n and exec==False :
                ans *=10
                if ans == n:
                    print("Yes")
                    exec=True
            while ans < n and exec==False :
                ans *=20
                if ans == n:
                    print("Yes")
                    exec=True
            while ans < n and exec==False :
                ans = ans * 20 *10
                if ans == n:
                    print("Yes")
                    exec=True
        if exec==False:
            print("No")

if __name__=='__main__':
    main()