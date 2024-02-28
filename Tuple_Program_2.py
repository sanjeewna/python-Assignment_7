names_set = set()

while True:
    name = input("Enter a name (or press Enter to finish): ")

    if name == "":
        break

    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)

print("\nList of names:")
for name in names_set:
    print(name)