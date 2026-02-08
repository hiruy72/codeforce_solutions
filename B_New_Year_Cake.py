def solve_case(a,b):
    
    layer =1
    count = 0
    
    while True:
        if a >= layer:
            a -= layer
            layer *=2
            count +=1
        else:
            break
        if b >= layer:
            b -= layer
            layer *=2
            count +=1
        else:
            break   
    return count 

n = int(input())   

for i in range(n):
    a, b = map(int, input().split())
    
    result1= solve_case(a, b)
    result2= solve_case(b, a)
    
    print(max(result1,result2))
    

    
