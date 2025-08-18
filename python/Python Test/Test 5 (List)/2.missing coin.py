# 2. A teacher came to class with a large box tokhat has several coins. Each coin has a number printed on it.
# Before coming to class, she ensured that All the numbers occur an Even number of times. However,
# while coming to the class, one coin fell down and got lost. She wants to find out the number on the missing coin.

# Inputs: The original number of coins and the actual number on each of the coins, separated by spaces.

# Output: The number on the missing coin Sample 

# Input: 8
# 5 7 2 7 5 2 5

# Sample Output: 5

n = int(input("Enter the coin "))   
coins = list(map(int, input("coin name : ").split()))

for coin in coins:
    if coins.count(coin) % 2 != 0:   
        print("missing coin is :", coin)
        break
