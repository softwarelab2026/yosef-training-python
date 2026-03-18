from ex2 import Animal

def main():
    dog = Animal("rex")
    dog.birthday()
    #print(dir(dog))
    dog.set_animal_name("snow")
    
    print(dog.get_name())
    print(dog.get_age())
    print(dog)


if __name__ == "__main__":
    main()