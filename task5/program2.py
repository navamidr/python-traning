class Animal:
    def speak(self):
        print("sound")
class Dog(Animal):
    def speak(self):
        print("I Bark")
class Cat(Animal):
    def speak(self):
        print("I Meow")

dog=Dog()
cat=Cat()
dog.speak()
cat.speak()