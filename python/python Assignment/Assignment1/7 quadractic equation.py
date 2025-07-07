a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

ans=(b*b)-(4*a*c)
ans=ans**0.5

root1=(-b+ans)/2*a
root2=(-b-ans)/2*a

print("root1: ",root1)
print("root2:",root2)