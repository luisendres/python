from classes.ninja import Ninja
from classes.pets import Pet

class Dog(Pet):
    def __init__(self, name, health = 100, energy = 100):
        super().__init__(name, health, energy)

class Cat(Pet):
    def __init__(self, name, health = 100, energy = 100):
        super().__init__(name, health, energy)

luis = Ninja("Luis","Endres",pet = Cat("Fluffy"))
grace = Ninja("Grace","Lucas", pet = Dog("Brooklyn"))

print(luis.pet.name)
print(luis.pet.health)

print(grace.pet.name)
print(grace.pet.health)

luis.pet.sleep()
luis.walk().feed().bath().pet.sleep()

grace.pet.sleep()
grace.walk().feed().bath().pet.sleep()