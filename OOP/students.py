class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    #Getters
    @property
    def name(self):
        return self._name
    
    @property
    def house(self):
        return self._house

    #Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name!")
        self._name = name
    
    @house.setter
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slythering']:
            raise ValueError("Invalid House!")
        self._house = house

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student =  Student(name, house)
    return student

if __name__=="__main__":
    main()