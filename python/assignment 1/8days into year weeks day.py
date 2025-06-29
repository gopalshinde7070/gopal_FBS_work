days=int(input("Enter the days:"))
year=days//365
r_day=days%365

week=r_day//7
dd=r_day%7

print("year is:",year)
print("weeks is:",week)
print("days into day reamining:",dd)
