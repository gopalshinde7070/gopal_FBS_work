internal_wall=int(input("Enter the internal wall:"))
internal_meter=int(input("Enter the internal feet:"))
internal_cost=int(input("Enter the internal cost:"))

a=internal_meter*internal_cost*internal_wall

print("cost of internal painting :",a)

external_wall=int(input("Enter the  external wall:"))
external_meter=int(input("Enter the external feet:"))
external_cost=int(input("Enter the  external cost:"))

b=external_wall*external_meter*external_cost

print("cost of external painting :",b)
c=a+b

print("cost of two room painting:",c)