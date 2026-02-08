from collections import Counter
n= int(input())

for i in range(n):
    s=input().strip()
    t=input().strip()
    p=input().strip()
    
    is_sub =0
    for k in t:
        if is_sub < len(s) and k ==s[is_sub]:
            is_sub +=1
            
    if is_sub != len(s):
        print("NO")
        continue
    
    s_count= Counter(s)
    t_count =Counter(t)
    p_count = Counter(p)
    
    flag =True
    
    for j in t_count:
        if t_count[j] > s_count[j] + p_count[j]:
            
            flag= False
            break
    if flag:
        print("YES")
    else:
        print("NO")
        
        