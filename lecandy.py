if __name__ == "__main__":
    for t in range(int(input())):
        nc = [int(m) for m in input().split()]
        na = [int(n) for n in input().split()]
        i = 0
        while i < len(na):
            nc[1] -= na[i]
            if nc[1] < 0:
                break
            i += 1
        if i == len(na):
            print("Yes")
        else:
            print("No")
