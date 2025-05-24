foods = ("burger", "pizza", "friet", "cake", "cookie")
# foods[2] = "cracker" - Je kan de waarde van een item in een tuple niet wijzigen.
for food in foods:
    print(food)

foods = ("burger", "cracker", "friet", "cake", "ice cream")
print("\nThe new menu:")
for food in foods:
    print(food)
    