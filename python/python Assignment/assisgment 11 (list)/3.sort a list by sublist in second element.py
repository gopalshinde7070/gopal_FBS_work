# 3. Python Program to Sort the List According to the Second Element in Sublist
l1=[[9,0],[7,6]]
for pas in range(1,len(l1)):
    for i in range(len(l1)-pas):
        if(l1[i][1]> l1[i+1][1]):
            l1[i],l1[i+1]=l1[i+1],l1[i]
print(l1)