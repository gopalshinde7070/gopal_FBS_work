rows = 4

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=" ")

    num = 1
    for j in range(i + 1):
        print(num, end="   ")
        num = num * (i - j) // (j + 1)

    print()

#       1   
#     1   1   
#   1   2   1   
# 1   3   3   1

