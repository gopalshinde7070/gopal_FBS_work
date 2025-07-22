people=int(input("Enter the people"))
for i in range(1,people+1):
    salary=int(input("Entre the num : "))
    if(salary<20000):
        da=0.10*salary
        ta=0.12*salary
        hrs=0.15*salary
        total=da+ta+hrs+salary
        print(total)
    
    elif(salary>=20000):
        da=0.15*salary
        ta=0.18*salary
        hrs=0.20*salary
        total=da+ta+hrs+salary
        print(total)
    else:
        print("Enter carrect value")