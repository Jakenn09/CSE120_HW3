# Physics2.py

class Object:
    def __init__(self):
        self.mass = True
        self.volume = True
        self.acceleration = True
        self.velocity = True

obj1 = Object()

obj1.mass = float(input("Please enter the objects mass: "))
obj1.volume = float(input("Please enter the objects volume: "))
obj1.acceleration = float(input("Please enter the objects acceleration: "))
obj1.velocity = float(input("Please enter the objects velocity: "))


def density():
    density = print("The density is:", (obj1.mass / obj1.volume))
    return density

def force():
    force = print("The force is:", (obj1.mass * obj1.acceleration))
    return force

def momentum():
    momentum = print("The momentum is:", (obj1.mass * obj1.velocity))
    return momentum      

i = 0
while i == 0:
    userselection = input("Would you like to calculate density, force, or momentum? ")
    userselection = userselection.lower()

    if userselection == "density":
        density()
        i = 1
    elif userselection == "force":
        force()
        i = 1
    elif userselection == "momentum":
        momentum()
        i = 1
    else:
        print("Invalid response. Try Again")

    
    


