# 12. Write a program to create three lists of numbers, their squares and cubes
l1=[1,2,3,4,5]
square=[]
cube=[]
for i in range(len(l1)):
    square+=[l1[i]*2]
    cube+=[l1[i]**3]

print("square: ",square)
print("cube  : ",cube)
print("number: ",l1)