k, n, l = map(int, input().split())

sum=0
for i in range(1,l+1):
    sum += k * i

print(sum - n)
    