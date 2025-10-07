# 6. Write a program to remove duplicates from the list.
l1=[1,1,2,2,3,3,4,4,5,5,6,7,8,9,10]
l2=[]
for i in range(len(l1)):
    if( l1[i] not in l2):
        l2+=[l1[i]]
print(l2)