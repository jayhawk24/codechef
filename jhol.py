def main():
    for _ in range(int(input())):
        jadu = str(input())
        jhol = str(input())
        if jhol in jadu:
            print("YES")
        else:
            print("NO")
if __name__=='__main__':
    main()