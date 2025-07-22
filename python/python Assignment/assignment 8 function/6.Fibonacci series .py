def fibonacci(num):
    a,b=0,1
    for i in range(1,num+1):
        print(a)
        a,b=b,a+b
num=int(input("Enter the number : "))
fibonacci(num)