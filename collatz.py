terms = 70
start_number = 1
end_number = 1000
def collatz(x):
    for i in range(terms):  # how many terms for each number
        if x == 1:  
            return True
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
    return False  

for x in range(start_number, end_number):  # how many numbers are we checking
    check = collatz(x)
    
    if not check:  
        print("The number", x, "didn't reach 1 within", terms , "terms")
          
else:
    print("All numbers reached 1 within the first", terms ,"terms.")

