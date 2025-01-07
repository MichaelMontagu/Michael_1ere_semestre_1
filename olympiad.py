def is_palimdrome(x):
    strnum = str(x)
    rev = strnum[::-1]
    if strnum == rev:
        return True
    return False

def nextPalim(x):
    if is_palimdrome(x):
        return x
    while is_palimdrome(x) == False:
        x += -1    
    return x

def palimsum(x):
    if is_palimdrome(x):
        return x
    diff = x - nextPalim(x)
    if is_palimdrome(diff):
        return nextPalim(x), diff    
    pal = nextPalim(x) 
    for i in range(nextPalim(x)):
        pal -= 1
        if is_palimdrome(pal) and is_palimdrome(x-pal):
            return x - pal, pal
    return False
                
def pal3(x):
    if is_palimdrome(x):
        return x
    diff = x - nextPalim(x)
    if is_palimdrome(diff):
        return nextPalim(x), diff    
    pal = nextPalim(x) 
    for i in range(nextPalim(x)):
        pal -= 1
        if is_palimdrome(pal) and is_palimdrome(x-pal):
            return pal, x - pal
    for i in range(1, x):
        if is_palimdrome(i):
            diff = x - i 
            return i, palimsum(diff)[0], palimsum(diff)[1]

#run function pal3
print(pal3(472443))


