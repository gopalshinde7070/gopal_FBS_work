# 3. Python Program to Detect if Two Strings are Anagrams
s1=input("Enter the anagrams word: ").lower()
s2=input("Enter the anagrams word: ").lower()
s1=s1.replace(" ","")
s2=s2.replace(" ","")

l1=list(s1)
l1.sort()
print(l1)
l2=list(s2)
l2.sort()

if(len(s1)==len(s2)):
    if(l1==l2):
        print("same")
    else:
        print("Not same")
    
else:
    print("Not a ")       