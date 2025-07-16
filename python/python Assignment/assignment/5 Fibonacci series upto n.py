# 5. WAP to print Fibonacci series upto n.

n=int(input("Enter the number : "))

a,b=0,1

for _ in range(1,n+1):
    print(a)
    a,b=b,a+b