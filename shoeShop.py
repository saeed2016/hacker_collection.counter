from collections import Counter
shoeSize = list(input("please enter size of shoes:").split(","))
cusCount = int(input("please enter number of Customer"))
orders = []
amount = 0

while cusCount > 0:
    size, price = input("please enter shoe size and it's price:").split(",")
    orders.append([size, price])
    cusCount -= 1
shoeSize=Counter(shoeSize)
for order in orders:
    #breakpoint()
    if order[0] in shoeSize.keys():
        if shoeSize[order[0]]>0:
            amount = amount + int(order[1])
    shoeSize[order[0]]-=1

#Sizes1 = Sizes
#Prices1 = Prices
#orders = {size: price for size in Sizes for price in Prices if Prices.index(price) == Sizes.index(size)}
#print(len(Sizes))
#print(orders)
print(amount)
#print(Counter(shoeSize).items())
#print(Counter(shoeSize)['45'])