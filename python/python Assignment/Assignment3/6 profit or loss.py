cost_price=int(input("enter the cost price:"))
selling_price=int(input("Enter the selling_price :"))

if(selling_price>cost_price):
    profit=selling_price-cost_price
    print("Your profit is :",profit)
elif(selling_price<cost_price):
    loss=cost_price-selling_price
    print("you loss :",loss)
else:
    print("you are not profit & loss:")