# 5. WAP to print Fibonacci series upto n.

n=int(input("Enter the number : "))

a,b=0,1
i=1
while(i<=n):
    print(a)
    a,b=b,a+b
    i+=1