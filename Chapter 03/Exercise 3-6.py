""" 3-6. More Guests: You just found a bigger dinner table, so now more space is  available. Think of three more guests to invite to dinner.
•	Start with your program from Exercise 3-4 or Exercise 3-5. Add a print  statement to the end of your program informing people that you found a  bigger dinner table.
•	Use insert() to add one new guest to the beginning of your list.
•	Use insert() to add one new guest to the middle of your list.
•	Use append() to add one new guest to the end of your list.
•	Print a new set of invitation messages, one for each person in your list. """

guest_list = [ "eaint hana", "aqua", "may", "lu lu aung" ]

removed_guest = guest_list.pop(1)

print(f"{removed_guest} can't be invited to have dinner.")

guest_list.insert(1, "hazel byur san san")

guest_list.insert(0, "thinzar wint kyaw")
guest_list.insert(3, "shoon shoon")
guest_list.append("noe noe")


print(f"Dear {guest_list[0].title()}, I would like to invite you to have dinner.")
print(f"Dear {guest_list[1].title()}, I would like to invite you to have dinner.")
print(f"Dear {guest_list[2].title()}, I would like to invite you to have dinner.")
print(f"Dear {guest_list[3].title()}, I would like to invite you to have dinner.")
print(f"Dear {guest_list[4].title()}, I would like to invite you to have dinner.")
print(f"Dear {guest_list[5].title()}, I would like to invite you to have dinner.")
print(f"Dear {guest_list[6].title()}, I would like to invite you to have dinner.")


