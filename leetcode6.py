prices = [2,4,1]
length = len(prices)
buy = prices[0]
i = 0
while i <= length-1:
    if buy >= prices[i]:
        buy = prices[i]
    i += 1
if prices.index(buy) == length:
    sell = buy
else:
    sell = prices[prices.index(buy)]
    for i in range(prices.index(buy), length):
        if sell <= prices[i]:
            sell = prices[i]
final = sell - buy
print(final)
print(buy)
print(sell)

# Above is my solution, below is the working one:

# buy = prices[0]
# profit = 0
# for i in range(1, len(prices)):
#     if prices[i] < buy:
#         buy = prices[i]
#     elif prices[i] - buy > profit:
#         profit = prices[i] - buy
# return profit