
print("exercise 1")
message = "i am gonna be most rich people in my entie bloodline"
print(message)

message = "i am gonna richest person in this country"
print(message)

print("exercise 2")
freind = "shazan"
print(f"hello {freind.title()} hope you are good")
print(f"hello {freind.title()}")
print(f"hello {freind.upper()}")
print(f"hello {freind.lower()}")

print("albert einstein once said, \"A person who never made a mistake never tried anything new\"")

name = "\t\n  daksh  \n\t"

print("Original:", repr(name))
print("Left strip:", repr(name.lstrip()))
print("Right strip:", repr(name.rstrip()))
print("Full strip:", repr(name.strip()))

file_name = "python_notes.txt"
print(file_name.removesuffix(".txt"))

print("exercise 3")

print(5+3)
print(9-1)
print(16/2)
print(4*2)

favourite_number = 1
print(f"my favourite number is {favourite_number}")

print("exercise 4")

names = ["shazan", "avaya", "ayush", "aman"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

print(f"welcome my dear freind {names[0]}")
print(f"welcome my dear freind {names[1]}")
print(f"welcome my dear freind {names[2]}")
print(f"welcome my dear freind {names[3]}")

mototrcycle = ["honda", "ducati", "bmw", ]

print(f"i would like to own {mototrcycle[0]}")
print(f"i would like to own {mototrcycle[1]}")
print(f"i would like to own {mototrcycle[2]}")

guests = ["Albert einstine", "Elon musk", "A.P.j Abdul Kalam",]

print(f"I would like you to invite for the dinner my guest {guests[0].title()}")
print(f"I would like you to invite for the dinner my guest {guests[1].title()}")
print(f"I would like you to invite for the dinner my guest {guests[2].title()}")

guests[0] = "Shera bhai"

print(f"I would like you to invite for the dinner my guest {guests[0].title()}")
print(f"I would like you to invite for the dinner my guest {guests[1].title()}")
print(f"I would like you to invite for the dinner my guest {guests[2].title()}")

print("Everone there is a good news that i have found a bigger table so i would like to invite more people ")

guests.insert(0, "Ada Lovelace")
guests.insert(2, "Alan Turing")
guests.append("Leonardo da Vinci")

print(f"I would like you to invite for the dinner my guest {guests[0].title()}")
print(f"I would like you to invite for the dinner my guest {guests[1].title()}")
print(f"I would like you to invite for the dinner my guest {guests[2].title()}")
print(f"I would like you to invite for the dinner my guest {guests[3].title()}")
print(f"I would like you to invite for the dinner my guest {guests[4].title()}")
print(f"I would like you to invite for the dinner my guest {guests[5].title()}")

print("Everone there is a bad news that the bigger table is not available we can invite  only two people ")

removed_guest0 = guests.pop()
removed_guest1 = guests.pop()
removed_guest2 = guests.pop()
removed_guest3 = guests.pop()

print(f"Sorry {removed_guest0}, I cannot invite you to dinner.")
print(f"Sorry {removed_guest1}, I cannot invite you to dinner.")
print(f"Sorry {removed_guest2}, I cannot invite you to dinner.")
print(f"Sorry {removed_guest3}, I cannot invite you to dinner.")

# Step 6: Invite the remaining two guests
print(f"\nDear {guests[0]}, you are still invited to dinner!")

print(f"Dear {guests[1]}, you are still invited to dinner!")

# Step 7: Delete the remaining guests
del guests[0]
del guests[0]

# Step 8: Print the empty list
print("\nFinal Guest List:")
print(guests)





