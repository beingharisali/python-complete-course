# class Student:
#     name = "Haris"
#     age = 37

# std1 = Student()
# std2 = Student()
# std3 = Student()

# print(std1.name, std1.age)


# class Car:
#     color = 'blue'
#     brand = 'Mercedes'

# car1 = Car()
# car2 = Car()
# car3 = Car()
# car4 = Car()

class Student: # class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("User has been added in the and his info is ", self.name, self.age, self.gender)
    def welcome(self):
        print("I am welcoming all the people and I am ", self.name)
    


std1 = Student('Haris', 37, 'Male') # object
std2 = Student('Anna', 30, 'Female')
std2.welcome()