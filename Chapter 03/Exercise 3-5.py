""" 3-5. Changing Guest List: You just heard that one of your guests can’t make the  dinner, so you need to send out a new set of invitations. You’ll have to think of  someone else to invite.
•	Start with your program from Exercise 3-4. Add a print statement at the  end of your program stating the name of the guest who can’t make it.
•	Modify your list, replacing the name of the guest who can’t make it with  the name of the new person you are inviting.
•	Print a second set of invitation messages, one for each person who is still  in your list. """

guest_list = [ "eaint hana", "aqua", "may", "lu lu aung" ]

removed_guest = guest_list.pop(1)

print(f"{removed_guest} can't be invited to have dinner.")

guest_list.insert(1, "hazel byur san san")

print(f"Dear {guest_list[0].title()}, I would like to invite you to have dinner.")
print(f"Dear {guest_list[1].title()}, I would like to invite you to have dinner.")
print(f"Dear {guest_list[2].title()}, I would like to invite you to have dinner.")
print(f"Dear {guest_list[3].title()}, I would like to invite you to have dinner.")

