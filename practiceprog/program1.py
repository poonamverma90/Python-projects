apple=int(input("Enter how many apples harry has\n"))

mn=int(input("type minimum value to check\n"))
mx=int(input("type max value to check\n"))

for i in range(mx, mn+1):
    if apple%i == 0:
        print(f"{i} is a divisor of {apple}")

    else:
        print(f"{i} is not a divisor of {apple}")
        
        
        
        
        
        
        
        
        
        
        
        
        