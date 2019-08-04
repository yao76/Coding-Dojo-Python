class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def add_lion(self, name):
        self.animals.append(name)
    def add_tiger(self, name):
        self.animals.append(name)
    def add_dragon(self, name):
        self.animals.append(name)
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        # print(f"Name: {self.name} Age: {self.age} Health: {self.health} Happiness: {self.happiness} Guests Eaten: {kwargs.get('guests_eaten', self.guests_eaten)}")
        print(f"Name: {self.name} Age: {self.age} Health: {self.health} Happiness: {self.happiness}")
    
    def feed(self):
        self.happiness += 10
        self.health += 10

class Lion(Animal):
    def __init__(self, name, age, health = 80, happiness = 80):
        super().__init__(name, age, health, happiness)
class Tiger(Animal):
    def __init__(self, name, age, health = 75, happiness = 50):
        super().__init__(name, age, health, happiness)
# class Dragon(Animal):
#     def __init__(self, name, age, health = 100, happiness = 100, guests_eaten = 10):
#         super().__init__(name, age, health, happiness)
#         self.guests_eaten = guests_eaten
class Dragon(Animal):
    def __init__(self, name, age, health = 100, happiness = 100):
        super().__init__(name, age, health, happiness)


tony = Tiger("Tony", 15)
simba = Lion("simba", 10,100,100)
iroh = Dragon("Iroh", 1000, 500, 200)
zoo1 = Zoo("John's Zoo")
zoo1.add_lion(simba)
zoo1.add_tiger(tony)
zoo1.add_dragon(iroh)
# zoo1.add_lion("Simba",30)
# zoo1.add_tiger("Rajah")
# zoo1.add_tiger("Shere Khan")
zoo1.print_all_info()

tony.feed()
simba.feed()
iroh.feed()

zoo1.print_all_info()


# simba.display_info()
# simba.feed()
# simba.display_info()

# 
# iroh.display_info()

