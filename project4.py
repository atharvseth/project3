class Dog:
    
    animal = "Dog"

    
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour


    def display_details(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Colour:", self.colour)
        print("----------------------")



dog1 = Dog("shitzu", "white and brown")
dog2 = Dog("golden retriever", "golden")


dog1.display_details()
dog2.display_details()