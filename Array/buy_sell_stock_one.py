#Author: JC
#Date: 7/18/2018
#Version: 1.0

def try_buy_sell(A):
    max_i, max_j, max_value = 0, 0, 0
    for i in range(len(A)):
        for j in reversed((range(len(A)))):
            if i < j and A[i] < A[j]:
                if abs(A[i] - A[j]) > max_value:
                    max_value = abs(A[i] - A[j])
                    max_i = i
                    max_j = j
    print(max_value,A[max_i],A[max_j])

A= [310,315,275,295,260,270,290,230,255,250]
try_buy_sell(A)

def buy_and_sell_Stock_once(prices):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

x= buy_and_sell_Stock_once(A)
print(x)