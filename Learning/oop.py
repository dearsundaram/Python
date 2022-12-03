class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def dog_name(self):
        return self.name
    def dog_age(self):
        return self.age
    def dog_chage(self,age):
        self.age = age

d = Dog("Jim",5)
d.dog_chage(10)
print(d.dog_age())


