# Physics2.py

class Object:

    def Density(self, mass, acceleration, velocity, volume):
        print("The density is:", (mass / volume))

    def Force(self, mass, acceleration, velocity, volume):
        print("The force is:", (mass * acceleration))

    def Momentum(self, mass, acceleration, velocity, volume):
        print("The momentum is:", (mass * velocity))

mass = float(input("Please enter the objects mass: "))
volume = float(input("Please enter the objects volume: "))
acceleration = float(input("Please enter the objects acceleration: "))
velocity = float(input("Please enter the objects velocity: "))

obj1 = Object()

end = False
while end == False:
    userselection = input("Would you like to calculate density, force, or momentum? ")
    userselection = userselection.lower()

    if userselection == "density":
        obj1.Density(mass, acceleration, velocity, volume)
        end = True
    elif userselection == "force":
        obj1.Force(mass, acceleration, velocity, volume)
        end = True
    elif userselection == "momentum":
        obj1.Momentum(mass, acceleration, velocity, volume)
        end = True
    else:
        print("Invalid choice of calcualtion, Try Again...")
