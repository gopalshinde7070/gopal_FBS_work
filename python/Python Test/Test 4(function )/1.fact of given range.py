# write a function to which we pass a paremeter and print the factor of given number
# for eg : 12 :factorial of given number 
def facto(num,fact=1):   
    for i in range(1,num+1):
        if(num%i==0):
            fact*=i
            print(fact)
num=int(input("enter the number : "))
facto(num)
