for i in range(1,6):
    c=65
    for j in range(1,7-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(chr(c),end=" ")
        c+=1
    
    for j in range(1,i):
        print(chr(c),end=" ")
        c+=1
    
    print()