# 2. Write a program to find maximum and minimum element in a list.
list1=[24,36,84,10,33,5]
print(list1)

# minimum number
small=list1[0]
for i in range(1,len(list1)):
    if(small>list1[i]):
        small=list1[i]
print("minimum number: ",small)

# maximum number
big=list1[0]
for i in range(1,len(list1)):
    if(big < list1[i]):
        big=list1[i]
print("maximum number: ",big)