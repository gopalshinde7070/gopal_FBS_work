def sumofdigit(num):
    sum=0
    for i in num:
        sum+=int(i)
    return(sum)
num=input("ENter the num")

a=sumofdigit(num)
print(a)