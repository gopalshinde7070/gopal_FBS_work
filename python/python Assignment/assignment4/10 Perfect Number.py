num=int(input("Enter the number :"))

perfect=0

for i in range(1,num):
    if(num%i==0):
        perfect+=i
if(num==perfect):
    print("perfect number")