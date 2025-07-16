start=int(input("Enter the number : "))
stop=int(input("Enter the number : "))
for num in range(start,stop+1):
    temp=num
    count=0
    while(num!=0):

        a=num%10
        num=num//10
        count+=1

    num=temp

    sum=0

    while(num!=0):
    
      a=num%10
      num=num//10
      sum=sum+(a**count)
    


    if(temp==sum):
        print(sum)

