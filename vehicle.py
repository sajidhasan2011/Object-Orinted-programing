class Vehicle:
    
    wheels = 4
    
    def __init__(self,maxSpeed,milage):
        self.maxSpeed = maxSpeed
        self.milage = milage
        

nano = Vehicle(120,30)
lambo = Vehicle(350,3)

print(f"Nano Max Speed :{nano.maxSpeed}")
print(f"Nano Mileage :{nano.milage}")

print(f"Lamborghini Max Speed :{lambo.maxSpeed}")
print(f"Lamborghini Mileage :{lambo.milage}")

print(f"Nano Wheels :{nano.wheels}")
print(f"Lamborghini Wheels :{lambo.wheels}")
        
        
        