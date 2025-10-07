# 6. Python Program to Find the Union of two Lists
l1=[1,2,3]
l2=[3,4,5]
l1.extend(l2)
print(l1)
l3=[]

for i in range(len(l1)):
    if l1[i] not in l3:
        l3.append(l1[i])
print(l3)