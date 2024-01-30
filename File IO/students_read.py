students = []

with open("../File IO/students.csv") as file:
    for line in file:
        name, address = line.rstrip().split(",")
        #students.append(f"{name} is in {address}")
        #print(f"{name} is in {address}") #directly print to console
        student = {"name": name, "address": address}
        #student = {}
        #student["name"] = name
        #student["address"] = address
        students.append(student)

#for student in sorted(students):
#    print(student)
#print(students)

def get_name(student):
    return student["name"]

for student in sorted(students, key = get_name):
    print(f"{student['name']} is in {student['address']}.")