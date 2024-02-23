class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing Name!")
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slythering']:
            raise ValueError("Invalid House!")
        self.name = name
        self.house = house
        self.patronus = patronus
        

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🙄"
            case "Otter":
                return "🥴"
            case "Jack Russel Terrier":
                return "🌚"
            case _:
                return "🖊️"

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    student =  Student(name, house, patronus)
    return student

if __name__=="__main__":
    main()