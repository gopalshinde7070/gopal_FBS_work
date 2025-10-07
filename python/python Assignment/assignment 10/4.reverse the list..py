# 4. Write a program to reverse the list.
l1=[10,20,30,40,50]
l2=l1[0]

for pas in range(1,len(l1)):
    for i in range(len(l1)-pas):
        if(l1[i] < l1[i+1]):
            l1[i],l1[i+1]=l1[i+1],l1[i]
print(l1)