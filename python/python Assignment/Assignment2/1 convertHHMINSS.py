# 1. Convert the time entered in hh,min and sec into seconds. 
hour=int(input("enter the hrs:"))
minute=int(input("enter the minute:"))
second=int(input("enter the minute"))
total_second=hour*3600+minute*60+second
print("total number of second is:",total_second)