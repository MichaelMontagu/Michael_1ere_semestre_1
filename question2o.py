def fuse(x):
    if x == 1:
        time = input("Enter time for fuse 1: ")
        if time != 0:
            return 3
        else:
            return 0
    if x == 2:
        time1 = input("Enter time for fuse 1: ")
        time2 = input("Enter time for fuse 2: ") 
        if time1 == time2:
            return 7
        else:
            return 9
    if x == 3:
        time1 = input("Enter time for fuse 1: ")
        time2 = input("Enter time for fuse 2: ")
        time3 = input("Enter time for fuse 3: ")    
        if time1 != time2 != time3:
            return 22
        if time1 == time2 == time3:
            return 13
        else:
            return 19
    if x == 4:
        time1 = input("Enter time for fuse 1: ")
        time2 = input("Enter time for fuse 2: ")
        time3 = input("Enter time for fuse 3: ")
        time4 = input("Enter time for fuse 4: ")
        return 41

print(fuse(1))
