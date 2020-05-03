from itertools import combinations_with_replacement
if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        string = str(input())
        cnt = string.count('1')
        print((cnt*(cnt+1))//2)