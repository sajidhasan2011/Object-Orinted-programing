class Parrot:
    
    specias ="bird"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    
blu = Parrot("Blu",10)
woo = Parrot("Woo",15)

print(f"Blu is a {blu.specias}")
print(f"Woo is also a {woo.specias}")

print(f"{blu.name} is {blu.age} years old ")
print(f"{woo.name} is {woo.age} years old ")