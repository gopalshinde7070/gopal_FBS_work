num=int(input("Enter the number : "))
sum=0
while(num!=0):
    a=num%10
    num=num//10
    fact=1
    for i in range(1,a+1):
        fact*=i
        fact1=i%fact
    sum+=fact1
print(sum)
 