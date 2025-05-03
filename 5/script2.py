a1 = {2, 3, 1}
a2 = {"c", "a", "b"}
s3 = list(zip(a1, a2))
print(s3,"\n")

##################################################################

b1 = [1000, 2000, 3000, 4000]
b2 = [10000, 20000, 30000, 40000]

for x, y in zip(b1, b2[ ::- 1]):
    print(x, y)

####################################################################

stocks = {"reliance", "infosys", "tcs", }
price = {1250, 65000, 659000}

new_dict = {stocks: price for stocks, price in zip(stocks, price)} 
print('\n{}'.format(new_dict))