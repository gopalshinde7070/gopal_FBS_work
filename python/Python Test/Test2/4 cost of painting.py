
internal=input("only available for internal room (yes)/(no) : ")

if(internal=="yes"):

  meter=int(input("1 room meter is : ")) 
  
  room=int(input("Enter the room : "))
  
  m1price=meter*10
  
  price=m1price*room
  
  
  print("total bill is ",price)
else:
    print("sorry for next time")

