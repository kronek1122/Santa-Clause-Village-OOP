
class village_building():
    
    def __init__(self, name, purpose):
        self.name = name 
        self.purpose = purpose

    def __str__(self):
        return f"{self.name} is Santa Clause Village building and intended for {self.purpose}."

    def tenant(self, tenand="Santa Clause"):
        self.tenand = tenand
        return f"In {self.name} you can find {self.tenand}"

