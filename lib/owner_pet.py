class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=""):
        self.name = name
        self.owner = owner
        
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        
        self.pet_type = pet_type
        Pet.all.append(self)
    

class Owner:
    
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet.")
        pet.owner = self
        
    def get_sorted_pets(self): 
        return sorted(self.pets(), key=lambda pet: pet.name)