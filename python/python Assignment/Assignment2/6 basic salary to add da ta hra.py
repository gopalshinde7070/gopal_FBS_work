#6.WAP to calculate total salary of employee based on basic,da=10% of basic,ta=12%of basic,hra=15%of basic.
basic_salary=float(input("basic salary:"))
da=0.10*basic_salary
ta=0.12*basic_salary
hra=0.15*basic_salary
total_price=basic_salary+ta+da+hra
print("Total price is :",total_price,".rs")