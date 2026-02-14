t = int(input())
for _ in range(t):
    n = int(input())
    a = b = 0
    turn = 0
    i = 1
    while n > 0:
        give = min(i, n)
        if turn == 0:
            a += give
        else:
            b += give
        n -= give
        i += 1
        if i % 2 == 0:
            turn ^= 1
    print(a, b)