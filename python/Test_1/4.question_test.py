# calculate the cost of painting the following buildings walls (both interior and exteriror).you need to accept area and cost of both interior and exterior wall

internal_wall=int(input("enter the internal wall"))

external_wall=int(input("enter the external wall:"))

internal_cost=float(input("enter the internal_cost:"))
external_cost=float(input("enter the external_cost:"))

a=internal_wall*internal_cost

b=external_wall*external_cost

x=internal_wall+internal_cost

print("internal wall or  internal cost is: ",x)

y=external_wall*external_cost
print(" external wall or external cost is: ",x)


c=a+b

print(c)