num=int(input("Enter the number : "))
i=1
count=0
while(count<num):
    j=2
    while(j<i):
        if(i%j==0):
            break
        j+=1
    else:
        print(i)
        count+=1
    i+=1