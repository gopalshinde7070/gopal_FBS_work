# 1. WAP to print all even numbers until n.

n=int(input("end point : "))

for i in range(1,n+1):
    if(i%2==0):
        print(i)
