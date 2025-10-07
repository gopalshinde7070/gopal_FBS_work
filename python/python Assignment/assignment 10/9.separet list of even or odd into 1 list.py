# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

l1=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in range(len(l1)):
    if(l1[i]%2==0):
        even+=[l1[i]]
    elif(l1[i]%2!=0):
        odd+=[l1[i]]

print("even: ",even)
print("odd : ",odd)