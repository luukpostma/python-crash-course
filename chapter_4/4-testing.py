# Een for loop gaat bij elk item in een list lang.
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)

# Je kunt verschillende dingen met deze for loops doen.
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

# Als je nog een functie toevoegd aan de for loop, word de lijst opnieuw uitgevoert.
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

# Hier begin je met een lege lijst om vervolgens de getallen 1 t/m 10 berekent tot het kwadraat 2. (1, 4, 9, 16, etc.)
# Je voegt daarna die getallen toe aan de varaible square en voegt ze toe aan de lijst door de append() functie, om vervolgens de lijst te vullen & te printen.
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