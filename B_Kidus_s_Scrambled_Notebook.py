t= int(input())  
    
for i in range(t):
    rating = str(input())
    n= len((rating))
    flag= False
    
    
    
    for j in range(1,n):
        
        if rating[0]== '0' or rating[j]== '0':
            continue
        a= int(rating[:j])
        b= int(rating[j:])
        
        if b > a:
            print(a, b)
            flag = True
            break
        
        
        
    if not flag:
        print(-1)
            
    
    
    
    