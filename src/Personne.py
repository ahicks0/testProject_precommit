class Personne:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def incrementAge(self):
        self.age += 1

    def rename(self, newname):
        self.name = newname

    def __repr__(self):
        return f"Nom : {self.name}, Age: {self.age}"
