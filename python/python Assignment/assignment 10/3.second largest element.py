# 3. Write a program to find the second largest element in the list.
l=[6,5,4,3]
l2=l[0]
sl=0

for i in range(1,len(l)):
    if(l2 < l[i]):
        sl=l2
        l2=l[i]
    elif(sl < l[i] ):
        sl=l[i]
print(sl)