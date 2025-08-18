# 5. Python Program to Find the Union of two Lists without
# using set concept.
l1=[1,2,3,5,6,1,1]
l2=[1,3,7,5,9,8,7,2,3,5]
unique=[]
for j in l2:
    l1.append(j)

for i in l1:
    if i not in unique:
        unique.append(i)
print(unique)
