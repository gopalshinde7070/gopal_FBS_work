# 10 Write a program to remove all occurrences of a given element in the list.
l1=[1,2,3,4,5,5,4]

l=[]
x=int(input("Enter the delete element : "))

for i in range(len(l1)):
    if(l1[i]!=x):
        l+=[l1[i]]
print(l)