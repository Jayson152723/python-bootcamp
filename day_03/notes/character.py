class Character:
    def __init__(self, health = 10, strength = 10, defense = 10):
        self.health = health
        self.strength = strength
        self.defense = defense

    def attack(self, other):
        damage = self.strength - other.defense
        other.health -= damage

class Knight:
    def __init__(self, health = 10, defence = 10):
        self.health = health
        self.defense = defense
    def attack(self):
        damage = self.defence - other.defense
        other.health

player = Character(strength=100)
enemy = Character()

player.attack(enemy)
print(enemy.health)