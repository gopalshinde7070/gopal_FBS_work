# 12. Python Program to count number of lowercase characters in a string.
s1=input("Enter the string : ")

c=0
for i in s1:
    if i.islower():
        c+=1
print(c)