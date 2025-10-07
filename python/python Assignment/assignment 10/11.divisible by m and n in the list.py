# Write a program to print all numbers which are divisible by m and n in the list.

l=[1,2,3,4,5,6,7,8,9,10]
l2=[]
m=int(input("Enter the m number : "))
n=int(input("Enter the n number : "))
for i in range(len(l)):
    if(l[i]%m==0 and l[i]%n==0):
        l2+=[l[i]]
print(l2)
