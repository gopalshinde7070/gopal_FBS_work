def sum(num):
    sum=0
    for i in range(1,num+1):
        if(i%2!=0):
            sum+=i
    return sum

num=int(input("ENter the nuber : "))
a=sum(num)
print(a)
