# 7. Python Program to Find the Intersection of Two Lists
l1=[1,2,3]
l2=[3,4,5,2]
l3=[]

for i in l1:
    if i in l2 and i not in l3:
        l3.append(i)
print(l3)

