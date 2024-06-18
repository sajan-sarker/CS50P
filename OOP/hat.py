import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slyntherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
    
Hat.sort("Harry")