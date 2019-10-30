def main():
    for _ in range(int(input())):
        nm = list(map(int, input().split()))
        completed = list(map(int, input().split()))
        jobchef=[]
        jobas=[]
        j=0
        for i in range(1,nm[0]+1):
            if i not in completed:
                if j%2==0:
                    jobchef.append(i)
                else:
                    jobas.append(i)
                j=j+1
        for num in jobchef:
            print(num,end=' ')
        print()
        for num2 in jobas:
            print(num2,end=' ')
        print()
if __name__ == '__main__':
    main()