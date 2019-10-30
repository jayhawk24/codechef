for _ in range(int(input())):
    n=int(input())
    song=list(map(int,input().split()))
    uji=int(input())
    uj=song[uji-1]
    s=sorted(song)
    for i in range(n):
        if s[i] == uj:
            print(i+1)
            i=n
