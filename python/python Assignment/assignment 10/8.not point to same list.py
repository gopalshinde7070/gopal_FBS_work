# 8. Write a program to create a duplicate of an existing list. It should not point to same 
# list.

l1=[1,2,3,4,5]
# l2=l1.copy()
# l2=l1[:]

l2=list(l1)
l1.clear()
print(l1)
print(l2)