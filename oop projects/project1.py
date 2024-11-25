from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

# Child class inheriting from abstract class
class Dog(Animal):
    def sound(self):
        return "Woof!"

# Another child class inheriting from abstract class
class Cat(Animal):
    def sound(self):
        return "Meow!"

# Child class with additional methods
class Bird(Animal):
    def sound(self):
        return "Chirp!"

    def fly(self):
        return f"{self.name} is flying."

# Using the classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")

print(dog.name + ": " + dog.sound())
print(cat.name + ": " + cat.sound())
print(bird.name + ": " + bird.sound())
print(bird.fly())
