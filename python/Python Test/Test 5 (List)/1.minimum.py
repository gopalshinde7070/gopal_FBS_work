# 1. A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.

d=[2000,500,200,100,50,20,10,5]

am=120450
n=0
for i in d:
    n+=am//i
    am=am%i
print(n)