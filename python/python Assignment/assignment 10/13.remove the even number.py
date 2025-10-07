# 13 . Write a program to print list after removing even numbers.
l=[1,2,3,4,5,6,7,8]
l1=[]
for i in range(len(l)):
    if(l[i]%2!=0):
        l1+=[l[i]]
print(l1)