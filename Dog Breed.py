class Dog:
    animal = "Dog"
    
    def __init__(self,breed,anger,color):
        self.breed = breed
        self.anger = anger
        self.color = color
        
        
chop = Dog("Rottweiler",10,"Black")
alfa = Dog("Siberian Husky",5,"Black,White,Red") 
bob = Dog("Bulldog",9,"Brown and White")
tommy = Dog("Beagle",4,"White,Brown And Black Mixed")
lion = Dog("German Shepherd",8,"Brown And Black Mixed")

print(f"Dog Breed for Chop : {chop.breed}")
print(f"Anger Level  for Chop : {chop.anger}")
print(f"Colour of Chop : {chop.color}")
print(f"Specias of Chop : {chop.animal}")

print(f"Dog Breed for Alfa : {alfa.breed}")
print(f"Anger Level  for Alfa : {alfa.anger}")
print(f"Colour of Alfa : {alfa.color}")
print(f"Specias of Alfa : {alfa.animal}")   

print(f"Dog Breed for Bob : {bob.breed}")
print(f"Anger Level  for Bob : {bob.anger}")
print(f"Colour of Bob : {bob.color}")
print(f"Specias of Bob : {bob.animal}")

print(f"Dog Breed for Tommy : {tommy.breed}")
print(f"Anger Level  for Tommy  : {tommy.anger}")
print(f"Colour of Tommy  : {tommy.color}")
print(f"Specias of Tommy  : {tommy.animal}")  

print(f"Dog Breed for Lion : {lion.breed}")
print(f"Anger Level  for Lion  : {lion.anger}")
print(f"Colour of Lion  : {lion.color}")
print(f"Specias of Lion  : {lion.animal}")


  