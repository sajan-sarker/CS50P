#names = []

#for _ in range(3):
#    name = input("Enter name: ")
#    names.append(name)

#for name in sorted(names):
#    print(f"Hello, {name}")

# Store in file as unsorted format.
with open("../File IO/names.txt", "a") as file:
    for i in range(5):
        name = input(f"Enter {i+1} name: ")
        file.write(f"{name} \n")