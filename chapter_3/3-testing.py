motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# Voegt een item toe op het einde van de list.
motorcycles.append("ducati")
print(motorcycles)

# Voegt een item toe op de aangegeven plek.
motorcycles.insert(1, "ducati")
print(motorcycles)

# Verwijdert het item op de aangegeven plek.
del motorcycles[1]
print(motorcycles)

# Pakt het item uit de list zodat je het kan hergebruiken.
last_owned_motorcycles = motorcycles.pop(2)
print(f"My last motorcycle was a {last_owned_motorcycles.title()}")

# Verwijdert een item dat gelijk is aan de gegeven waarde van de variable uit de list.
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# Gebruik van een for loop zorgt er voor dat je meerder instaties van dezelfde waarde kan verwijderen uit de list.
motorcycles = ["honda", "ducati", "yamaha", "suzuki", "ducati"]
print(motorcycles)

too_expensive = "ducati"

for x in motorcycles:
    if x == too_expensive:
        motorcycles.remove(too_expensive)

print(motorcycles)

# Sorteren en Reversen van een list.
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
cars.sort(reverse=True)
print(cars)

print("This is the original list.")
print(cars)
print("This is the sorted list.")
print(sorted(cars))

# Gebruik deze manier om de list te ordenen op alfabetische volgorde en vervolgens te reversen.
print("This is the reversed list.")
print(sorted(cars, reverse=True))

# Deze funtie reversed alleen de list, maar doet niets aan alfabetische volgorde.
cars.reverse()
print(cars)

# Hiermee krijg je de lengte van een list, in dit geval dus 4.
len(cars)