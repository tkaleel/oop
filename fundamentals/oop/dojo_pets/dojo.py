class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    def walk(self):
        Pet.play(self)
        return self
    
    def feed(self):
        Pet.eat()

    def bathe(self):
        Pet.noise()

class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print("*SCREAMS*")

theo = Ninja("Theo", "Kaleel", "Sachiko", 5, 5)
sachiko = Pet("Sachiko", "Shiba", "sit", 100, 100)

# testing Pet method sleep()
# print(sachiko.energy)
# sachiko.sleep()
# print(sachiko.energy)

theo.walk()
