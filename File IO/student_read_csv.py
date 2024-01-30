import csv

students = []

# read the csv file using reader function.
#with open("../File IO/students.csv") as file:
#    reader = csv.reader(file)
#    for name, home in reader:
#        students.append({"name": name, "home": home})

#read the csv file using DictReader function.
with open("../File IO/students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #print(row)
        students.append({"name": row['name'], "home": row['home']})


for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student["name"]} is from {student["home"]}.")
