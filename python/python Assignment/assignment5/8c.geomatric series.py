n=int(input("Enter the number : "))
sum_series=0
term=1
for i in range(n):
    sum_series+=term
    term*=2
print("sum of geomatric series",sum_series)