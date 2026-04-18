def maxProfit(prices: list[int]) -> int:
    maxP = 0
    minBuy = prices[0]

    for sell in prices:
        maxP = max(maxP, sell - minBuy)
        minBuy = min(minBuy, sell)
    return maxP

if __name__ == "__main__": 
    print(maxProfit([10,1,5,6,7,1]))
