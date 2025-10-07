# 5. Python Program to Count the Number of Vowels in a String
s1=input("Enter the sentace : ")
c=0
for i in s1:
    if(i in "aeiou"):
        c+=1
print("vowel :",c)