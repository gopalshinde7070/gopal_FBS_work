# write a program to accept 3 digit number. if frist digit is double of second digit and half of third 
# digit then display "yes" you have done it" otherwise display "please try next time".
num=int(input("Enter the num"))

a=num%10

num=num//10
b=num%10

c=num//10

if(c>b and c<a):
    print("yes")
else:
    print("try next time")