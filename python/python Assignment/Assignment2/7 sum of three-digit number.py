# 7. Find the sum of three-digit number.
num=int(input("Enter Three Digit Number:"))
a=num%10
num=num//10
c=num%10
d=num//10
sum=a+c+d
print(sum)