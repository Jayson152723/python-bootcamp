from abc import abstractmethod, ABC


class Character(ABC):
    # template for specific character

    def __init__(self, health=10, defence=10):
        self.health = health
        self.defense = defence

    @abstractmethod
    def attack(self, other):
        raise NotImplemented

class Knight(Character):

    def attack(self, other):
        damage = self.defense - other.defense
        other.health -= damage
        
class Mage(Character):
    def __init__(self, health = 10, defense = 10, magic = 10):
        super().__init__(health, defense)
        self.magic = magic

    def attack(self, other):
        damage = self.defense - other.defense
        other.health -= damage

class Warrior(Character):
    def __init__(self, health = 20, defense = 20, strength = 50):
        super().__init__(health, defense)
        self.strength = strength

    def attack(self, other):
        damage = self.defense - other.defense
        other.health -= damage

knight1 = Knight()
knight2 = Mage()
knight1.attack(knight2)
print(knight2.health)