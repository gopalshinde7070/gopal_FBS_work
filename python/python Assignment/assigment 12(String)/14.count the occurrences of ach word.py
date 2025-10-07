# 14. Python Program to count the occurrences of ach word in a string.

s1="my name is and my name gopal but name is name 1"
s2=s1.split()
print(s2)
s3=[]
for i in range(len(s2)):
    if s2[i] not in s3:
        s3.append(s2[i])

for i in range(len(s3)):
    print(s3[i],":",s2.count(s3[i]))