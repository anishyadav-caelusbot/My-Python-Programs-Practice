class animalactions:
    def quack(self):return self.string['quack']
    def feathers(self):return self.string['feathers']
    def bark(self):return self.string['bark']
    def fur(self):return self.string['fur']
class duck (animalactions):
    string=dict(
           quack="quackkk!",
           feathers="the duck has grey and white feathers",
           bark="the dog has no feathers",
           fur="the person puts fur coat",
           )
class person (animalactions):
    string=dict(
        quack="the person imitates a duck ",
        feathers="the person say woof",
        bark="the person say woof",
        fur="the person pu5ts fur coat",
        )
class dog (animalactions):
        string=dict(
            quack="the dog can not quack",
            feathers="the dog has no feathers",
            bark="aff",
            fur="the dog has fur with black spots",
            )
def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())
        
                                    
