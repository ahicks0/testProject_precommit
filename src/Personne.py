from datetime import datetime


class Personne:
    def __init__(self, name, age, birthday: datetime):
        self.name = name
        self.age = age
        self.birthday = birthday

    def incrementAge(self):
        self.age += 1

    def rename(self, newname):
        self.name = newname

    def __repr__(self):
        return f"Nom : {self.name}, Age: {self.age}"

    def checkDate(self):
        if datetime.today().date() == self.birthday.date():
            self.incrementAge()
