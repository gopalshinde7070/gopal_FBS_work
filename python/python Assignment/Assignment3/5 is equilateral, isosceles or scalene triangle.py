# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

angle1=int(input("Enter the angle1 : "))
angle2=int(input("Enter the angle2 : "))
angle3=int(input("Enter the angle3 : "))

if(angle1 is angle2 is angle3):
    print("equilateral")
elif(angle1==angle2 or angle2==angle3 or angle1==angle3):
    print("isosceles")
else:
    print("scalena")