class Animal:
    def __init__(self, animal_name):
        self.__name = animal_name
        self.__age = 0
    
    def birthday(self):
        self.__age += 1
    
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def set_animal_name(self, animal_name):
        self.__name = animal_name

    def __str__(self):
        return f"animal details:\nname: {self.get_name()}\nage: {self.get_age()}"
    

    


def main():
    pass



if __name__ == "__main__":
    main()   