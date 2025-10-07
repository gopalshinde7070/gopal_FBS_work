# 7. Write a program to create a new list from existing list which contains cube of each 
# number of list.

l1=[1,2,3,4,5]
l2=[]

for i in range(len(l1)):
    l2+=[l1[i]**3]
print(l2)