# 10.Python Program to Take in Two Strings and Display the Larger String without Using 
# Built-in Functions

s1 = input("Enter the string 1 : ")
s2 = input("Enter the string 2: ")

length1=0
length2=0
for _ in s1:
    length1+=1

for _ in s2:
    length2+=1

print(length1)
print(length2)

if(length1>length2):
    print("s1 is grether  ")
elif(length2>length1):
    print("s2 isgrether  ")
else:
    print("s1 and s2 same")
