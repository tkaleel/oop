class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        else:
            print("Oh no!!! you need more pet food!")
        return self

    def bathe(self):
        self.pet.noise()

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
        print(self.name, ": *SCREAMS*")

sachiko = Pet("Sachiko", "Shiba", "sit", 100, 100)
theo = Ninja("Theo", "Kaleel", "peanut butter", ['tuna', 'salmon', 'homework'], sachiko)


# testing Pet method sleep()
# print(sachiko.energy)
# sachiko.sleep()
# print(sachiko.energy)

theo.walk().feed().feed().feed().feed().bathe()
