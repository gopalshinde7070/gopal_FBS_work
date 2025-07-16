# 3. WAP to print sum of series upto n.

n=int(input("Enter the number : "))
add=0

for i in range(1,n+1):
    add+=i
    print(add)