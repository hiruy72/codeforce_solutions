n = int(input())
arr = list(map(int, input().split()))


result = []
for i in arr:
    count = 1
    for j in arr:
        if j > i:
            count +=1
    result.append(count)

print(*result)
    






