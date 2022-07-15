# Clothing.py

class clothing:
    def __init__(self, name, minTemp, maxTemp, formal):
        self.name = name
        self.minTemp = minTemp
        self.maxTemp = maxTemp
        self.formal = formal

num_clothes = int(input("Please enter the number of clothing pieces you want to catalog: "))

clothes_list = []

for i in range(num_clothes):
    name = input("Please enter the clothing item: ")
    minTemp = input("Please enter the minimum temp you would like to wear the item: ")
    maxTemp = input("Please enter the maximum temp you would like to wear the item: ")
    formal = input("Would you wear this to a formal event? ")

    clothes_list.append(clothing(name, minTemp, maxTemp, formal))

temperature = input("Please enter the current temperature: ")
is_formal = input("Is the item formal? ")

print("Items that can be worn: ")

for item in clothes_list:
    if temperature >= item.minTemp and temperature <= item.maxTemp:
        if is_formal.lower() == item.formal.lower():
            print(item.name)



