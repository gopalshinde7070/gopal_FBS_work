# 2. Python Program to Remove the nth Index Character from a Non-Empty String
s=input("Enter the charecter : ")
l=list(s)
#print(l)
l.pop(-1)
#print(l)
p="".join(l)
print("remone n of number : ",p)