# 9. WAP to print all numbers in a range divisible by a given number.

start=int(input("Enter the start point :"))
end=int(input("Enter the end point :"))

number=int(input("divisible by number :  "))

for i in range(start,end):
    if(i%number==0):
        print(i)