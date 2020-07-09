toppings = ['pepperoni', 'pinapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
print ("We sell " + str(num_pizzas) + " different kinds of pizza!")
print ("")

pizzas = list(zip(prices, toppings))
pizzas.sort()
print (pizzas)
print ("")

cheapest_pizza = pizzas[0]
print (cheapest_pizza)
print ("")

priciest_pizza = pizzas[-1]
print (priciest_pizza)
print ("")

three_cheapest = pizzas[:3]
print(three_cheapest)
print ("")

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
