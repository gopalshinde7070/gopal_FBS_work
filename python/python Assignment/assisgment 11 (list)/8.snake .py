# 8. Print 1 to 100 in snakes and ladder pattern.

main=[]
sublist=[]
row=1
for i in range(1,101):
    sublist.append(i)
    if(i%10==0):
        if(row%2==0):
            sublist.reverse()
        main.append(sublist)
        sublist=[]
        row+=1
main.reverse()
for i in main:
    print(i)