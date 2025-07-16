num=int(input("Enter the amaunt"))
temp=num

add=0

while(num!=0):  
    a=num//500                                                             
    num=num%500
    
    b=num//200
    num=num%200
    
    c=num//100
    num=num%100

    d=num//50
    num=num%50

    e=num//20
    num=num%20

    f=num//10
    num=num%10
    print(num)
    add+=a+b+c+d+e
print("Total Number of notes ₹500 : ",a)
print("Total Number of notes ₹200 : ",b)
print("Total Number of notes ₹100 : ",c)
print("Total Number of notes ₹ 50 : ",d)
print("Total Number of notes ₹ 20 : ",e)
print("Total Number of notes ₹ 10 : ",f)
print("Total notes used :",add)