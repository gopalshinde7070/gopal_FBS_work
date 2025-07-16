i=1

while(i<=3):
    u=input("Enter  the User_Name : ")
    pa=input("Enter the password  : ")
    if(u=="go" and pa=="pass"):
        print("login sucessfully ")
        break
    else:
        print("user_name and password  incorrect")
    i+=1