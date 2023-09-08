import random

names_list = ["Maya", "Shahaf", "Jorden", "Gilad", "Ziv", "Matan", "Koral", "Hen", "Ezra", "Yehuda"]
ids_list = [12345678, 56781234, 98765432, 234567891, 345678921, 456789012, 678901234, 789012345, 890123456, 901234567]
ages_list = [19, 18, 20, 22, 56, 21, 17, 34, 23, 5]



class Person:
    def __init__(self):
        self.name = random.choice(names_list)
        self.id = Person.generate_id(ids_list)
        self.age = random.choice(ages_list)
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def print_attributes(self):
        print(self.name, self.id, self.age)

    @staticmethod
    def generate_id(ids_list):
        random_id = random.choice(ids_list)
        ids_list.remove(random_id)
        return random_id