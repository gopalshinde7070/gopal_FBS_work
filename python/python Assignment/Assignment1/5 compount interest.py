# 5. Write a program to enter P, T, R and calculate Compound Interest.
p=int(input("Enter The Principle"))
t=int(input("Enter The Time:"))
r=int(input("Enter The Rate:"))
a=p*(1+r/100)**t
ci=a-p

print(ci)