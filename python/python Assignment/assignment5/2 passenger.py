'''3. Accept no. of passengers from user and per ticket cost. Then accept age of each
passenger and then calculate total amount to ticket to travel for all of them based on
following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.'''
i=1
total=0
passenger=int(input("Enter the passenger :"))
ticket=100
while(i<=passenger):
    age=int(input("Enter the age : "))
    if(age<12):
        total+=ticket-(ticket*0.30)
    elif(age>59):
        total+=ticket-(ticket*0.50)
    else:
        total+=ticket
    
    #print("Total bill is : ",total)
    i+=1
print("total bill : ₹" ,total)