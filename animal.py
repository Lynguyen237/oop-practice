class Animal:
    species = None
    hunger = 50

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"Hey, I am {self.name} the {self.species}")
    

class Cat(Animal):
    
    # def __init__(self, name):
    #     self.name = name
    #     self.species = 'cat'

    # Use super().methodName(arguments)
    def __init__(self, name):
        super().__init__(name, 'cat')

    def purr(self):
        print(f'{self.name} enfurs you')
    
    #Subclass can override their parents' methods
    def speak(self):
        print(f'Meow, I am {self.name} the {self.species}')
    

katy = Cat("Katy")
whisk = Cat('Whisk')
