from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name ,age):
        self.name = name
        self.age = age
        self.__legs = 4

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def setName(self, name):
        pass
    
    @abstractmethod
    def getAge(self):
        pass
   
    @abstractmethod
    def getLegs(self):
        pass

class Interface(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal, Interface):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "Bark"
     

    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
        
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
    
    def speak(self):
        print(self.__sound)
    
    def getLegs(self):
        return self.__legs


class Cat(Animal, Interface):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "Meow"

    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def speak(self):
        print(self.__sound)
    
    def getLegs(self):
        return self.__legs

class Panda(Animal, Interface):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "growl"
    

    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def speak(self):
        print(self.__sound)
    
    def getLegs(self):
        return self.__legs

class Bear(Animal, Interface):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "growl"

    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def speak(self):
        print(self.__sound)
    
    def getLegs(self):
        return self.__legs

class Camel(Animal, Interface):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "grunt"

    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def speak(self):
        print(self.__sound)
    
    def getLegs(self):
        return self.__legs

class Deer(Animal, Interface):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "bell"

    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def speak(self):
        print(self.__sound)
    
    def getLegs(self):
        return self.__legs

class Donkey(Animal, Interface):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "bray"

    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def speak(self):
        print(self.__sound)
    
    def getLegs(self):
        return self.__legs

class Horse(Animal, Interface):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "neigh"

    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def speak(self):
        print(self.__sound)
    
    def getLegs(self):
        return self.__legs


class Jackals(Animal, Interface):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "howl"

    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def speak(self):
        print(self.__sound)
    
    def getLegs(self):
        return self.__legs

class Lion(Animal, Interface):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)
        self.__sound = "roar"


    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def speak(self):
        print(self.__sound)
    
    def getLegs(self):
        return self.__legs

