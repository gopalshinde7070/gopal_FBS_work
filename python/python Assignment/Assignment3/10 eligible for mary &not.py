# 10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

gender=input("Enter the gender (male/female):")

age=int(input("enter the age : "))

if(gender=="male" or gender=="female"):
    
    if(gender=="male"):
       if(age>=21):
           print("yes")
           
       else:
        print("no")
    else:
       
       if(age>=18):
          print("you are marry")
       else:
              print("sorry your age is 18 year below")
else:
    print("please Enter correct gender")