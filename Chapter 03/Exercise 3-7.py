""" 3-7. Shrinking Guest List: You just found out that your new dinner table won’t  arrive in time for the dinner, and you have space for only two guests.
•	Start with your program from Exercise 3-6. Add a new line that prints a  message saying that you can invite only two people for dinner.
•	Use pop() to remove guests from your list one at a time until only two  names remain in your list. Each time you pop a name from your list, print  a message to that person letting them know you’re sorry you can’t invite  them to dinner.
•	Print a message to each of the two people still on your list, letting them  know they’re still invited.
•	Use del to remove the last two names from your list, so you have an empty  list. Print your list to make sure you actually have an empty list at the end  of your program. """

guest_list = [ "eaint hana", "aqua", "may", "lu lu aung" ]

removed_guest = guest_list.pop(1)

# print(f"{removed_guest} can't be invited to have dinner.")

guest_list.insert(1, "hazel byur san san")

guest_list.insert(0, "thinzar wint kyaw")
guest_list.insert(3, "shoon shoon")
guest_list.append("noe noe")

print(f"I am sorry that I can invite only two people from the list.\n")

removed_guest = guest_list.pop(4)
print(f" I am sorry that I can't invite {removed_guest.title()} to dinner.")
removed_guest = guest_list.pop(3)
print(f" I am sorry that I can't invite {removed_guest.title()} to dinner.")
removed_guest = guest_list.pop(2)
print(f" I am sorry that I can't invite {removed_guest.title()} to dinner.")
removed_guest = guest_list.pop(1)
print(f" I am sorry that I can't invite {removed_guest.title()} to dinner.")
removed_guest = guest_list.pop(0)
print(f" I am sorry that I can't invite {removed_guest.title()} to dinner.")

print(f"\nDear {guest_list[0].title()} and {guest_list[1].title()}, you are still invited to dinner.\n")

del guest_list[1]
del guest_list[0]

print(guest_list)