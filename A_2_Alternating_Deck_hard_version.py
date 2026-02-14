t = int(input())
for _ in range(t):
    n = int(input())
    
    alice_white = 0
    alice_black = 0
    bob_white = 0
    bob_black = 0
    
    step = 1
    position = 1
    remaining = n
    
    while remaining > 0:
        take = min(step, remaining)

        if position % 2 == 1:
            whites = (take + 1) // 2
        else:
            whites = take // 2
        
        blacks = take - whites
        
        if step % 4 == 1 or step % 4 == 0:
            alice_white += whites
            alice_black += blacks
        else:
            bob_white += whites
            bob_black += blacks
        
        position += take
        remaining -= take
        step += 1
    
    print(alice_white, alice_black, bob_white, bob_black)
