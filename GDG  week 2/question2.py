prices =[120, 45, 300, 85, 150]
def get_expensive_products(prices):
       expensive=[]
       for x in prices:
            if x> 100:
               expensive.append(x)
       return expensive
print (get_expensive_products(prices))