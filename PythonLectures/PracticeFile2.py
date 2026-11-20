# Lecture 8 Object Oriented Programming
# return multiple values/vars - e.g. return name, house, pair with multiple var assignment
# tuples - immutable lists, can change lists/mutable objects nested in tuples tho
# classes/objects
#... syntax
# attributes of classes and objects
# can make ur own methods for objects/classes
# dunder init/__init__ method - intialising contents of a class
# dunder str/__str__ - control what print(object) is - so not somehting weird like main.XXXXX, user friendly
# can create our own string methods - not like dunder methods which run wiht normal functions, for objecy/calss methods, need Biwi.charm() for instance
# if not name/if name == ""
# raise
# properties - @property/decorators
# getters and setters - to set an attribute you need by going through these functions, setter works for biwi.house =, as well as the init
# class methods - @classmethod decorator - methods for class, not for instances (instances have self), class ones can be used wihtout objects - just class
# class variables - can access without any objects
# static methods
# inheritance - e.g. Student(Person) - super()
# operator overloading - e.g. __add__(self, other)

def get_student():
    return 1,2
value1, value2 = get_student()

def get_biwi():
    biwi = Biwi()
    biwi.name = input("Name: ")
    biwi.house = input("House: ")
    return biwi

def get_Balami():
    name = "Balami"
    house = input("House: ")
    try:
        return Biwi(name, house)
    except ValueError:
        return Biwi("Balami", "Migger")
    

class Biwi:
    def __init__(self, house, patronus="The spirit of SIR RALAM", name=None):
        if not name:
            raise ValueError("Missing Name")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return "a Biwi. Completely unremarkable."

    def charm(self):
        match self.patronus:
            case "The spirit of SIR RALAM": 
                return "🤺"
            case _:
                return "No patronus"
    # getter
    @property #when biwi.house runs, don't look directly for value, run this function
    def house(self):
        return self._house
    # setter
    @house.setter
    def house(self, house):
        if house not in ["Ralamdor", "Balam", "Cralam", "Migger"]:
            raise ValueError("Invalid House")
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise ValueError("Migger")
        elif not name:
            print("No Name??")
        else:
            self._name = name
import random
class Malam():
    houses = ["Ralamdor", "Balam", "Cralam", "Migger"]

    def __init__(self, name):
        self.name = name.upper()
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)

class Malamander(Malam):
    def __init__(self, name):
        super().__init__(name)

class Vault():
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return(f"This bank vault has 0 galleons, sickles and knuts. brokie lol. jk you have {self.galleons} galleons, {self.sickles} sickles, and {self.knuts} knuts")

    def __add__(self, other): #self is lhs vault, other is rhs
        return Vault(self.galleons + other.galleons, self.sickles + other.sickles, self.knuts + other.knuts)

miwi = Vault(10000, 50359, 25235304)
biwi = Vault(0, 0, 3)

from datetime import date
import num2words

class Date():
    def __init__(self, d):
        list1 = d.split("-")
        self.date = date(int(list1[0]), int(list1[1]), int(list1[2]))
    
    def __sub__(self, other):
        raw = str(self.date - other.date).split()
        return int(raw[0])

def age_in_mins():
    birthdate = Date(input("Please input birthdate in YYYY-MM-DD: "))
    difference = (Date(str(date.today())) - birthdate)
    mins_diff = int(difference) * 1440
    print(num2words.num2words(mins_diff), "minutes")

class Jar():
    def __init__(self, capacity, size):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        text = ""
        for i in range(int(self.size)):
            text += "🍪"
        return text

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError("capacity must be positive")
        else:
            self._capacity = capacity

    def deposit(self):
        added = input("How many cookies do you wish to deposit my good sir? ")
        if int(self.size) + int(added) > self.capacity:
            raise ValueError("TOO MANYYYY")
        else:
            self.size = str(int(self.size) + int(added))

    def withdraw(self):
            lost = input("How many cookies do you wish to deposit my good sir? ")
            if int(self.size) - int(lost) < 0:
                raise ValueError("Yu too gredy..!")
            else:
                self.size = str(int(self.size) - int(lost))

