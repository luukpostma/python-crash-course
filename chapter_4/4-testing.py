# Een for loop gaat bij elk item in een list lang.
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

# Je kunt verschillende dingen met deze for loops doen.
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# Als je nog een functie toevoegde aan de for loop, wordt de lijst opnieuw uitgevoerd.
# Als je 2 print functies hebt, dan gaat het eerste item eerst door de TWEE! functies heen.
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show.")

# Range() function.
for value in range(1, 5):
    print(value)

# Range en list function.
numbers = list(range(1, 5))
print(numbers)

# het toevoegen van een derde argument bij de range() functie.
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Hier begin je met een lege lijst om vervolgens de getallen 1 tot en met 10 berekent tot het kwadraat 2. (1, 4, 9, 16, etc.)
# Je voegt daarna die getallen toe aan de variable square en voegt ze toe aan de lijst door de append() functie, om vervolgens de lijst te vullen & te printen.
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# Kortere variant.
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# Nog kortere variant door list comprehension.
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# Slicen van een list.
players = ["charles", "martina", "michael", "eli"]
print(players[0:3])

# Slicen van een list
players = ["charles", "martina", "michael", "eli"]
print(players[:2])

# Gedeelte van een list printen met een for loop.
players = ["charles", "martina", "michael", "eli", "florence"]
for player in players[0:3]:
    print(player.title())

# Het koperen van een list en toevoegen aan een nieuwe variable.
my_foods = ["pizza", "falafel", "carrot cake"]
friends_food = my_foods[:]

# append() functie om iets verschillends toe toevoegen and en de list.
my_foods.append("hamburger")
friends_food.append("apple")

print("My favorite foods are:")
print(my_foods)

print("My friends favorite foods are:")
print(friends_food)


# Een tuple word gebruikt als een lijst, maar we gebruiken hier haakjes.
# Een item in een tuple is een vast waarde, en kan je dus niet veranderen.
# Wordt veel gebruikt voor bijvoorbeeld dimensies van een vierkant op een website.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Door een tuple heen lopen en waarde wijzigen door de complete variable te wijzigen.
# Je kan dus alleen de waarde veranderen als je de complete variable wijzigt.
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    
