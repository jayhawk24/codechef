for _ in range(int(input())):
    n = int(input())
    people = [int(foo) for foo in input().split()]
    infected = []
    i, j, k = 0, 0, 0
    streak = 0
    while i < n - 1:
        spread = 1
        if abs(people[i] - people[i + 1]) < 3:
            for j in range(i, n - 1):
                if abs(people[j] - people[j + 1]) < 3:
                    spread += 1
                else:
                    infected.append(spread)
                    i = j
                    break
                if j == n-2:
                    streak = 1
            infected.append(spread)
            i = j
        if abs(people[i] - people[i - 1]) < 3:
            spread = 1
            for k in range(i, 0, -1):
                if abs(people[k] - people[k - 1]) < 3:
                    spread += 1
                else:
                    infected.append(spread)
                    break
            infected.append(spread)
        i += 1
    if len(infected) == 0:
        infected.append(1)
    print(min(infected), max(infected))
