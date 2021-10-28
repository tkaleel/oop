# characters
# halflings
# dwarves
# humans


class Character:
    def __init__(self, name, health=100, attack_strength=5, defense_strength=5):
        self.name =  name
        self.health = health
        self.attack_stength = attack_strength
        self.defense_strength = defense_strength

    def info(self):
        print(self.name)
        print(f"health: {self.health}")
        return self


class Halfling(Character):
    def __init__(self, name, health=100, attack_strength=25, defense_strength=30):
        super().__init__(self, name, health, attack_strength, defense_strength)

char1 = Character('bob')
char1.info()
p1 = Halfling('frodo')
p1.info()