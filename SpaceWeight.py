# SpaceWeight2.py

class Planet:
    
    Mercury = 0.38
    Venus = 0.91
    Mars = 0.38
    Jupiter = 2.34
    Saturn = 0.93
    Uranus = 0.92
    Neptune = 1.12
    Pluto = 0.62

    def calculate_spaceweight(self, weight, planet_diff):
        planet_weight = weight * planet_diff
        return planet_weight


planet1 = Planet()
weight = float(input("Please enter your weight: "))
planet_diff = planet1.Mercury
list1 = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uransus", "Neptune", "Pluto"]
print(planet1.Mars)

#for i in range(len(list1)):
    #print("Your weight on", list1[i], "is: ", planet1.calculate_spaceweight(weight, planet_diff))

'''

planet_diff = float(input("Please enter the planet diff: "))
planet1.calculate_spaceweight(weight, planet_diff)



print(weight * planet1.Mercury)
print(planet1.Planet)
'''