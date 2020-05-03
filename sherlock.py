def main():
    nm = [int(n) for n in input().split()]
    n = nm[0]
    m = nm[1]
    palace = []
    for __ in range(n):
        bar = [int(foo) for foo in input().split()]
        palace.append(bar)
    queries = []
    for _ in range(int(input())):
        queries.append(int(input()))
    for num in queries:
        if num in palace:
            