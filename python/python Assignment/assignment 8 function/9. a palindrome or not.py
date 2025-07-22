def palindrome(num):
    rev=""
    for i in num:
        rev=i+rev
    if(rev==num):
        return("polindrome")
    else:
        return ("not")
num=input("Enter num ")
a=palindrome(num)
print(a)