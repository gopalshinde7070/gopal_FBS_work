# 1. Python Program to Put Even and Odd elements of a List into two Different Lists
l1=[1,2,3,4,5,67,8,9,11,12,13,14,15,15,16]
even =[]
odd=[]
for i in range(len(l1)):
    if(l1[i]%2==0):
        even+=[l1[i]]
    else:
        odd+=[l1[i]]
print("even : ",even)
print("odd",odd)