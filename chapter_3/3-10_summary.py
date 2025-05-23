# Dit was mijn overzicht van de belangrijkste lijst-functies in hoofdstuk 3.
# Vooral append(), pop(), remove(), sort(), sorted() en len() zijn superhandig en komen vaak terug in echte programma’s.



voetballers = ["cristiano ronaldo", 'lionel messi', "luis suarez", "virgil van dijk"]
autos = ["bmw", "volvo", "audi", "volkswagen"]
lettertypes = ["helvetica", "arial", "open sans", "neue haas grotesk"]
nederlandse_steden = ["leeuwarden", "almere", "groningen", "eindhoven"]

# Pak een item uit de list, en met de title() functie maak je de eerste letters van het woord / de woorden hoofdletters.
voetballers = ["cristiano ronaldo", 'lionel messi', "luis suarez", "virgil van dijk"]
print(voetballers[1].title())

# Indexeren, hiermee pak je de index van een list, in dit geval nummer 2, daarmee pak je het 3e item uit een list.
autos = ["bmw", "volvo", "audi", "volkswagen"]
print(autos[2])

# Voeg een item toe aan de list. Met de append() functie word het item aan het einde van de list toegevoegd.
nederlandse_steden = ["leeuwarden", "almere", "groningen", "eindhoven"]
nederlandse_steden.append("den helder")
print(nederlandse_steden)

# Voeg een item toe op een specifieke plaats met de insert() functie.
lettertypes = ["helvetica", "arial", "open sans", "neue haas grotesk"]
lettertypes.insert(1, "monaspace")
print(lettertypes)

# del functie, verwijderd een item van een list. Je moet het item wel indexeren of [:] gebruiken om de hele lijst leeg te maken.
# del autos[:] verwijderd alle items in de list.
# Werkt op index en niet op waarde. Het is daarnaast ook een statement en geen functie.
autos = ["bmw", "volvo", "audi", "volkswagen"]
del autos[1]
print(autos)

# Met de pop() functie verwijder je het laatste item van een list, maar deze kun je hergebruiken als je het in een variable bewaard.
# Je verwijdert standaard het laatste item, of je geeft een index op om een specifiek item te verwijderen.
voetballers = ["cristiano ronaldo", 'lionel messi', "luis suarez", "virgil van dijk"]
voetballer_1 = voetballers.pop()
# Je kunt het ook los gebruiken, maar dan kun je er niks meer mee.
voetballers.pop()
print(voetballers)
# Je kunt ook aangeven welke van de items je wilt verwijderen.
# Het is makkelijk om in een variable te bewaren voor bijvoorbeeld online gebruikers van een website.
# Als ze offline gaan worden ze eruit 'gepopt' en kun je ze toevoegen aan een list van offline gebruikers.
voetballer_2 = voetballers.pop(1)
print(voetballer_2)
# Nu zit er nog maar 1 voetballer in de lijst.
print(voetballers)

# Verwijderd een item van een list, maar dan op basis van waarde.
# Dit is handig als je precies weet welke waarde je wilt verwijderen. Het verwijderd vervolgens de eerste beste gelijke waarde in de list.
# Als je meerdere van dezelfde items hebt in de list, kun je een loop gebruiken om er vaker door heen te gaan.
autos = ["bmw", "volvo", "audi", "volkswagen"]
autos.remove("bmw")
print(autos)

# Met de sort() functie, kun je een lijst op alfabetische volgorde sorteren.
lettertypes = ["helvetica", "arial", "open sans", "neue haas grotesk"]
# Hiermee kun je alle items bij langsgaan met een for loop en vervolgens de title() functie toepassen de eerste letter van elk woord met een hoofdletter te laten beginnen.
lettertypes = [naam.title() for naam in lettertypes]
lettertypes.sort()
print(lettertypes)
# Je kunt een lijst ook reversen met de reverse() functie.
lettertypes.reverse()
print(lettertypes)
# Dit kan ook in 1 zin.
print(sorted(lettertypes, reverse=True))

# Met de len() functie kun je zien wat de 'lengte'is van je list.
nederlandse_steden = ["leeuwarden", "almere", "groningen", "eindhoven"]
len(nederlandse_steden)
# Sneller alternatief.
print(len(nederlandse_steden))

# Met de sorted() functie kun je in combinatie met een nieuwe variable, een nieuwe gesorteerde list maken terwijl je de originele in tact laat.
# Handig als je de originele lijst wilt bewaren en alleen tijdelijk wilt sorteren, zoals bij een tijdelijke weergave op een website of in een app.
voetballers = ["cristiano ronaldo", 'lionel messi', "luis suarez", "virgil van dijk"]
sorted_voetballers = sorted(voetballers)
print(sorted_voetballers)

# Met de sort() functie in combinatie met key=, kun je de lijst in dit geval op len(lengte) sorteren.
# Je kunt met key= op meerdere manieren je lijst sorteren.
lettertypes = ["helvetica", "arial", "open sans", "neue haas grotesk"]
lettertypes.sort(key=len)
print(lettertypes)