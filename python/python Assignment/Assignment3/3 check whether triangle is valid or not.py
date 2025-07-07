# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

angle1=int(input("Enter the angle 1 :"))
angle2=int(input("Enter the angle 1 :"))
angle3=int(input("Enter the angle 1 :"))

if(angle1+angle2+angle3==180 and angle1>0 and angle2>0 and angle3>0 ):
    print("Tringle is valid")
else:
    print("tringle is not valid")   