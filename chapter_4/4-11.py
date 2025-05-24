pizzas = ["carbonara", "milano", "calzone"]
friends_pizzas = ["carbonara", "milano", "calzone"]

pizzas.append("salami")
friends_pizzas.append("hawaii")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza.title())