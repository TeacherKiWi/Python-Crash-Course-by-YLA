""" 3-10. Every Function: Think of something you could store in a list. For example,  you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items  and then uses each function introduced in this chapter at least once. """

locations_last = ["Bagan", "Pataya", "Egypt", "Great Wall", "Greek"]

print(locations_last)

print("Welcome to " + locations_last[0])

popped_locations = locations_last.pop(0)
print(popped_locations)

del locations_last[0]
print(locations_last)

locations_last.append("Inlay")
print(locations_last)

locations_last.insert(0, "Mandalay")
print(locations_last)

locations_last[1] = "Yangon"
print(locations_last)

locations_last.remove("Great Wall")
locations_last.remove("Greek")
print(locations_last)



locations = ["Bagan", "Pataya", "Egypt", "Great Wall", "Greek"]

print(len(locations))

# sorted() function
print(sorted(locations))
print(locations)
# reverse() method
locations.reverse()
print(locations)

locations.reverse()
print(locations)
# sort()method
locations.sort()
print(locations)
# reverse in sort()method
locations.sort(reverse=True)
print(locations)

