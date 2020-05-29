class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Dog(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "Bark"

    def speak(self):
        print(self.__sound)

class Cat(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "Meow"

    def speak(self):
        print(self.__sound)

class Panda(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "growl"

    def speak(self):
        print(self.__sound)

class Bear(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "growl"

    def speak(self):
        print(self.__sound)

class Camel(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "grunt"

    def speak(self):
        print(self.__sound)

class Deer(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "bell"

    def speak(self):
        print(self.__sound)

class Donkey(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "bray"

    def speak(self):
        print(self.__sound)

class Horse(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "neigh"

    def speak(self):
        print(self.__sound)


class Jackals(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "howl"

    def speak(self):
        print(self.__sound)

class Lion(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "roar"

    def speak(self):
        print(self.__sound)
