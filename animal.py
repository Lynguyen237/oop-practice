class Animal:
    species = None
    hunger = 50

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self, greet = 'Hey'):
        print(f"{greet}, I am {self.name} the {self.species}.")
    

class Cat(Animal):
    
    # You could declare all the attributes of Cat again
    # def __init__(self, name):
    #     self.name = name
    #     self.species = 'cat'

    # Or Use super().methodName(arguments)
    def __init__(self, name):
        super().__init__(name, 'cat')

    def purr(self):
        print(f'{self.name} enfurs you')
    
    #Subclass can override their parents' methods
    def speak(self):
        print(f'Meow, I am {self.name} the {self.species}')


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name, 'dog')


    #super() function invoke methods that were defined on a parent class
    #subclass can add additional "actions" to the parent method
    def speak(self):
        super().speak()
        print("Woof woof")
    
    #super() method can also be called after the subclass-specific actions
    # def speak(self):
    #     print("Woof woof")
    #     return super().speak()


class Duck(Animal):

    def __init__(self, name):
        super().__init__(name, 'duck')
    

    # Subclass' method can take different arguments from the parent method
    # This is done by having a parameter with default value in the parent method
    # In this case the speak(self, greet = "Hey") method has a default parameter at the parent level
    # At the child level, we only need to feed in the modified greet value
    def speak(self):
        super().speak('Quack')


#==== Test =====
katy = Cat("Katy")
whisk = Cat('Whisk')
nick = Dog("Nick")
duckie = Duck('Duckie')

animals = [katy, whisk, nick, duckie]

for animal in animals:
    animal.speak()

# ==== Resources ====
'''
Melon Production Homework: https://fellowship.hackbrightacademy.com/materials/pt7g/homework/melon-production/ 
Solution: https://fellowship.hackbrightacademy.com/materials/pt7g/homework/melon-production/solution/

Class handout: https://fellowship.hackbrightacademy.com/materials/pt7g/lectures/classes-2/
'''