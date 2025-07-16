num=int(input("Enter number : "))
temp=num
sum=0
while(num!=0):
    a=num%10
    num=num//10

    fact=1

    for i in range(1,a+1):
        fact*=i

    sum+=fact

if(sum==temp):
    print("This is strong number ")
else:
    print("Not a strong number ")