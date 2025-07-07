#10. Write a program to reverse three-digit number.
value=int(input("Enter the three digit number "))
a=value%10
value=value//10
b=value%10
reverse=a*10+b
c=value//10
reverse=reverse*10+c
print("This is reverse value:",reverse)

