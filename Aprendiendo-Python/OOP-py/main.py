class Person:
    # Static class attribute
    # is independent of the
    # instanciated class
    number_of_people = 0 

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Static attribute +1
        Person.number_of_people += 1

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age


print(Person.number_of_people)
p = Person("buu", 12)
print(p.get_name())
print(p.number_of_people)
p2 = Person("p2", 40)
print(Person.number_of_people)