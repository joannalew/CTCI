# CLRS Rod cutting
# https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture12.pdf

# Given a rod of length n inches and an array of prices 
#   that contains prices of all pieces of size smaller than n. 
# Determine the maximum value obtainable by cutting up the rod 
#   and selling the pieces. 

# For example, if length of the rod is 8 and the values 
#   of different pieces are given as following, 
#   then the maximum obtainable value is 22 
#   (by cutting in two pieces of lengths 2 and 6)

# length   | 1   2   3   4   5   6   7   8  
# --------------------------------------------
# price    | 1   5   8   9   10  17  17  20

# And if the prices are as following, 
#   then the maximum obtainable value is 24 
#   (by cutting in eight pieces of length 1)

# length   | 1   2   3   4   5   6   7   8  
# --------------------------------------------
# price    | 3   5   8   9   10  17  17  20

INT_MIN = -32767

def cutRod(prices, n):
    val = [0] * (n + 1)
    
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
            max_val = max(max_val, prices[j] + val[i - j - 1])
        val[i] = max_val

    return val[n]

def main():
    print(cutRod([1, 5, 8, 9, 10, 17, 17, 20], 8))
    print(cutRod([3, 5, 8, 9, 10, 17, 17, 20], 8))
    print(cutRod([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 10))

if __name__ == "__main__":
    main()

