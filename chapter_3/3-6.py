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