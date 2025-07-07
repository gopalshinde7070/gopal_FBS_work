""" 8. Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)"""
import random

user_id=input("Enter the User_Id :  ")
password=input("Enter the password : ")


if(user_id=="gopal" and password=="Gopal@7070" ):
    captcha=random.randint(1000,9000)
    print(captcha)
    a=int(input("Enter The above Number:"))
    if(a==captcha):
        print("login succesfully")
    else:
        print("envalid captcha")

else:
    print("invalid user_id & password")