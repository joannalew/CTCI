# LeetCode 121: Best Time to Buy and Sell Stock
# Say you have an array for which the ith element 
#   is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction
#   (i.e., buy one and sell one share of the stock), 
#   design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.

# Example: Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), 
#   profit = 6-1 = 5.


def maxProfit(prices):
    numPrices = len(prices)
    if numPrices < 2:
        return 0
    
    profit = [0] * numPrices
    low = prices[0]

    for i in range(1, numPrices):
        if prices[i] < low:
            low = prices[i]
        
        profit[i] = max(prices[i] - low, profit[i - 1])
    
    return profit[-1]
            
def main():
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]))

if __name__ == "__main__":
    main()