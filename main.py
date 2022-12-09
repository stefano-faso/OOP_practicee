class animal:
    def __init__(self,name,age,species):
        self.name = name
        self.age = age
        self.species = species

    def speak(self):
        print(f"I am a {self.species} my name is {self.name} and I am {self.age} years old ")

    def get_age(self):
        print(self.age)

    def get_species(self):
        print(self.species)

    def get_name(self):
        print(self.name)

class dog(animal):

    def __init__(self, breed, name, age, species):
        super().__init__(name, age, species)
        self.breed = breed
    def get_breed(self):
        print(self.breed)
    pass

a = animal("Chris",12,"dog")
a.speak()
a.get_age()
a.get_name()
a.get_species()


b = dog("Shepard",9,"James","dog")
b.speak()
b.get_age()
b.get_name()
b.get_species()
b.get_breed()
