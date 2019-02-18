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