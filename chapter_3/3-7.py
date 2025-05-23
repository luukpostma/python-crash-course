guest_list = ["michael Jackson", "ed matthes", "justin bieber", "lebron james"]
print(f"Just got a message that {guest_list[3]} can not make it to dinner.")

guest_list[3] = ("Katy Perry")
print(f"You are invited to dinner tonight {guest_list[0].title()}!")
print(f"You are invited to dinner tonight {guest_list[1].title()}!")
print(f"You are invited to dinner tonight {guest_list[2].title()}!")
print(f"You are invited to dinner tonight {guest_list[3].title()}!")

print("I just found a bigger dining table, let's invite more peope!")

guest_list.insert(0, "mat steward")
guest_list.insert(2, "taylor swift")
guest_list.append("joe rogan")
print(guest_list)

print(f"You are invited to dinner tonight {guest_list[0].title()}!")
print(f"You are invited to dinner tonight {guest_list[1].title()}!")
print(f"You are invited to dinner tonight {guest_list[2].title()}!")
print(f"You are invited to dinner tonight {guest_list[3].title()}!")
print(f"You are invited to dinner tonight {guest_list[4].title()}!")
print(f"You are invited to dinner tonight {guest_list[5].title()}!")
print(f"You are invited to dinner tonight {guest_list[6].title()}!")

print("I just found out the bigger dining table will not arrive in time, so I only have room for 2 guests.")

print(guest_list)

guest_1 = guest_list.pop()
guest_2 = guest_list.pop()
guest_3 = guest_list.pop()
guest_4 = guest_list.pop()
guest_5 = guest_list.pop()

print(f"Sorry {guest_1.title()}, I do not have enough room to invite you. I'm sorry.")
print(f"Sorry {guest_2.title()}, I do not have enough room to invite you. I'm sorry.")
print(f"Sorry {guest_3.title()}, I do not have enough room to invite you. I'm sorry.")
print(f"Sorry {guest_4.title()}, I do not have enough room to invite you. I'm sorry.")
print(f"Sorry {guest_5.title()}, I do not have enough room to invite you. I'm sorry.")

# Zelfde als hierboven, maar dan iets efficienter met een for loop.
# not_guest = guest_1, guest_2, guest_3, guest_4, guest_5

# for not_invited in not_guest:
#     print(f"Sorry {not_invited.title()}, I do not have enough room to invite you to dinner tonight I'm Sorry.")

# Nog sneller, je bewaart de namen in de range van de eerste 5 in een list genaamd not_guest.
# not_guest = []
# for _ in range(5):
#     not_guest.append(guest_list.pop())

# Daarna kun je ook een berichtje sturen met een for loop.
# for name in not_guest:
# print(f"Sorry {name.title()}, I do not have enough room to invite you to dinner tonight. I'm sorry.")

print(f"I only have room for 2 people, so you are invited {guest_list[0].title()}.")
print(f"I only have room for 2 people, so you are invited {guest_list[1].title()}.")

# Zelfde als hierboven, maar dan iets efficienter met een for loop.
# for names in guest_list:
#     print(f"I only have room for 2 people, so you are invited {names.title()}!")

print(guest_list)

del guest_list[0]
del guest_list[0]

# Dit verwijderd alle items in een list.
# del guest_list[:]

print(guest_list)
