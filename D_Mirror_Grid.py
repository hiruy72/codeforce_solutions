t = int(input())
for _ in range(t):
    n = int(input())
    grid = [input() for _ in range(n)]
    flips = 0
    
    for i in range((n+1)//2):
        for j in range(n//2):
            # 4-way rotational group
            cells = [
                grid[i][j],
                grid[j][n-1-i],
                grid[n-1-i][n-1-j],
                grid[n-1-j][i]
            ]
            zeros = cells.count('0')
            ones = 4 - zeros
            flips += min(zeros, ones)
    
    print(flips)
