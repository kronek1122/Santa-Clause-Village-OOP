
class village_building():
    
    def __init__(self, name, purpose):
        self.name = name 
        self.purpose = purpose

    def __str__(self):
        return f"{self.name} is Santa Clause Village building and intended for {self.purpose}."


class tentant():
    
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return f"This is {self.name} a {self.age} years old {self.type}"

class Elf(tentant):
    
    def attrribute(self, ability = "hard-working"):
        self.ability = ability

class Reindeer(tenant):

    def attrribute(self, ability = "hungry"):
        self.ability = ability

class Santa_Clause(tenant):

    def attrribute(self, ability = "busy"):
        self.ability = ability

class Mrs_Santa(tenant):

    def attrribute(self, ability = "caring"):
        self.ability = ability

