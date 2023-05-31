class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class  AnimalShelter:
    def __init__(self):
        self.animals=[]
    
    
    def enqueue(self,animal):
        if animal.species == "cat" or animal.species == "dog":
            self.animals.append(animal)

    def dequeue(self,pref):
        if pref == "cat" or pref == "dog":
            for i,animal in enumerate(self.animals):
                if animal.species == pref:
                   pop_value= self.animals.pop(i)
                   return pop_value.species
        
        return None
    

    def print_animals(self):
        for animal in self.animals:
            print(f"Species: {animal.species}, Name: {animal.name}")
    





if __name__ == "__main__":
    shelter = AnimalShelter()
    cat1=Animal("cat","LoLo")
    shelter.enqueue(cat1)
    dog1=Animal("dog","zorro")
    shelter.enqueue(dog1)
    cat2=Animal("cat","lossy")
    shelter.enqueue(cat2)
    dog2=Animal("dog","bogy")
    shelter.enqueue(dog2)
    shelter.print_animals()
    print("///////////////////////////")
    print(shelter.dequeue("cat"))
    shelter.dequeue("cat")
    shelter.print_animals()


        