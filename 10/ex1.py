import random
############################################## 
class Plane:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def update_position(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

    def get_position(self):
        return self.x, self.y
############################################## 

class Animal:
    def __init__(self):
        self.name = "ros"
        self.age = 10
    
    def birthday(self):
        self.age += 1
    
    def get_age(self):
        return self.age
    



def main():
    plane1 = Plane()
    #plane1.update_position()
    #xpos, ypos = plane1.get_position()
    #print(xpos, ypos)


if __name__ == "__main__":
    main()
    