# write a program to find factorial of given number using recrsion of all no in given range
def fa(num):
    if(num==1):
        return 1
    return num *fa(num-1)

def f(num):
  if(num==1):
     return
  f(num-1)
  print(fa(num))
num=int(input("Enter the number "))
a=f(num)
print(a)