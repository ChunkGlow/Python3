def palindr(r):  
    e = len(r) - 1  
    s = 0  
    while s < e:  
        if r[s] != r[e]:  
            return False  
        s += 1  
        e -= 1  
    return True  
    
r = input("Enter the number of elements in the tuple: ")

if(palindr(r)):  # Corrected the function name from 'palind' to 'palindr'  
    print("The Tuple is Flip-Flop")  
else:  
    print("The Tuple is not Flip-Flop")