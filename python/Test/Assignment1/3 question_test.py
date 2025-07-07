# write a program acept distance in km and convert it into meter and centimeter

km=int(input("enter the distance:"))

m=(km*0.3248)+(km*0.0254)
cm=m*100

print("meter is :",m)
print("centimeter is:",cm)
