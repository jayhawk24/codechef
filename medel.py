def main():
    for _ in range(int(input())):
        n=int(input())
        arr = [int(n) for n in input().split()]
        orderd=[]
        for i in range(3):
            orderd.append(arr[i])
        sorted(orderd)
        arr.remove(orderd[1])
        print(f"{orderd[2]} {len(arr)}")

if __name__=='__main__':
    main()