# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort
l1=[2,4,8,3,1,]

for pas in range(1,len(l1)):
    for i in range(len(l1)-pas):
        if(l1[i] > l1[i+1]):
            l1[i],l1[i+1]=l1[i+1],l1[i]

print(l1[-2])