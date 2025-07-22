# 10. Write a program to check if entered year is a leap year or not.
def leap(year):
    if((year%4==0 and year%100!=0)or(year%400==0)):
        return "leap year"
    else:
        return "Not a leap year"

year=int(input("Enter the year : "))
a=leap(year)
print(a)