# 12. Write a program to check if given 3 digit number is a palindrome or not.
num=int(input("Enter number"))

#orignal=num

a=num%10
num1=num//10
b=num1%10
reverse=a*10+b

c=num1//10

reverse=reverse*10+c

print(reverse)

if(num==reverse):
    print("yes")
else:
    print("no")