def prime(num):
    sum=0
    for i in range(2,num+1):
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            sum+=i
    return sum
num=int(input("ENter the number : "))
a=prime(num)
print(a)