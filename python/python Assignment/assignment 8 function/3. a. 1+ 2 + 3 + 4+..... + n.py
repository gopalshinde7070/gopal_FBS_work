# a. 1+ 2 + 3 + 4+..... + n
def sum(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum

# b. 1!+ 2! + 3! + 4!+..... + n!
def facto(num):
    sum=0
    while(num!=0):
        a=num%10
        num//=10
        fact=1
        for i in range(1,a+1):
            fact*=i
        sum+=fact
    return sum

# c. 1^1 + 2^2 + 3^3+ ...... n^n
def ff(num):
    sum=0
    for i in range(1,num+1):
        a=num**i
    sum+=a
    return sum

while True:
    print("1. 1+ 2 + 3 + 4+..... + n")
    print("2. 1!+ 2! + 3! + 4!+..... + n!")
    print("3. 1^1 + 2^2 + 3^3+ ...... n^n")
    print("4. Exit")
    ch=input("Enter the above option : ")
    if(ch=="1"):
        num=int(input("Enter the number  : "))
        a=sum(num)
        print(a)
        input("Press Enter to continue...")
        print()
    elif(ch=="2"):
        num=int(input("Enter the number : "))
        a=facto(num)
        print(a)
        input("Press Enter to continue...")
        print()
    elif(ch=="3"):
        num=int(input("Enter the number : "))
        a=ff(num)
        print(a)
        input("Press Enter to continue...")
        print()
    elif(ch=="4"):
        print("Goodbye")
        break
    else:
        print("Enter correct option")
        input("Press Enter to continue...")
        print()

print("Enter multiple lines (type 'end' to finish):")
lines = ""
while True:
    line = input()
    if line.lower() == "end":
        break
    lines += line + "\n"

print("You typed:\n", lines)
