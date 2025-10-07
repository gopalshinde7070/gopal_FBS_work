# 13. Python Program to count number of digits and letters in a string.
s1=input("Enter the string : ")
c=0
for i in s1:
    if i.isdigit():
        c+=1
print(c)