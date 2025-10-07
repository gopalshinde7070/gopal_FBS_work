# 5. Accept a number from user and check if this element is present in the list or not. Also
#  tell how many times it is present in the list.

def checknumber(l1,x):
    c=0
    for i in range(len(l1)):
        if(x==l1[i]):
            c+=1
    if(c==0):
        print("Not present in list")
            
            
    elif(c>0):
        
        print(f"{x} present in list : {c} time",  )

l1=[10,20,30,10,20]
x=int(input("Enter the number : "))
checknumber(l1,x)