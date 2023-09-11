''' 2-7. Stripping Names: Store a person’s name, and include some whitespace  characters at the beginning and end of the name. Make sure you use each  character combination, "\t" and "\n", at least once. 
    Print the name once, so the whitespace around the name is displayed.  Then print the name using each of the three stripping functions, lstrip(),  rstrip(), and strip(). '''

name = "\tMg Hla\n"

print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())




