class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def say(self):
        return "Hi :)"
    
    def __str__(self):
        return "Person {} is {} years old".\
        format(self.__name, self.__age)
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

##################################################

class Student(Person):
    def __init__(self, name = "ros", age = 30, grade_average = 0): 
        super().__init__(name, age)
        self.__grade_average = grade_average

    def get_grade_average(self):
        return self.__grade_average
    
    def set_grade_average(self, average):
        self.__grade_average = average
    
    
