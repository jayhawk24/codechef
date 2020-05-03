if __name__ == "__main__":
    for t in range(int(input())):
        nk = *(int(n) for n in input().split()),
        n = *(int(m) for m in input().split()),
        lst = []
        for num in n:
            num += nk[1]
            if num % 7 == 0:
                lst.append(num)
        print(lst.count())
