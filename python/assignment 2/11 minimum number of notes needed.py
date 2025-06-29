am=int(input("Enter The Amount:"))
n500=am//500
r_am=am%500

n200=r_am//200
r_am=r_am%200

n100=r_am//100
r_am=r_am%100

n50=r_am//50
r_am=r_am%50

n20=r_am//20
r_am=r_am%20

n10=r_am//10

print("number of 500.RS notes:",n500)
print("number of 200.RS notes:",n200)
print("number of 100.Rs notes:",n100)
print("number of  50.RS notes:", n50)
print("number of  20.RS notes:", n20)
print("number of  10>RS notes:", n10)