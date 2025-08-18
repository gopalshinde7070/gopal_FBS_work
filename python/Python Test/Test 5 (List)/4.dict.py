# 4. There is a list with some numbers. Create a new
# dictionary using this list in such a way that key is
# number and value is frequency of occurrence of that
# number in list.

# [1,3,4,1,2,3,6,7,1,2,4]
# {1:3,3:2,2:2,}
l=[1,3,4,1,2,3,6,7,1,2,4]
l1=[]
l2=[]

dic={}
for i in l:
    if(i not in l1):
        l1.append(i)
print(l1)

for i in l1:
    l2=l.count(i)
    dic[i]=l2
print(dic)

