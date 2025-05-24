# Vraag de gebruiker om zijn of haar naam.
# Print een begroeting, (Leuk dat je je boeken komt delen)
# Maak een lege lijst voor boeken
# Vraag 3 keer een boek van de gebruiker
# Print daarna een genummerde lijst van de boeken
# Laat de gebruiker nog een boek toevoegen
# Sorteer de lijst alfabetisch en print hem opnieuw
# Print het totaal aantal boeken in de lijst.

naam = input("Voer je naam in:\n")
print(f"Hallo {naam.title()}, leuk dat je je favoriete boeken komt delen!")
print("Ik ga je vragen om 3 van je favoriete boeken te delen.")

favoriete_boeken = []

for i in range(3):
    boek = input("Voer een boek in:\n")
    favoriete_boeken.append(boek.title())
print(f"1. {favoriete_boeken[0]}\n2. {favoriete_boeken[1]}\n3. "
      f"{favoriete_boeken[2]}")

laatste_boek = input("Voer nog een laatste boek in:\n")
favoriete_boeken.append(laatste_boek.title())
favoriete_boeken.sort()

print("Hier print ik de boeken op alfabetische volgorde:\n")

for boek in favoriete_boeken:
    print(boek.title())
