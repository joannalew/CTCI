# LeetCode 322: Coin Change
# You are given coins of different denominations 
#   and a total amount of money amount. 
# Write a function to compute the fewest number of coins that 
#   you need to make up that amount. 
# If that amount of money cannot be made up by any combination 
#   of the coins, return -1.

# Example: coins = [1, 2, 5], amount = 11
#   Output: 3
#   Explanation: 11 = 5 + 5 + 1

# Example: coins = [2], amount = 3
#   Output: -1

def coinChange(coins, amount):
    rows = len(coins)
    cols = amount + 1
    memo = [[amount + 1 for y in range(cols)] for x in range(rows)]
    memo[0][0] = 0

    for i in range(rows):
        for j in range(cols):
            if j < coins[i] and i == 0:
                continue
            elif i == 0:
                memo[i][j] = memo[i][j - coins[i]] + 1
            elif j < coins[i]:
                memo[i][j] = memo[i - 1][j]
            else:
                memo[i][j] = min(memo[i - 1][j], memo[i][j - coins[i]] + 1)

    res = -1 if memo[-1][-1] > amount else memo[-1][-1]
    return res

def main():
    print(coinChange([1, 2, 5], 11)) # => 3
    print(coinChange([1, 5, 6, 8], 11)) # => 2
    print(coinChange([2], 3)) # => -1


if __name__ == "__main__":
    main()


# Solve it:
# Make a chart to keep track of min coins
# rows = coin values, cols = 0...amount
# initialize all values to max (amount + 1), set memo[0][0] = 0
# fill out the first row
# row element is min between (prev row, same column) 
#   and ((same row, column - coin value) + 1)

# Example: coinChange([1, 5, 6, 8], 11)
#    | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11
#  1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11
#  5 | 0 | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 | 5 | 2  | 3
#  6 | 0 | 1 | 2 | 3 | 4 | 1 | 1 | 2 | 3 | 4 | 2  | 2
#  8 | 0 | 1 | 2 | 3 | 4 | 1 | 1 | 2 | 1 | 2 | 2  | 2

# Ref: https://www.youtube.com/watch?v=Y0ZqKpToTic 