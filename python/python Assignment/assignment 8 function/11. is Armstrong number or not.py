def seprate(num):
    count=0
    while(num!=0):
        num//=10
        count+=1
    return count

def armstrong(num):
    sum=0
    am=seprate(num)
    while(num!=0):
        a=num%10
        num//=10
        sum+=a**am
    return sum
num=int(input("Enter the num : "))
a=armstrong(num)
if(a==num):
    print("ARmstrong number")
else:
    print("Not a armstrong ")
