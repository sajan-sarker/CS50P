import csv

name = input("Enter name: ")
home = input("Enter Home: ")

with open("../File IO/students.csv", "a", newline='') as file:
    #writer = csv.writer(file)  #using writer function
    #writer.writerow([name, home])  #using writer function
    writer = csv.DictWriter(file, fieldnames=["name", "home"])  #using DictWriter function
    writer.writerow({"name": name, "home": home})   #using DictWriter function