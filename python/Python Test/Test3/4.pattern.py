x=0
for i in range(1,6):
    for j in range(1,6):
        if(x%2==0):
            print("1",end=" ")
            x+=1
        else:
            print("0",end=" ")
            x+=1
    print()