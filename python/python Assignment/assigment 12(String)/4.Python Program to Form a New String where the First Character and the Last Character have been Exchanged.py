# 4. Python Program to Form a New String where the First Character andthe Last Character have
#  been Exchanged
s1=input("Enter the string 2  : ")

if(len(s1)<=2):
    print("Your string are alpha 2 above need : ")
else:
    frist=(s1[0])
    last=(s1[-1])
    medium=(s1[1:-1])

    print("fc: ",frist)
    print("mc: ",medium)
    print("lc: ",last)
    print("final: ", last+medium+frist)