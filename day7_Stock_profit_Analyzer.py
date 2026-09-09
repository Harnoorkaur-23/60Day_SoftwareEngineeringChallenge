prices=list(map(int,input("Enter stock prices:").split()))
min_price=price[0]
max-profit=[0]
buy_day=0
sell_day=0
for i in range(1,len(prices)):
   if prices[i]<min_price:
     min_price=prices[i]
     buy_day=i
   profit=prices[i]-min_price
  if profit>max_profit:
     max_profit=profit
     sell_day=i
print("Maximum profit:",max_profit)
if max_profit>0:
   print("Buy on day:",buy_day+1)
   print("sell on day:",sell_day+1)
   print("Buy prices:",prices[buy_day])
    print("sell prices:",prices[sell_day])
else:
  profit("no profit can be made")

