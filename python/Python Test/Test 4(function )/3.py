
for i in range(1,5+1):
    for j in range(1,5+1):
        if(i==1 or i==5 or i==6-j ):
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()