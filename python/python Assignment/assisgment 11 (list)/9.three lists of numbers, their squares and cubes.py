# 9. Write a program to create three lists of numbers, their squares and cubes
l1=[10,20,30]
cube=[]
square=[]
num=[]
for i in l1:

    cube.append(i**2)
    square.append(i**3)
    num.append(i)

print(cube)

print(square)

print(num)

