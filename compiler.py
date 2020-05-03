if __name__ == "__main__":
    for t in range(int(input())):
        inp = list(str(input()))
        cnt = 0
        i = j = 0
        stack = []

        for i in range(len(inp)):
            if inp[i] == '<':
                stack.append('<')
            else:
                if len(stack) > 0:
                    stack.pop()
                    cnt += 2

        print(cnt)
