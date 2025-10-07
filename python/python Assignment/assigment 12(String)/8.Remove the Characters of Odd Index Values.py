# 8. Python Program to Remove the Characters of Odd Index Values in a String
s=input("Enter the string : ")

new_list=list(s)

new=[]
for i in range(len(new_list)):
   if(i%2==0):
       new.append(new_list[i])
# print(new)

a="".join(new)
print(a)
# print(type(a))