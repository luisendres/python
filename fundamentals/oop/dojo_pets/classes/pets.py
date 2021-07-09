class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, health = 100, energy = 100):
        self.name = name
        # self.type = type
        # self.tricks = tricks
        self.health = health
        self.energy = energy
# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25;
        print(f"{self.name} has slept energy has increased to : {self.energy}")
        return self
# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} has eaten health has increased to : {self.health}")
        print(f"{self.name} has eaten energy has increased to : {self.energy}")
        return self
# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"{self.name} played health has increased to : {self.health}")
        return self
# noise() - prints out the pet's sound
    def noise(self):
        print(f"{self.name} makes sound")
        return self

# class Dog(Pet):
#     def __init__(self, name, health = 100, energy = 100):
#         super().__init__(name, health, energy)

# class Cat(Pet):
#     def __init__(self, name, health = 100, energy = 100):
#         super().__init__(name, health, energy)