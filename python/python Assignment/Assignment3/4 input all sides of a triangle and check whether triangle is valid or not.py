# 4. Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1=int(input("Enter side1:"))
side2=int(input("Enter side2:"))
side3=int(input("Enter side3:"))

if(side1<=side2+side3 and side2<=side1+side3 and side3<=side1+side2):
    print("this is valid")
else:
    print("This is not valid")