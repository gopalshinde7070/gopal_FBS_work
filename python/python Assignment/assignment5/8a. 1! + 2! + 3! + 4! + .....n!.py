#8.a. 1! + 2! + 3! + 4! + .....n!
fact=1
sum=0

i=1
num=int(input("Enter the number : "))

while(i<=num):
    fact*=i
    
    sum+=fact


    i+=1
    print(sum)