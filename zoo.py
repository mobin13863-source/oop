class Animal():
    zoo_name = "tehran zoo"  # this is a Attribte 
    def __init__(self, name, species, age, sound): 
        # Instance Attribute
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound


    # method to make sound
    def make_sound(self):
        return f' the suond is {self.sound}'
        

    # method to show info animal
    def info(self):
        res = f'name animal is {self.name},the age that{self.age},the sound is {self.sound}and {self.species}'
        return res
    

    # dunder method to represent object as string
    def __str__(self):
        return f'name:{self.name},species:{self.species},age:{self.age},sound{self.sound}'
    
# Create an instance of Animal (Lion)
lion = Animal("Simba", "Lion", 5, "Roar")
print(lion) # calls __str__
print(lion.info()) # show info
print(lion.make_sound()) # show make_sound

# Subclass Bird inherits from Animal
class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        # # Call parent constructor using super()
        super().__init__( name, species, age, sound)
        self.wing_span = wing_span



    #  Override make_sound method
    def make_sound(self):
        return f' the {self.name} chirps {self.sound}'
    
    # Override __str__ method
    def __str__(self):
        return f' name : {self.name}, species : {self.species}, age : {self.age}, sound {self.sound}  Wing span{self.wing_span}'

        
# Create an instance of Bird (Parrot)
parrot = Bird("Polly", "Parrot", 2, "Squawk", 25)
print(parrot)
print(parrot.make_sound())

    