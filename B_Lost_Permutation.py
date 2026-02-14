t = int(input())

for _ in range(t):
    m, s = map(int, input().split())
    b = list(map(int, input().split()))
    
    if len(set(b)) !=m:
        print("NO")
        continue
    sum_b = sum(b)
    max_b=max(b)
    
    total = sum_b +s

    k=0
    
    while(k*(k +1))//2 < total:
        k +=1
    if (k* (k +1))//2 == total and  k >=max_b:
        print("YES")
    else:
        print("NO")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    # used = set(b)
    # current = 1
    
    # while s > 0:
    #     if current not in used:
    #         s -= current
    #     current += 1
    
    # if s == 0:
    #     print("YES")
    # else:
    #     print("NO")


