# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

sub1=int(input("Enter the sub1 mark :"))
sub2=int(input("Enter the sub2 mark :"))
sub3=int(input("Enter the sub3 mark :"))
sub4=int(input("Enter the sub4 mark :"))
sub5=int(input("Enter the sub5 mark :"))


mark=sub1+sub2+sub3+sub4+sub5
over=(mark/500)*100
print(over)

if(over>=80 and over<=100 ):
    print("excelent")

elif(over>=70 and over<80 ):
    print("frist class")

elif(over>=60 and over<70 ):
    print("second class")

elif(over>=50 and over<60 ):
    print("Thrid class")

elif(over>=40 and over<50 ):
    print("pass")

elif(over>=0 and over<40):
    print("fail")

else:
    print("wrong output")