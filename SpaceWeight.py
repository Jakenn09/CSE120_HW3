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
planet_diff = [planet1.Mercury, planet1.Venus, planet1.Mars, planet1.Jupiter, planet1.Saturn, planet1.Uranus, planet1.Neptune, planet1.Pluto]
list1 = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uransus", "Neptune", "Pluto"]
for i in range(len(list1)):
    print("Your weight on", list1[i], "is: ", weight * planet_diff[i])

'''
planet_diff = float(input("Please enter the planet diff: "))
planet1.calculate_spaceweight(weight, planet_diff)

print(weight * planet1.Mercury)
print(planet1.Planet)
'''