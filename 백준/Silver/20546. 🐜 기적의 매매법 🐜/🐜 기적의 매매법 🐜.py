import sys 

input = sys.stdin.readline 

totalMoney = int(input().rstrip())

stockPrices = list(map(int,input().rstrip().split()))

#성민 
aMoney = totalMoney 
aStock = 0 
for stock in stockPrices:
    stockBuyable = aMoney // stock
    if stockBuyable >0:
        aStock += stockBuyable
        aMoney -= (stockBuyable*stock)

aMoney += (stockPrices[13]*aStock)
    
bMoney = totalMoney
bStock = 0 
for i in range(3,len(stockPrices)):
    #매도  
    if stockPrices[i-3] <stockPrices[i-2] < stockPrices[i-1] < stockPrices[i]:
        bMoney += (bStock * stockPrices[i])
        bStock = 0 
    elif stockPrices[i-3] > stockPrices[i-2] > stockPrices[i-1] > stockPrices[i]:
        #매수
        stockBuyable = bMoney // stockPrices[i]
        if stockBuyable >0:
            bStock += stockBuyable
            bMoney -= (stockBuyable*stockPrices[i])  

bMoney += (stockPrices[13]*bStock)

#print(aMoney,bMoney)
if aMoney > bMoney: 
    print("BNP")
elif aMoney < bMoney: 
    print("TIMING")
else: 
    print("SAMESAME")

