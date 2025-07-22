def reverse(num):
    rev=0
    while(num!=0):
      a=num%10
      num//=10
      rev=rev*10+a
    return rev
num=int(input("Enter the number : "))
a=reverse(num)
print(a)