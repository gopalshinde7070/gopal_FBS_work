# Convert distant given in feet and inches into meter and centimeter.
feet=int(input("Enter The Feet:"))
inches=int(input("Enter The Inches"))

meter=(feet*0.3048)+(inches*0.0254)
centimeter=(meter*100)

print(meter)
print(centimeter)

