# print in unsorted format.
#with open("../File IO/names.txt") as file:
#    lines = file.readlines()

#for line in lines:
#    print("Hola,", line.strip())
#print(type(lines))

names = []

with open("../File IO/names.txt") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    print(f"Hola, {name}")